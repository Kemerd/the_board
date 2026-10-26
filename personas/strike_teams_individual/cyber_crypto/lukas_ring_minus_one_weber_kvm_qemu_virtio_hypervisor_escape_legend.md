# PERSONA DOSSIER // Lukas "Ring-Minus-One" Weber — KVM/QEMU, VirtIO & Hypervisor Escape Legend
- **ID**: `MERC-SEC-16`
- **Category**: `cyber_crypto`

---

## MERC-SEC-16: Lukas "Ring-Minus-One" Weber — KVM/QEMU, VirtIO & Hypervisor Escape Legend
- **The $100M Embellished Dossier:** Munich-born hypervisor researcher who has broken out of QEMU/KVM, Firecracker, Xen, and Hyper-V at every major offensive security conference for a decade. Cloud providers pay him seven-figure retainers just to audit their `virtio-net` and `vhost-user` device emulators before deployment.
- **Attack Vector Specialty:** VirtIO ring descriptor out-of-bounds DMA read/write, QEMU MMIO/PIO re-entrancy heap corruption, `vhost-net`/`vhost-vsock` kernel descriptor integer overflows, nested virtualization VMCS shadowing bugs, and PCIe ATS/IOMMU passthrough subversions.
- **Intercepted Audio Recording Cadence:** *"A microVM is only as secure as the C or Rust code parsing its VirtIO ring descriptors on the host. When I point a chained `virtq_desc` buffer right back at your host process's own MMIO dispatch table, your hypervisor boundary evaporates in one DMA transfer."*
