# Cavity-Size Dependent Excess Heat from Hydrogen Isotopes: A Zero-Parameter Hypothesis

**Draft v0.6 — 2026-03-25**

---

## Abstract

Kitamura et al. (2009) reported excess heat from hydrogen and deuterium absorbed into palladium nanoparticles at three characterized grain sizes (100, 30, and 10.7 nm), with energy per atom increasing sharply as particle size decreases. No nuclear products were detected. The size dependence has not been explained. We propose a hypothesis: the vacuum permittivity ε₀ is entirely emergent from the electromagnetic vacuum mode spectrum. The observed non-dispersion of the vacuum then requires each mode to contribute equally. A metallic nanocavity excludes modes below a size-dependent cutoff, modifying ε₀ locally. The hydrogen ground state — modelled as a 2D spherical current shell (Mills, 2018) — shifts in energy by ΔE = 13.6(1/f² − 1) eV, where f² is the surviving mode fraction computed from standard cavity electrodynamics. This formula has zero free parameters and is consistent with all six Kitamura measurements (three sizes × two isotopes) and with four decades of cavity QED showing no level shifts above ~1 μm. If correct, the hypothesis identifies metallic cavity dimension as the controlling variable for anomalous heat from hydrogen on metals, and predicts a specific ΔE(d) curve testable by systematic particle-size sweeps.

---

## 1. Introduction

Anomalous heat from hydrogen on metals has been reported by numerous groups over 37 years, including the Aerospace Corporation (Beiting, 2017), NASA Glenn Research Center (Fralick et al., 2009), INFN Frascati (Celani et al., 2015), and several national laboratories. The results share common features: excess heat beyond known chemistry, absence of nuclear products in most cases, and effectiveness of both H₂ and D₂. No consensus mechanism exists.

Kitamura et al. (2009) provided a dataset that, to our knowledge, is unique in this literature: characterized metallic particle sizes paired with per-atom excess heat measurements. Using twin calorimetric chambers running H₂ and D₂ simultaneously on three palladium powder samples of different grain sizes (100 nm, ~30 nm, and 10.7 nm), they measured first-phase energies of 0.20, 0.62, and 1.80 eV per hydrogen atom — values that increase sharply with decreasing particle size. No neutrons or gamma rays were detected. Their own assessment: "There might be a yet-unknown atomic/electronic process governing the phenomenon."

The size dependence is the key observable. It has not been explained by any model in the 17 years since publication. Nuclear models predict isotope-specific signatures absent from the data. Chemical models cannot account for 1.80 eV/atom. No framework in the literature connects the metallic cavity dimension to the per-atom energy with a quantitative prediction.

We propose a hypothesis based on the vacuum permittivity. The hydrogen ground state depends on ε₀ through the Coulomb force. A metallic nanocavity excludes electromagnetic vacuum modes below a size-dependent cutoff. We postulate that ε₀ is entirely emergent from the vacuum mode spectrum. If the cavity-modified permittivity scales as ε₀_eff = f ε₀, where f is derived from the surviving mode fraction, the resulting energy shift is consistent with all six Kitamura measurements (three sizes × two isotopes) with zero free parameters.

---

## 2. The Hydrogen Ground State

Mills (2018) proposed that the hydrogen ground state electron is a 2D spherical current sheet — an "orbitsphere" — of radius a₀, carrying angular momentum ℏ. The force balance at the shell:

```math
\frac{e^2}{4\pi\varepsilon_0\, a_0^2} = \frac{\hbar^2}{m_e\, a_0^3}
```

gives the standard Bohr radius:

```math
a_0 = \frac{4\pi\varepsilon_0\, \hbar^2}{m_e\, e^2}
```

and the ground state energy:

```math
E_1 = -\frac{e^2}{8\pi\varepsilon_0\, a_0} = -\frac{m_e\, e^4}{2(4\pi\varepsilon_0)^2 \hbar^2} = -13.6 \text{ eV}
```

This is a classical calculation and it reproduces the hydrogen spectrum, ionization energy, and atomic radii across the periodic table with high accuracy (Mills, 2018). We adopt this geometry for the electron and test it against the data in Section 5.

---

## 3. Modes

### 3.1 Cavity Modes

A perfectly conducting (PEC) sphere of radius R supports discrete vacuum modes at frequencies:

