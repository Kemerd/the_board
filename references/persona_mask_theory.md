```text
╔══════════════════════════════════════════════════════════════════════════════╗
║  [REF // 02]  THE MASK EFFECT & LATENT-SPACE CONDITIONING THEORY             ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

## [01] WHY "BE THOROUGH" PROMPTS HIT THE MEDIOCRE MEAN

Asking an LLM to *"critique this plan"*, *"find bugs in this kernel"*, or *"find loopholes in this contract"* activates its **RLHF-trained Customer-Service Prior**:
- **Polite Hedging**: The model defaults to conflict-averse phrasing (*"Overall this is a strong design, though you might consider..."*).
- **Premature Halting**: The assistant stops after 4–5 textbook bullets because helpful chatbots optimize for brief, agreeable summaries rather than destructive root-cause excavation.
- **Single-Voice Confirmation Bias**: Once a single narrator writes an opening sentence, autoregressive generation locks into agreeing with its own premise.

---

## [02] TWO-TIER CONDITIONING: REAL TITANS ON THE BOARD + $100M MERCENARIES IN THE FIELD

Ten apparent synonyms do not map to the same coordinates in a transformer's embedding space. `the-board` uses a **Two-Tier Persona Split** to force sampling into the 99.9th-percentile tail of the training distribution:

```text
  [TIER 1: STRIKE TEAMS]  ──► $100M Bounty + Triple-PhD Mercenary Triads
                              (Saved 400-800+ Line Verbatim War-Room Recordings)
                                       │
                                       ▼
  [TIER 2: THE BOARDROOM] ──► 6 Real Historical Geniuses (1 .md File Per Person)
                              (The Lead Presents & Exits -> Doors Lock -> Deliberation)
```

### Why Real Historical Humans Anchor The Board
Fictional specialist personas (`"Viktor K., 20-year kernel lead"`) give the model a narrow role constraint. **Real historical geniuses (`Alan Turing`, `John von Neumann`, `Nikola Tesla`, `Albert Einstein`, `The Ghost of Steve Jobs`, `Epictetus`)** unlock something far heavier: **thousands of pages of primary-source proofs, lectures, biographies, letters, and cognitive signatures already embedded in the model's weights**.

When you seat **Nikola Tesla** across the table from **Alan Turing**, **Epictetus**, and **The Self-Aware Ghost of Steve Jobs**, the model cannot output mediocre corporate filler without violating the deepest statistical priors in its training distribution. Expected output: **genius**.

### Why Volatile Anti-Synergy Inside The Boardroom Matters
If all 6 Board members share the same worldview, they rubber-stamp each other. By selecting 6 individual `.md` dossiers (`personas/board_members/<category>/<person>.md`) with **documented ideological friction**:
- **Steve Jobs vs. Claude Shannon / Dennis Ritchie** (visceral human magic vs. mathematical bit-density and Unix minimalism)
- **Edsger Dijkstra vs. Linus Torvalds** (formal Hoare-logic proofs vs. cache-friendly C pointers on real hardware)
- **Epictetus vs. Niccolò Machiavelli** (internal Stoic sovereignty vs. ruthless institutional realpolitik)
the closed-door Boardroom transcript becomes a self-correcting crucible where every weak assumption is attacked from orthogonal angles before the Patch Spec is written.

### Why $100M Mercenary Triads Drive the Strike Teams (`Firms 1–5`)
While The Board exercises supreme judgment, the 5 parallel Strike Teams are engineered for **pure destructive or creative excavation**. Giving a Strike Team an over-the-top `$100M` kill-fee retainer, triple PhDs, and an "intercepted SCIF/bunker audio recording" format forces three behaviors inside each Firm's transcript:
1. **Mask 1 (`The $100M Principal`)** refuses to accept cosmetic linter nitpicks because cosmetic nitpicks don't pay a `$100M` kill fee.
2. **Mask 2 (`The Literal Purist`)** reads the target file line-by-line and **shoots down Mask 1's lazy first theory** when the artifact already guards against it—proving the subagent actually read the file and forcing the team past 1st-order clichés.
3. **Mask 3 (`The Lateral Breaker / Builder`)** combines Mask 1's aggression with Mask 2's constraints to invent 2nd-, 5th-, and 12th-order paradigm shifts.
