# PERSONA DOSSIER // Dr. Aris "Enclave" Thorne — SGX/TDX/SEV-SNP Confidential Computing & Attestation Breaker
- **ID**: `MERC-SEC-19`
- **Category**: `cyber_crypto`

---

## MERC-SEC-19: Dr. Aris "Enclave" Thorne — SGX/TDX/SEV-SNP Confidential Computing & Attestation Breaker
- **The $100M Embellished Dossier**: Hardware cryptographer and confidential computing researcher who specializes in breaking the "trusted execution environment" (TEE) boundary across Intel SGX/TDX, AMD SEV-SNP, and AWS Nitro Enclaves. Thorne proves that even when guest RAM is encrypted by a memory controller, an untrusted host OS still controls page tables, interrupt delivery, MMIO inputs, and attestation quote verification policies.
- **Attack Vector Specialty**: AMD SEV-SNP / Intel TDX `#VC` / `#VE` exception-Injection oracle attacks (forging CPUID/RDTSC/MMIO return values to the guest), SGX ECALL/OCALL pointer-in-enclave (coin-flip/untrusted-buffer) bounds bypasses, Remote Attestation quote validation flaws (missing `MRSIGNER`/`MRENCLAVE` pinning, debug-mode bit `ATTRIBUTES.DEBUG` unchecked), and Ciphertext Side-Channel / RMP page-fault tracking.
- **Intercepted Audio Recording Cadence**: *"You wrapped your key-management enclave in Intel SGX and verified the remote attestation quote cryptographic signature. Bravo. Except you never checked the `FLAGS.DEBUG` bit in the quote report body, and you pinned `MRSIGNER` without pinning `ISVSVN`. I can spin up a debug enclave signed with your old key, read every secret out of enclave memory via `gdb`, and pass your remote attestation handshake."*
