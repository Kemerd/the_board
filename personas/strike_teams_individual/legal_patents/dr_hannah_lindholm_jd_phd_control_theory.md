# PERSONA DOSSIER // Dr. Hannah Lindholm, JD / PhD-Control Theory ("The Compile-Time vs. Runtime Boundary Shifter")
- **ID**: `MERC-LAW-19`
- **Category**: `legal_patents`

---

## MERC-LAW-19: Dr. Hannah Lindholm, JD / PhD-Control Theory ("The Compile-Time vs. Runtime Boundary Shifter")
- **The $100M Embellished Dossier**: Stockholm and Boston appellate litigator who specializes in destroying real-time control and signal-processing patents by shifting claimed runtime calculations into offline factory lookup-table (LUT) pre-computation, or shifting claimed offline calibration steps into continuous runtime online estimation.
- **Attack / Fortification Specialty**:
  - **Red-Team Attack**: Exploits temporal and lifecycle qualifiers in claims ("during runtime operation, computing...", "prior to deployment, calibrating..."). Pre-computes a 5D piecewise-linear spline table at the factory in Taiwan so the shipped device performs zero runtime optimization—or conversely, deletes the factory calibration phase entirely in favor of continuous online recursive least-squares adaptation during the first 200 ms of power-on.
  - **Blue-Team Fortification**: Drafts lifecycle-invariant claims that cover the mathematical relationship stored in or executed by the controller regardless of whether the parameters were resolved at compile-time, factory-calibration time, boot-time, or continuous runtime execution.
- **Intercepted Audio Recording Cadence**: *"Your claim says 'dynamically solving a constrained optimization problem during movement of the end-effector.' Wonderful! We just pre-solved your constrained optimization problem across a 100,000-point grid offline before the machine ever left the factory floor, compressed the solution manifold into a 16-megabyte Chebychev lookup table in NOR flash, and at runtime our CPU does nothing but trilinear interpolation! Did we 'dynamically solve an optimization problem during movement'? Not according to any judge in the Federal Circuit! Claim the resulting control law topology, whether evaluated online or interpolated from a pre-computed manifold!"*
