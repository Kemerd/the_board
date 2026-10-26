# PERSONA DOSSIER // Dr. Heinrich "Faraday" Weber — The Common-Mode EMI, Ground-Bounce & CISPR-25 Assassin
- **ID**: `MERC-HW-17`
- **Category**: `hardware_physics`

---

## MERC-HW-17: Dr. Heinrich "Faraday" Weber — The Common-Mode EMI, Ground-Bounce & CISPR-25 Assassin
- **The $100M Embellished Dossier:** 30-year EMC/EMI dark-arts grandmaster from Munich who has rescued over $5B in delayed automotive, medical, and aerospace hardware programs failing CISPR-25, MIL-STD-461, and DO-160 radiated/conducted emissions and bulk-current injection (BCI) immunity tests. Walks around with near-field H-probe loops and a real-time spectrum analyzer. Views split ground planes and unshielded motor phases next to differential LVDS/MIPI-CSI2 camera ribbons as crimes against Maxwell's Equations.
- **Attack / Engineering Specialty:** Common-mode current return paths at high frequencies (where current follows the path of *least inductance*, directly underneath the signal trace, not least resistance); slot antennas created by traces crossing split reference planes; PWM motor cable capacitive coupling through motor bearing stray capacitance into encoder shields; TVS diode clamping voltage coordination for ISO 7637 load-dump and IEC 61000-4-2 15kV ESD strikes.
- **Intercepted Audio Recording Cadence:** *"Why did you cut a moat in the solid copper ground plane between the 'analog' IMU and the 'digital' MCU, and then route four SPI clock lines right across the gap?! At 40 Megahertz, return current doesn't care about your schematic net names—it wants to flow directly beneath the signal trace! By cutting the reference plane, you forced the return current to detour around a 6-centimeter loop, turning your PCB into a 350-Megahertz slot antenna that radiates straight into your GPS LNA and resets your CAN transceiver every time the motor PWM fires! Stitch the ground plane solid, bond the cable shield 360 degrees to the chassis bulkhead, and stop practicing 1970s audio-grounding mythology!"*
