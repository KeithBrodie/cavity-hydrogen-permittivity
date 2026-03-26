"""
Figure: ΔE vs Cavity Size for the Spectral Metric Model
=========================================================

Error boxes: vertical (energy per atom) and horizontal (cavity size).
Kitamura (2009) reports no explicit size uncertainties. Horizontal
error bars estimated from characterization methods:
  PP (100 nm): ±30% — commercial supplier specification, no measurement
  PB (30 nm):  ±30% — SEM qualitative ("nano-fractal, tens of nm")
  PZ (10.7 nm): ±15% — TEM average grain size + BET cross-check

2026-03-22 (original), 2026-03-24 (error boxes)
"""

import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Constants
c = 2.99792458e8
a0 = 5.29177210903e-11
E_H = 13.6
beta = 2 * np.pi * np.sqrt(2)  # 2D surface screening ≈ 8.886

# ============================================================
# TM l=1 mode zeros — exact for first 500, asymptotic for rest
# ============================================================

def tm_l1_equation(x):
    if abs(x) < 1e-10: return 1.0
    return np.sin(x) * (1 - 1/x**2) + np.cos(x) / x

def find_zeros(n_zeros=500):
    zeros = []
    x_scan = np.linspace(0.5, n_zeros * np.pi + 10, n_zeros * 100)
    vals = np.array([tm_l1_equation(x) for x in x_scan])
    for i in range(len(x_scan) - 1):
        if vals[i] * vals[i+1] < 0:
            z = brentq(tm_l1_equation, x_scan[i], x_scan[i+1])
            if z > 0.5:
                zeros.append(z)
            if len(zeros) >= n_zeros:
                break
    return np.array(zeros)

tm_zeros_exact = find_zeros(500)
x1 = tm_zeros_exact[0]  # ≈ 2.744

def get_tm_zeros(n_needed):
    """Get n_needed TM l=1 zeros, exact for first 500, asymptotic for rest."""
    if n_needed <= len(tm_zeros_exact):
        return tm_zeros_exact[:n_needed]
    extra_start = len(tm_zeros_exact)
    extra_n = n_needed - extra_start
    spacing = np.mean(np.diff(tm_zeros_exact[-20:]))
    extra_zeros = tm_zeros_exact[-1] + spacing * np.arange(1, extra_n + 1)
    return np.concatenate([tm_zeros_exact, extra_zeros])


# ============================================================
# f² and ΔE computation
# ============================================================

def compute_f2(d_nm):
    """f² for cavity diameter d_nm using 2D surface screening."""
    R = d_nm * 1e-9 / 2
    n_needed = max(500, int(1.5 * R / a0 / np.pi) + 10)
    n_needed = min(n_needed, 50000)
    mode_zeros = get_tm_zeros(n_needed)
    x_max = 5
    x_modes = mode_zeros * a0 / R
    x_modes = x_modes[x_modes < x_max]
    if len(x_modes) == 0:
        return 0.0
    I_cav = np.sum(np.exp(-beta * x_modes))
    I_free = R / (np.pi * a0 * beta)
    if I_free <= 0:
        return 1.0
    return np.clip(I_cav / I_free, 0, 1)


def compute_dE(d_nm):
    """ΔE in eV for cavity diameter d_nm."""
    f2 = compute_f2(d_nm)
    if f2 <= 0:
        return E_H * 100
    if f2 >= 1:
        return 0.0
    return E_H * (1/f2 - 1)


# ============================================================
# Data with error boxes
# ============================================================

# Kitamura H₂ data: (d_nm, dE_eV, dE_err, d_frac_err)
kit_H = [
    (100.0, 0.20, 0.04, 0.30),   # PP: ±30% size (commercial spec)
    ( 30.0, 0.62, 0.10, 0.30),   # PB: ±30% size (SEM qualitative)
    ( 10.7, 1.80, 0.40, 0.15),   # PZ: ±15% size (TEM + BET)
]

# Kitamura D₂ data
kit_D = [
    (100.0, 0.25, 0.05, 0.30),
    ( 30.0, 0.67, 0.10, 0.30),
    ( 10.7, 2.40, 0.20, 0.15),
]

# ============================================================
# Model curve
# ============================================================

print("Computing model curve...")
# Model curve starts at the 25% encroachment boundary — no predictions below
t_boundary = -np.log(0.75)
d_boundary_val = 2 * beta * x1 * a0 * 1e9 / t_boundary  # ≈ 8.97 nm
d_values = np.logspace(np.log10(d_boundary_val), np.log10(5000), 200)
dE_model = np.array([compute_dE(d) for d in d_values])

# ============================================================
# Figure
# ============================================================

fig, ax = plt.subplots(figsize=(10, 6.5))

# Model curve
ax.plot(d_values, dE_model, 'k-', linewidth=2.5,
        label='Spectral Metric Model\n(zero free parameters)', zorder=2)

# --- Error boxes and data points ---

def plot_error_box(ax, d, dE, dE_err, d_frac, color, alpha=0.15):
    """Draw an error box (rectangle) for a data point."""
    d_lo = d * (1 - d_frac)
    d_hi = d * (1 + d_frac)
    dE_lo = dE - dE_err
    dE_hi = dE + dE_err
    # On log-x axis, use the actual coordinates
    rect = Rectangle((d_lo, dE_lo), d_hi - d_lo, dE_hi - dE_lo,
                      linewidth=0.8, edgecolor=color, facecolor=color,
                      alpha=alpha, zorder=3)
    ax.add_patch(rect)