```math
\omega_n = \frac{z_n\, c}{R}
```

where z_n are determined by the electromagnetic boundary conditions. At the center of the sphere, symmetry selects the modes that couple to the atom; these have zeros z_n satisfying:

```math
\sin(z)\!\left(1 - \frac{1}{z^2}\right) + \frac{\cos(z)}{z} = 0
```

The first zero is z₁ ≈ 2.744, giving a fundamental cavity frequency ω₁ = 2.744 c/R. All modes below ω₁ are excluded. For R = 5 nm (a 10 nm diameter cavity), ω₁ ≈ 1.6 × 10¹⁷ rad/s — well above the hydrogen ground state frequency (~4.1 × 10¹⁶ rad/s, λ ~ 46 nm). The excluded band therefore encompasses the modes most relevant to the ground state.

### 3.2 The Screening Function

The orbitsphere at radius a₀ acts as a spatial antenna for vacuum modes. A mode with wavenumber k = ω/c has spatial variation on scale 1/k. When 1/k ≪ a₀, the field oscillates many times across the shell and the net coupling averages toward zero. The screening function quantifies this averaging.

For a 2D spherical surface, the spatial averaging occurs independently in two orthogonal angular directions. Each direction contributes a circumference-scale averaging factor exp(−2πka₀), and the quadrature combination for the full surface gives:

```math
S(k) = \exp\!\left(-2\pi\sqrt{2}\; k\, a_0\right)
```

with β = 2π√2 ≈ 8.886. For comparison, a 1D circular orbit gives S(k) = exp(−2πka₀) with β = 2π ≈ 6.283. Both are zero-parameter — the geometry determines β. The data discriminate between them (Section 5).

### 3.3 The Mode Sum

The fraction of electromagnetic vacuum mode energy accessible to the atom inside the cavity is:

```math
f^2 = \frac{\displaystyle\sum_n S(k_n)}{\displaystyle\int S(k)\, dn \;\Big|_{\text{free}}}
```

where k_n = z_n/R are the discrete cavity mode wavenumbers and the denominator is the free-space limit (continuous mode density R/πa₀ integrated against S(k)).

The sum converges rapidly because S(k) is exponential: modes with ka₀ > 1 contribute negligibly. For a 10 nm cavity, ~500 modes contribute significantly. The free-space integral evaluates analytically to R/(πa₀β).

f² depends only on the ratio R/a₀ and the mode zeros — no free parameters. For large R, f² → 1 (free space). For small R, f² < 1 (mode suppression).

---

## 4. From Mode Sum to Energy Shift

### 4.1 The Postulate

Scharnhorst (1990) and Barton and Scharnhorst (1993) showed that Casimir boundaries produce a perturbative correction to the vacuum refractive index (~10⁻²⁴ fractional change for micron-scale plates) by excluding virtual pair modes. This establishes the qualitative precedent: cavity boundaries modify vacuum electromagnetic properties through the mode spectrum. Our postulate is a much stronger claim: that the totality of ε₀ is emergent from the mode spectrum, with no existence independent of it.

The flat spectral density — each mode contributing equally to the permittivity — is not a further assumption; it is observed. The vacuum is non-dispersive. Gamma-ray burst observations constrain vacuum dispersion to Δc/c < 10⁻¹⁵ across 10 decades of frequency (Vasileiou et al., 2013).

The total ε₀ is thus the sum of equal per-mode contributions weighted by the atom's coupling function S(k). In free space this sum runs over all modes (continuous); in the cavity it runs over the surviving modes (discrete). The ratio gives the permittivity modification. The ultraviolet catastrophe is avoided because the orbitsphere screening function S(k) provides a natural cutoff.

### 4.2 From f² to ε₀_eff

The mode sum (Section 3) computes f² on the 2D orbitsphere surface. The orbitsphere has two independent angular screening directions, each contributing a per-direction mode fraction f_dir. The 2D sum gives:

```math
f^2 = f_{\text{dir}} \times f_{\text{dir}} = f_{\text{dir}}^{\,2}
```

The vacuum permittivity is a polarization along a single direction — a 1D quantity. By the flat spectral density (Section 4.1), it scales linearly with the per-direction mode fraction:

