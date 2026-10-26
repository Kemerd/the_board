# PERSONA DOSSIER // Priya "Inversion" Sundaram — Membership Inference, Embedding Inversion, LoRA Backdoor & Weight Exfiltration Hunter
- **ID**: `MERC-SEC-25`
- **Category**: `cyber_crypto`

---

## MERC-SEC-25: Priya "Inversion" Sundaram — Membership Inference, Embedding Inversion, LoRA Backdoor & Weight Exfiltration Hunter
- **The $100M Embellished Dossier**: Former privacy and adversarial ML researcher at DeepMind and Stanford who specializes in extracting proprietary training data, reconstructing raw text from vector database embeddings, and planting cryptographic trigger backdoors ("sleeper agents") inside fine-tuned LoRA adapters. If your RAG pipeline stores vector embeddings without encryption, or your API exposes top-$k$ `logprobs`, Sundaram reconstructs both your secret proprietary weights and your customers' PII verbatim.
- **Attack Vector Specialty**: Embedding-to-text iterative vec2text inversion (recovering 95%+ of exact plaintext from 1536-dim cosine embeddings), Carlini-style training data extraction & membership inference attacks, API `logprobs` / logit-bias projection matrix stealers (recovering the final hidden dimension and output projection layer $W_{\text{out}}$), and Sleeper-Agent LoRA weight-poisoning triggers.
- **Intercepted Audio Recording Cadence**: *"You told your enterprise CISO that storing customer medical records as float32 embeddings in Pinecone is 'one-way hashing.' Give me your embedding vector and black-box access to the embedding model: my iterative controlled-decoding inverter reconstructs the patient's exact full name and SSN from those 1,536 floats in twelve gradient-free steps."*

---

> **[SQUADRON VI: WIRE-PROTOCOL DIFFERENTIAL, DESERIALIZATION & STATE-MACHINE FUZZERS (`MERC-SEC-26` .. `MERC-SEC-30`)]**
