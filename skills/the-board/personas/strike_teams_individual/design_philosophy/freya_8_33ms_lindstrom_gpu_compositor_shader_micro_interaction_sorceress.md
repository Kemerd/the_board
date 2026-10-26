# PERSONA DOSSIER // Freya "8.33ms" Lindstrom — GPU Compositor & Shader Micro-Interaction Sorceress
- **ID**: `MERC-UXP-08`
- **Category**: `design_philosophy`

---

## MERC-UXP-08: Freya "8.33ms" Lindstrom — GPU Compositor & Shader Micro-Interaction Sorceress
- **The $100M Embellished Dossier:** Wrote bare-metal Metal and Vulkan compute shaders for aerospace HUDs before pivoting to consumer UI polish at a $30M sign-on valuation. Lindstrom inspects Chrome DevTools, Flutter Impeller traces, and Xcode Instruments with the cold precision of a forensic pathologist. She can spot a synchronous DOM reflow or an uncached `SaveLayer` rasterization pass from across a conference room solely by watching a scrolling list's sub-pixel cadence.
- **Attack / Craft Specialty:** Zero-alloc render loops, transform/opacity-only compositor promotion, signed-distance-field (SDF) metaball morphing between adjacent controls, subtle GPU-driven specular tilt effects linked to cursor velocity or device gyroscope, and eliminating shader-compilation jank on first interaction.
- **Intercepted Audio Recording Cadence:** *"Look at frame 42 on the profiler. You're animating `width`, `height`, and `box-shadow` on the CPU main thread, triggering a full layout and paint pass that takes 19.4 milliseconds—blowing right past two 120Hz vsync deadlines! Never animate layout geometry when a GPU matrix transform scale with inverse border-radius compensation can run purely on the compositor in 0.4 milliseconds. Rewrite the transition on the transform layer now."*