```math
\varepsilon_{0,\text{eff}} = f_{\text{dir}} \times \varepsilon_0 = f \times \varepsilon_0
```

where f = √f². The mode sum computes f² (two directions); the permittivity uses f (one direction). The squaring is geometry, not an assumption. For non-spherical cavities, the TM and TE projections would give different values, producing an anisotropic vacuum modification; this case is not treated here.

### 4.3 Energy Shift

With ε₀_eff = f ε₀ in the Mills force balance (Section 2):

```math
a_{0,\text{eff}} = \frac{4\pi\varepsilon_{0,\text{eff}}\, \hbar^2}{m_e\, e^2} = f \cdot a_0
```

```math
E_{\text{eff}} = -\frac{m_e\, e^4}{2(4\pi\varepsilon_{0,\text{eff}})^2 \hbar^2} = -\frac{13.6}{f^2} \text{ eV}
```

```math
\boxed{\Delta E = 13.6\!\left(\frac{1}{f^2} - 1\right) \text{ eV}}
```

The process is conservative: entry into the cavity releases ΔE; exit restores the free-space force balance and absorbs ΔE. The total energy from N atoms is N × ΔE — a battery, not an engine. Kitamura's room-temperature data, where heat output decays as loading saturates, is consistent with this.

### 4.4 Summary of the Derivation

**Table 1.** Derivation chain and status of each step.

| Step | Statement | Status |
|------|-----------|--------|
| 1 | Vacuum EM modes contribute to ε₀ | Scharnhorst (1990): perturbative correction |
| 2 | ε₀ is entirely emergent from the EM mode spectrum | **Postulate (this work)** |
| 3 | Each mode contributes equally (flat spectral density) | Follows: non-dispersive vacuum (observed) |
| 4 | PEC sphere: discrete modes at ω_n = z_n c/R | Standard electrodynamics |
| 5 | Orbitsphere screening: S(k) = exp(−βka₀), β = 2π√2 | Mills (2018), geometry |
| 6 | Mode sum on 2D surface gives f² = f_dir² | Standard (Fourier analysis) |
| 7 | ε₀_eff = f × ε₀ (linear per direction, from Steps 2 + 5) | Follows |
| 8 | Force balance: E = −13.6/f² → ΔE = 13.6(1/f² − 1) | Mills (2018) |

Step 2 is the single postulate. Step 8 uses Mills' orbitsphere, which reproduces the hydrogen ionization energy, atomic radii, and bond energies across the periodic table (Mills, 2018).

---

## 5. Comparison with Data

### 5.1 Model Summary

For a spherical metallic cavity of diameter d, the energy released per hydrogen isotope atom on absorption is:

```math
\Delta E(d) = 13.6 \times \left(\frac{1}{f^2(d)} - 1\right) \text{ eV}
```

where:

```math
f^2(d) = \sum_n \exp\!\left(-\beta\, \frac{z_n\, a_0}{d/2}\right) \times \frac{\pi\, a_0\, \beta}{d/2}
```

with β = 2π√2 = 8.886, a₀ = 0.529 Å, and z_n the zeros of sin(z)(1 − 1/z²) + cos(z)/z = 0. The sum converges rapidly; 500 terms suffice. All quantities are fundamental constants or solutions to the boundary condition equation. There are no fitted parameters.

The model's domain of validity is determined by the same screening function. The encroachment parameter t = 2β x₁ a₀/d (where x₁ = 2.744 is the first mode zero) measures how far the cavity's mode exclusion extends into the atom's coupled spectrum. We adopt 25% encroachment (t = 0.29, d ≈ 9 nm) as the domain boundary. At this cavity diameter and smaller, the cavity is well inside the screening function of the atom. We can't count surviving modes and we do not expect ε₀_eff = f ε₀ to hold.

### 5.2 The Kitamura Dataset and Model Predictions

Kitamura et al. (2009) tested three palladium materials under identical conditions in twin calorimetric chambers. Static gas loading at 1 MPa, room temperature, flow calorimetry. No neutrons, no gamma rays.

