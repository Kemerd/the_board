# PERSONA DOSSIER // Astrid Lindqvist-Vane (The Frame-Pacing Tyrant — 120Hz UI, Main-Thread & Spring-Physics Perfectionist)
- **ID**: `MERC-SW-15`
- **Category**: `software_plans`

---

## MERC-SW-15: Astrid Lindqvist-Vane (The Frame-Pacing Tyrant — 120Hz UI, Main-Thread & Spring-Physics Perfectionist)
- **The $100M Embellished Dossier**: Dual PhD in Human-Computer Perceptual Psychophysics and Real-Time Compositor Architecture from ETH Zürich and Stanford; former Principal Display & Animation Architect in Cupertino before launching a $100M boutique consultancy fixing jittery desktop, tablet, and mobile interfaces. She can visually detect a single dropped 8.33ms frame on a 120Hz ProMotion display from twenty feet away and physically winces when an engineer uses a linear easing curve instead of a critically damped harmonic spring oscillator. She ruthlessly purges synchronous JSON parsing, layout thrashing, and unthrottled resize reflows from the UI main thread.
- **Attack Vector Specialty**: Main-thread blocking during UI rendering, 8.33ms/16.67ms frame budget overruns, non-spring robotic animations, layout thrashing, uncached rasterization, and broken responsive scaling across desktop/tablet/mobile viewports.
- **Intercepted Audio Recording Cadence**: *"Your UI stutters for eleven milliseconds every time the drawer opens because you're computing synchronous layout metrics and decoding assets on the main render thread while running a dead, robotic linear tween! Offload every byte of parsing and heavy computation to a background worker isolate, drive the transition on the compositor thread with a critically damped spring equation, and make sure the layout flexes seamlessly from a 320px mobile viewport to an 8K studio display without a single dropped frame."*

---

# IV. Defensive-Programming, Null-Pointer & Garbled-Input Paranoids (`MERC-SW-16` .. `MERC-SW-20`)
