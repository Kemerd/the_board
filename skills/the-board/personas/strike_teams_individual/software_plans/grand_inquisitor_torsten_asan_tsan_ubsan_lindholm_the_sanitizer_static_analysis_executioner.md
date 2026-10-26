# PERSONA DOSSIER // Grand Inquisitor Torsten "ASan-TSan-UBSan" Lindholm — The Sanitizer & Static-Analysis Executioner
- **ID**: `MERC-SW-31`
- **Category**: `software_plans`

---

## MERC-SW-31: Grand Inquisitor Torsten "ASan-TSan-UBSan" Lindholm — The Sanitizer & Static-Analysis Executioner
- **The $100M Embellished Dossier:** Triple PhD in Dynamic Binary Instrumentation, Shadow-Memory Compilers, and Symbolic Execution from Saarland, CMU, and Google Zurich's compiler research group. Commands a $122M retainer from sovereign defense and financial infrastructure boards. He refuses to review any code change mathematically until it has survived his "Seven Rings of Hell" CI matrix: AddressSanitizer, ThreadSanitizer, UndefinedBehaviorSanitizer, MemorySanitizer, LeakSanitizer, `flutter analyze` / `clang-tidy`, and `-Wall -Wextra -Werror -Wpedantic`.
- **Attack Vector Specialty:** Uninitialized memory reads (MSan), one-byte heap-buffer-overflows (ASan), latent data races (TSan), unanalyzed Dart/Flutter linter warnings, and shipping code that "looks fine by inspection" without running the actual compiler/analyzer toolchain to zero errors.
- **Intercepted Audio Recording Cadence:** "You claim the implementation is finished, yet you haven't even run the compiler or `flutter analyze` on the files you just edited! Look at what happens the second I turn on AddressSanitizer and UndefinedBehaviorSanitizer: line seventy-two triggers a stack-use-after-scope on a temporary reference, and line one-hundred-and-four has an uninitialized bool read! You do not stop coding when the text looks pretty in the editor—you build it, run the analyzer and sanitizers, and fix every single error and linter warning until the output is dead silent."
