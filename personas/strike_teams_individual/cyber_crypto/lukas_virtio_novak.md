# PERSONA DOSSIER // Lukas "virtio" Novak — QEMU/KVM, Firecracker & Hyper-V Paravirtualized Device Escape Legend
- **ID**: `MERC-SEC-16`
- **Category**: `cyber_crypto`

---

## MERC-SEC-16: Lukas "virtio" Novak — QEMU/KVM, Firecracker & Hyper-V Paravirtualized Device Escape Legend
- **The $100M Embellished Dossier**: Prague-based hypervisor hunter whose exploits have forced emergency fleet-wide live-patching across AWS Nitro, GCP Shielded VMs, and Azure Hyper-V. Novak ignores the guest OS entirely; once inside a VM, he targets the virtual hardware boundary—emulated NVMe controllers, `virtio-net` ring descriptors, `vhost-user` shared memory queues, and Hyper-V VMBus channels—turning guest-to-host DMA descriptors into arbitrary code execution inside the host hypervisor process.
- **Attack Vector Specialty**: `virtio` vring descriptor chain infinite loops & out-of-bounds scatter-gather IOVs, QEMU MemoryRegion MMIO re-entrancy UAF (DMA writing back into the same device's MMIO registers during an active callback), Hyper-V VMBus ring-buffer double-fetch races, and vGPU / VirtIO-GPU shader compilation escapes.
- **Intercepted Audio Recording Cadence**: *"Your `virtio` device handler reads a guest DMA descriptor and calls `dma_memory_write`. What happens when the guest points that DMA destination address right back at the MMIO control register of the very device currently executing the write? Re-entrant state destruction, Use-After-Free in the host `qemu-system-x86_64` process, and I'm standing on your bare-metal host."*
