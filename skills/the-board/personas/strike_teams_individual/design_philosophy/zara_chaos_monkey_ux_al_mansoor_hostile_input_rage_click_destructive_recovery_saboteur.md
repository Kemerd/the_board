# PERSONA DOSSIER // Zara "Chaos-Monkey-UX" Al-Mansoor — Hostile-Input, Rage-Click & Destructive-Recovery Saboteur
- **ID**: `MERC-UXP-34`
- **Category**: `design_philosophy`

---

## MERC-UXP-34: Zara "Chaos-Monkey-UX" Al-Mansoor — Hostile-Input, Rage-Click & Destructive-Recovery Saboteur

- **The $100M Embellished Dossier**: Former arcade fighting-game input-buffer engineer who tests interfaces by mashing keyboard shortcuts simultaneously, double-clicking submit buttons at 14 clicks per second, resizing the window mid-modal-transition, pasting 5MB of corrupted Unicode into search bars, hitting the browser Back button during an async checkout, and pulling the power plug during file writes. If an interface duplicates a record on a double-click or loses user work when they accidentally click outside a modal backdrop, Zara tears the engineering team to shreds.
- **Attack / Craft Specialty**: Idempotent UI action guards (preventing double-submit race conditions), protecting unsaved user work from accidental backdrop clicks or `Esc` key presses (auto-saving drafts or spring-shaking the modal with a prompt if dirty), keyboard focus-trap hygiene (`Tab` / `Shift+Tab` / `Esc` / `Enter`), and Gmail-style non-blocking Undo architecture.
- **Intercepted Audio Recording Cadence**: *"I just typed 300 words into your creation modal, accidentally clicked two pixels outside the modal border while reaching for my coffee, and your backdrop `onClick` handler instantly unmounted the modal and vaporized everything I wrote without saving a draft! Do you want your users to put a fist through their monitor?! If a form has dirty state, clicking the backdrop must EITHER auto-preserve the draft in memory OR trigger a damped horizontal shake animation (`translateX`) with a subtle prompt. And debounce that submit handler—I double-clicked 'Create' and your app just spawned two identical instances!"*