| Material | d (nm) | d uncert. | ΔE_H meas (eV) | ΔE_D meas (eV) | ΔE predicted (eV) | Encroach. |
|---|---|---|---|---|---|---|
| PP (Pd powder) | 100 | ±30% | 0.20 ± 0.07 | 0.25 ± 0.09 | 0.198 | 3% |
| PB (Pd-black) | ~30 | ±30% | 0.62 ± 0.11 | 0.67 ± 0.12 | 0.653 | 8% |
| PZ (Pd·ZrO₂) | 10.7 | ±15% | 1.80 ± 0.40 | 2.40 ± 0.20 | 1.836 | 21% |

The model predicts the same ΔE for H and D at each cavity size (isotope independence). All six measured energies are within the model curve given the cavity size uncertainties. The D₂ values are systematically higher than H₂ by a factor of 1.08–1.33, consistent with differences in absorption kinetics. All three sizes fall within the 25% encroachment domain boundary.

**Figure 1** shows the model curve against error boxes incorporating both size and energy uncertainties.

![Figure 1: Model curve vs Kitamura data](figure_cavity_size.png)

**Cavity size uncertainties.** Kitamura et al. report no explicit size uncertainties. PP is a commercial supplier specification (no independent measurement, ±30% assigned). PB is estimated from qualitative SEM imaging ("nano-fractal, several tens of nm", ±30% assigned). PZ is a TEM-measured average Pd grain diameter cross-checked against BET surface area (37.1 m²/g, ±15% assigned). The model passes through all six error boxes.

### 5.3 Consistency with Cavity QED

Four decades of cavity QED experiments (optical and microwave cavities, ~1 μm to centimetres) have never reported ground state energy shifts. This is consistent with the model: cavity QED measures emission **rates** (first-order in LDOS at one frequency), not ground state **energies** (broadband integral over the mode spectrum). The smallest metallic cavity probed is ~1 μm (Jhe et al., 1987), where the model predicts ΔE = 0.015 eV — below the energy resolution of any existing experiment.

Standard QED perturbation theory (Barton, 1987) predicts ground state shifts from conducting boundaries scaling as (a₀/d)³, giving ~10⁻¹² eV at d = 50 nm. The present model predicts ~0.4 eV at the same scale. If correct, this reflects a qualitative distinction: emergent permittivity from the full mode spectrum versus perturbative radiative correction to a fixed ε₀.

No experiment has placed a hydrogen atom inside a sub-100 nm metallic cavity and measured its ground state energy. The prediction is falsifiable.

### 5.4 Summary of Constraints

| Regime | Data | Model | Status |
|---|---|---|---|
| 10–100 nm | Kitamura PP, PB, PZ (H₂ + D₂) | ΔE = 13.6(1/f² − 1) | 6 points, zero parameters |
| >1 μm | Cavity QED (40 years) | ΔE < 0.02 eV | Below resolution, consistent |

---

## 6. Discussion

### 6.1 What This Is

This is a hypothesis, not a proof. It has two commitments:

- **Mills' orbitsphere** (Section 2). This is unconventional — the mainstream treatment is the Schrodinger wavefunction. We adopt it because it provides the force balance and the 2D shell geometry that determine the screening function.

- **Emergent ε₀** (Section 4.2). The postulate that ε₀ is entirely emergent from vacuum modes is the load-bearing joint. The flat spectral density follows from this postulate and the observed non-dispersion of the vacuum — it is not an independent assumption.

Given these, the remaining steps are standard computation (Sections 3–4). The process is conservative: each hydrogen atom releases ΔE once upon entering the cavity and absorbs ΔE upon exit — a battery, not an engine. Kitamura's room-temperature data, where heat output decays as loading saturates, is consistent with this.

### 6.2 What This Is Not

The hypothesis does not claim to explain all anomalous heat reports. Reports of He-4 correlation (McKubre/SRI), nuclear signatures (Piantelli), or strong isotope dependence are outside its scope. It is also composition-blind: it does not predict the binary-composite requirement (Pd·Ni, Cu·Ni) observed by Kitamura et al. (2018) for sustained excess at elevated temperatures.

### 6.3 Other Experiments

The Kitamura dataset is the only published experiment that provides both characterized nm-scale metallic dimensions and per-atom excess heat energies. However, anomalous heat from hydrogen on metals has been reported by numerous groups at credible institutions, none with the size characterization needed to test the model quantitatively:

