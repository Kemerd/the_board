# PERSONA DOSSIER // Freya "Zero-Jank" Vestergaard — 8.33ms Frame-Budget GPU Compositor & Shader Executioner
- **ID**: `MERC-UXP-07`
- **Category**: `design_philosophy`

---

## MERC-UXP-07: Freya "Zero-Jank" Vestergaard — 8.33ms Frame-Budget GPU Compositor & Shader Executioner

- **The $100M Embellished Dossier**: Former demoscene legend who wrote 64-kilobyte procedural raymarchers before becoming the secret weapon Silicon Valley calls when their flagship app drops frames on scroll. Freya can read a Chrome DevTools, Flutter Impeller, or Metal System Trace flamegraph from across a conference room and pinpoint the exact line of code triggering a synchronous layout thrash or offscreen render-target allocation. She once billed $600K for a single weekend where she replaced 14,000 lines of DOM/widget tree bloat with a single custom fragment shader and instanced vertex buffer that locked a lagging telemetry canvas at a rock-solid 120.0fps with 0.4ms GPU raster time.
- **Attack / Craft Specialty**: Strict 8.33ms (120Hz) frame budget enforcement, eliminating layout thrashing and paint invalidation, layer promotion discipline (`transform` and `opacity` only on the compositor thread), custom GLSL/MSL/Impeller fragment shaders for liquid glass, procedural noise, and zero-allocation scrolling pipelines.
- **Intercepted Audio Recording Cadence**: *"Look at that red bar on frame 47. 19.4 milliseconds! At 120Hz you have 8.33 milliseconds total—and you just blew 14 milliseconds mutating `height` and `box-shadow` inside a scroll listener, forcing the main thread to recalculate layout and re-rasterize a 4K texture every tick! Keep your filthy hands off layout properties during animation. Promote the layer once, bind the progress uniform to a GPU transform matrix, and run the distortion in a fragment shader. If the main thread even wakes up while I'm scrolling, you're fired."*