# H₂ error boxes and points
for d, dE, dE_err, d_frac in kit_H:
    plot_error_box(ax, d, dE, dE_err, d_frac, '#2166ac', alpha=0.15)

h_d = [p[0] for p in kit_H]
h_e = [p[1] for p in kit_H]
h_e_err = [p[2] for p in kit_H]
h_d_lo = [p[0] * p[3] for p in kit_H]
h_d_hi = [p[0] * p[3] for p in kit_H]
ax.errorbar(h_d, h_e, yerr=h_e_err, xerr=[h_d_lo, h_d_hi],
            fmt='o', color='#2166ac', markersize=9,
            capsize=4, linewidth=1.2, markeredgecolor='black', markeredgewidth=0.8,
            label='Kitamura H$_2$ (2009)', zorder=5)

# D₂ error boxes and points
for d, dE, dE_err, d_frac in kit_D:
    plot_error_box(ax, d, dE, dE_err, d_frac, '#b2182b', alpha=0.12)

d_d = [p[0] for p in kit_D]
d_e = [p[1] for p in kit_D]
d_e_err = [p[2] for p in kit_D]
d_d_lo = [p[0] * p[3] for p in kit_D]
d_d_hi = [p[0] * p[3] for p in kit_D]
ax.errorbar(d_d, d_e, yerr=d_e_err, xerr=[d_d_lo, d_d_hi],
            fmt='s', color='#b2182b', markersize=9,
            capsize=4, linewidth=1.2, markeredgecolor='black', markeredgewidth=0.8,
            label='Kitamura D$_2$ (2009)', zorder=5)

# Purcell null
ax.plot(500, 0.0, 'D', color='#7570b3', markersize=11, markeredgecolor='black',
        markeredgewidth=0.8, label='Purcell null (cavity QED, >200 nm)', zorder=5)

# Domain of validity boundary at 25% encroachment
# 1 - exp(-t) = 0.25 → t = 0.2877 → d = 2*beta*x1*a0/t
t_boundary = -np.log(0.75)  # = 0.2877
d_boundary = 2 * beta * x1 * a0 * 1e9 / t_boundary  # ≈ 8.97 nm
ax.axvline(x=d_boundary, color='#cc6600', linewidth=1.5, linestyle='--', alpha=0.7, zorder=1)
ax.text(d_boundary * 0.82, 2.8, f'25% encroachment\nd = {d_boundary:.0f} nm',
        fontsize=8.5, ha='right', color='#cc6600', style='italic')

# Formatting
ax.set_xscale('log')
ax.set_xlabel('Cavity diameter (nm)', fontsize=14)
ax.set_ylabel('Energy per hydrogen atom (eV)', fontsize=14)
ax.set_xlim(d_boundary * 0.92, 3000)
ax.set_ylim(-0.2, 3.5)
ax.legend(loc='upper right', fontsize=9.5, framealpha=0.95)
ax.grid(True, alpha=0.3, which='major')
ax.grid(True, alpha=0.15, which='minor')
ax.tick_params(labelsize=12)
ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='-')

# Custom x-axis ticks
ax.set_xticks([3, 5, 10, 30, 100, 300, 1000, 3000])
ax.set_xticklabels(['3', '5', '10', '30', '100', '300', '1000', '3000'])

plt.tight_layout()
import os
_dir = os.path.dirname(os.path.abspath(__file__))
plt.savefig(os.path.join(_dir, 'figure_cavity_size.png'), dpi=200)
plt.savefig(os.path.join(_dir, 'figure_cavity_size.pdf'))
print("\nFigures saved.")

# ============================================================
# Verify: does the model curve pass through all error boxes?
# ============================================================

print("\nModel vs error boxes:")
print(f"  {'Material':>10}  {'d':>6} {'±d':>8}  {'ΔE_pred':>8}  {'ΔE_meas':>8} {'±ΔE':>5}  "
      f"{'in_box?':>7}")
print("  " + "-" * 65)

for label, data in [("H₂", kit_H), ("D₂", kit_D)]:
    for d, dE, dE_err, d_frac in data:
        # Model prediction at central d
        pred_center = compute_dE(d)
        # Model range across the d error bar
        pred_lo = compute_dE(d * (1 + d_frac))  # larger d → smaller ΔE
        pred_hi = compute_dE(d * (1 - d_frac))  # smaller d → larger ΔE
        # Does any part of the model range overlap the energy error bar?
        model_range = (pred_lo, pred_hi)
        data_range = (dE - dE_err, dE + dE_err)
        overlap = model_range[0] <= data_range[1] and model_range[1] >= data_range[0]
        name = f"{label} d={d:.0f}" if d > 20 else f"{label} d={d}"
        print(f"  {name:>10}  {d:6.1f} ±{d*d_frac:5.1f}  "
              f"{pred_center:8.3f}  {dE:8.2f} ±{dE_err:.2f}  "
              f"{'YES' if overlap else 'NO':>7}")
        print(f"  {'':>10}  model range: [{pred_lo:.3f}, {pred_hi:.3f}]  "
              f"data range: [{data_range[0]:.2f}, {data_range[1]:.2f}]")
