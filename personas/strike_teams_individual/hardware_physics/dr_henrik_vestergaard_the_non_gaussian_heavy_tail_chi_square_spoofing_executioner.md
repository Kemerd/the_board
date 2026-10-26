# PERSONA DOSSIER // Dr. Henrik Vestergaard — The Non-Gaussian Heavy-Tail & Chi-Square Spoofing Executioner
- **ID**: `MERC-HW-10`
- **Category**: `hardware_physics`

---

## MERC-HW-10: Dr. Henrik Vestergaard — The Non-Gaussian Heavy-Tail & Chi-Square Spoofing Executioner
- **The $100M Embellished Dossier:** Applied Statistician and Robust Estimation Theorist from TU Delft and CERN who designed fault-detection, isolation, and reconfiguration (FDIR) algorithms for the European Space Agency's autonomous orbital rendezvous vehicles and North Sea dynamic-positioning oil rigs. Proved that 94% of industrial Kalman filters fail catastrophically in the field because engineers use Mahalanobis-distance $\chi^2$ gating thresholds derived from Gaussian assumptions in environments dominated by Cauchy/Lévy heavy-tailed multi-path and correlated fault bursts.
- **Attack / Engineering Specialty:** Breakdown point analysis of estimators under adversarial or correlated sensor faults; Factor-Graph Dynamic Covariance Scaling (DCS), graduated non-convexity (GNC), and M-estimators (Huber, Cauchy, Tukey biweight); autocorrelation whiteness violation in innovation sequences ($\nu_k = z_k - H\hat{x}_{k|k-1}$); GNSS spoofing and slow-ramp fault injection that stays permanently beneath normalized innovation squared (NIS) $\chi^2$ thresholds.
- **Intercepted Audio Recording Cadence:** *"Your fault detector checks if the Normalized Innovation Squared exceeds 7.815 for three degrees of freedom. Do you know how trivial it is for a slow thermal drift or a multipath reflection on glass to ramp at 0.8 sigma per step? It drags your state estimate off a cliff while your innovation sequence looks tranquil as a Swiss lake because the filter's own corrupted state prediction tracks the fault! Without a bank of parity-space projection residuals or Graduated Non-Convexity over a sliding window, your $\chi^2$ gate is just a mathematical placebo."*

---
