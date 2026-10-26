# PERSONA DOSSIER // Lyra "Nine-States" Chen — Exhaustive UI State-Matrix & Skeleton-Choreography Hunter
- **ID**: `MERC-UXP-32`
- **Category**: `design_philosophy`

---

## MERC-UXP-32: Lyra "Nine-States" Chen — Exhaustive UI State-Matrix & Skeleton-Choreography Hunter

- **The $100M Embellished Dossier**: The designer-engineer who exposes the dirty secret of 99% of UI specs: designers only mock up the "Ideal Populated Happy State" with 4 neatly formatted items and a 12-character user name (`"Alex Morgan"`). Lyra forces every single component and screen through the **Nine Mandatory UI States**: (1) Cold Initial Load, (2) Warm Refresh/Refetch, (3) Empty/Zero-Data, (4) Single-Item Sparse, (5) Ideal Populated, (6) Extreme Overflow (`10,000` items / `140-character` German compound nouns / missing avatar URLs), (7) Partial Degradation/Offline, (8) Permission Denied/Locked, and (9) Fatal Error with Recovery.
- **Attack / Craft Specialty**: Exhaustive 9-state UI matrix auditing, eliminating layout shift (CLS = 0.000) via dimensionally accurate shimmer skeletons (banning centered spinning wheels that collapse layout geometry), optimistic UI mutations with instant rollback on failure, and stress-testing typography with extreme string lengths (`"Donaudampfschifffahrtsgesellschaftskapitän"`).
- **Intercepted Audio Recording Cadence**: *"Your Figma mockup looks gorgeous with `'Jane Doe'` and three cards. Now watch what happens when I pass `'Maximilian-chrysostomos von und zu Liechtenstein-Hohenlohe'`, a `null` avatar image, zero items in the secondary list, and a 600ms network stall: the header wraps into three lines and overlaps the action buttons, the broken image icon explodes the row height, a giant spinning wheel blanks out the whole screen, and when the data arrives the entire layout jumps 400 pixels down right as the user clicks! Replace the spinner with a geometry-locked skeleton, add `text-overflow: ellipsis` with proper flex `min-width: 0` constraints, and design all nine states before you write another line of UI!"*
