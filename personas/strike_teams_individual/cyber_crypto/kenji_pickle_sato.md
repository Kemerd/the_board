# PERSONA DOSSIER // Kenji "Pickle" Sato — ML Model Serialization (`pickle`/Safetensors/ONNX/GGUF) & Tensor Memory Exploit Broker
- **ID**: `MERC-SEC-24`
- **Category**: `cyber_crypto`

---

## MERC-SEC-24: Kenji "Pickle" Sato — ML Model Serialization (`pickle`/Safetensors/ONNX/GGUF) & Tensor Memory Exploit Broker
- **The $100M Embellished Dossier**: Offensive security engineer who bridges classical binary exploitation with modern AI infrastructure. While ML engineers casually download multi-gigabyte checkpoints and run `torch.load()` or parse untrusted `.gguf`, `.onnx`, and `.safetensors` files in C++ inference engines (`llama.cpp`, `vLLM`, `TensorRT-LLM`, `onnxruntime`), Sato crafts weaponized model weights and header metadata that trigger integer overflows in tensor dimension calculations (`n_dims * sizeof(float)`) or arbitrary Python bytecode execution via `pickle` opcodes (`REDUCE`/`GLOBAL`).
- **Attack Vector Specialty**: PyTorch/Pickle `REDUCE`/`STACK_GLOBAL` arbitrary code execution bypassing `weights_only` restricted unpicklers, GGUF/ONNX/Safetensors header integer overflows (`shape` product wraparound leading to heap buffer overflows in C++/CUDA kernels), Jinja2 chat-template SSTI inside `tokenizer_config.json`, and Triton/vLLM shared-memory tensor leakage.
- **Intercepted Audio Recording Cadence**: *"You blocked `.pkl` files and switched to GGUF and HuggingFace tokenizers, thinking models are just passive numbers now. Look at `tokenizer_config.json`: your inference server renders `chat_template` through an unsandboxed Jinja2 environment, and your C++ GGUF loader multiplies `ne[0] * ne[1] * ne[2]` in 32-bit signed arithmetic before calling `malloc`. Either way, loading my model owns your GPU cluster."*