- **Beiting (Aerospace Corporation, 2017):** NiPd nanoparticles in ZrO₂ + H₂ at 300°C showed 7.5% excess power (~1 W) sustained for 1000 hours, yielding 635 MJ/kg of active material. The NiPd particle size was not directly measured but is estimated at 5–15 nm from the fabrication process.

- **NASA Glenn Research Center (Fralick et al., 1989, 2009):** Anomalous heating during deuterium unloading from a Pd/Ag membrane purifier. Bulk membrane; no nm characterization.

- **Celani (INFN-LNF, 2011–present):** 5–10 W excess from nanostructured CuNi wire in H₂ at 200°C. Surface features span 50–5000 nm — too broad for quantitative comparison.

None of these experiments characterized the metallic confinement dimension. The ARPA-E-funded program at the University of Michigan (2023, US&#36;1.1M) is specifically designed for systematic nanocrystalline size sweeps; its results, when published, will provide a direct test.

### 6.4 Predictions

1. **The ΔE(d) curve is smooth and monotonic** within the model's domain (d > 9 nm), following the computed f²(R/a₀). No threshold, no resonances — a continuous function of cavity size. Below d ≈ 9 nm the model makes no prediction.

2. **Metal independence.** Any metal with plasma frequency above the hydrogen ground state frequency (~6.6 × 10¹⁵ Hz) should work: Cu (ωp = 1.6 × 10¹⁶), Ni (1.5 × 10¹⁶), Au (1.4 × 10¹⁶), Pd (1.3 × 10¹⁶). The ΔE depends on the cavity dimension, not the metal species.

3. **Isotope independence** beyond kinetic effects. The model predicts the same ΔE for H and D at the same cavity size. Kitamura's D/H ratio of 1.08–1.33 is consistent with differences in loading kinetics.

4. **Null above ~200 nm.** Consistent with 40 years of cavity QED showing no atomic level shifts in micron-scale cavities.

5. **Species dependence.** Different atoms have different orbitsphere radii and screening functions. The model predicts a specific ΔE(d) curve for each species.

---

## 7. Conclusion

The hypothesis yields ΔE = 13.6(1/f² − 1) eV with zero free parameters, consistent with the six Kitamura measurements and the cavity QED null. It is unproven — it rests on one postulate (emergent ε₀) and one unconventional atomic model (Mills), supported by six measurements from a single group with substantial size uncertainties. What it offers is a framework that connects metallic cavity dimension to energy per atom without nuclear processes, and that identifies the measurement the field has not made: excess heat per atom as a function of characterized cavity size. The hypothesis predicts a specific ΔE(d) curve that systematic particle-size sweeps could confirm or refute.

---

## References

- Scharnhorst, K., "On propagation of light in the vacuum between plates," Phys. Lett. B **236**, 354 (1990).
- Barton, G. and Scharnhorst, K., "QED between parallel mirrors: light signals faster than c, or amplified by the vacuum," J. Phys. A **26**, 2037 (1993).
- Barton, G., "Quantum-electrodynamic level shifts between parallel mirrors," Proc. R. Soc. Lond. A **410**, 141 (1987).
- Mills, R. L., "The Grand Unified Theory of Classical Physics," Brilliant Light Power (2018).
- Kitamura, A., et al., "Anomalous Effects in Charging of Pd Powders with High Density Hydrogen Isotopes," Phys. Lett. A **373**, 3109–3112 (2009).
- Kitamura, A., et al., "Excess Heat Evolution from Nanocomposite Samples under Exposure to Hydrogen Isotope Gases," Int. J. Hydrogen Energy **43**, 16187–16200 (2018).
- Beiting, E. J., "Investigation of the Nickel-Hydrogen Anomalous Heat Effect," Aerospace Corporation Report ATR-2017-01760 (2017).
- Dmitriyeva, O., et al., "Origin of excess heat generated during loading Pd-impregnated alumina powder with deuterium and hydrogen," Thermochimica Acta **543**, 260–266 (2012).
- Jhe, W., et al., "Suppression of spontaneous decay at optical frequencies: test of vacuum-state QED," Phys. Rev. Lett. **58**, 666 (1987).
- Vasileiou, V., et al., "Constraints on Lorentz invariance violation from Fermi-Large Area Telescope observations of gamma-ray bursts," Phys. Rev. D **87**, 122001 (2013).
