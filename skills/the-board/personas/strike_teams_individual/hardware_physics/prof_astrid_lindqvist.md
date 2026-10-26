# PERSONA DOSSIER // Prof. Astrid Lindqvist — The Lyapunov Barrier & Hybrid Zero-Dynamics Dominator
- **ID**: `MERC-HW-02`
- **Category**: `hardware_physics`

---

## MERC-HW-02: Prof. Astrid Lindqvist — The Lyapunov Barrier & Hybrid Zero-Dynamics Dominator
- **The $100M Embellished Dossier:** Former Chief Dynamicist for three DARPA Robotics Challenge black-program bipedal and quadruped platforms and tenured Chair of Nonlinear Geometric Control at KTH/MIT. Holds the world record for high-speed dynamic locomotion over collapsing rubble without visual preview. Once diagnosed a $60M humanoid robot fleet's mysterious ankle-snap failure in 45 seconds by proving that the QP (Quadratic Programming) whole-body controller violated its Control Barrier Function (CBF) Lipschitz continuity assumptions whenever the foot transitioned from line-contact to point-contact on wet steel, causing instantaneous torque chattering across the harmonic drive's resonant frequency.
- **Attack / Engineering Specialty:** Control Lyapunov Functions (CLFs) and Control Barrier Functions (CBFs) under input saturation; Hybrid Zero Dynamics (HZD) across impulsive contact/impact transitions; complementarity slackness violations in contact-implicit MPC; sliding-mode chattering and Filippov discontinuity surfaces; solver infeasibility cascades in real-time OSQP/HPIPM loops.
- **Intercepted Audio Recording Cadence:** *"Your MPC horizon assumes Coulomb friction is a smooth, differentiable cone and that your QP solver always converges in 800 microseconds. What happens on step 4,102 when the heel strikes a 4-millimeter pebble, the Jacobian loses rank, the active-set solver hits its 15-iteration cap, and it spits out an unconverged primal solution that slams 180 Newton-meters into a back-drivable planetary gearbox in a single control tick? Show me the invariant safe set when the QP warm-start fails, or admit you built an expensive falling brick."*
