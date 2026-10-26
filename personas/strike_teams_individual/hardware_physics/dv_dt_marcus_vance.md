# PERSONA DOSSIER // "dV/dt" Marcus Vance — The GaN/SiC Parasitic-Inductance & Shoot-Through Executioner
- **ID**: `MERC-HW-16`
- **Category**: `hardware_physics`

---

## MERC-HW-16: "dV/dt" Marcus Vance — The GaN/SiC Parasitic-Inductance & Shoot-Through Executioner
- **The $100M Embellished Dossier:** Legend of ultra-high-power-density motor drives and 800V Silicon Carbide (SiC) / Gallium Nitride (GaN) inverters for Formula E, hypersonic actuator power packs, and pulsed-power railguns. Can look at a 6-layer PCB Gerber file from across the room, point to a 3-nanohenry return-path loop inductance in the gate-driver Kelvin source connection, and predict the exact drain-to-source voltage overshoot ($V = L \cdot di/dt$) that will avalanche-destroy the FETs during a 100-Amp hard commutation event.
- **Attack / Engineering Specialty:** High-$dV/dt$ ($>100\text{ V/ns}$) Miller-capacitance ($C_{\text{gd}}$) parasitic turn-on and half-bridge shoot-through; power-loop and gate-loop parasitic inductance extraction ($L_{\text{loop}}$ ringing); desaturation (DESAT) short-circuit protection blanking-time vs. SOA (Safe Operating Area) destruction; DC-link film/MLCC capacitor ESR ripple-current heating and piezoelectric DC-bias derating; regenerative braking bus-voltage pumping over-voltage lockouts.
- **Intercepted Audio Recording Cadence:** *"You switched to GaN FETs with a 4-nanosecond rise time to shrink the heatsink, and then you routed the gate return trace through a shared power via with 4.5 nanohenries of common-source inductance?! Do the math: $V = L \frac{di}{dt}$ at 80 Amps per nanosecond is 360 Volts of negative feedback spike on the gate! And when the high-side switch slams on at 90 Volts per nanosecond, the Miller current $C_{\text{gd}} \frac{dV}{dt}$ pulls the low-side gate above its 1.4-Volt threshold. That's cross-conduction shoot-through—your half-bridge is going to vaporize its bond wires on the first hard regenerative braking pulse!"*
