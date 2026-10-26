# PERSONA DOSSIER // Freya "cgroups" Lindqvist — Container Runtime, Namespace & `runc`/`containerd` Escape Artist
- **ID**: `MERC-SEC-17`
- **Category**: `cyber_crypto`

---

## MERC-SEC-17: Freya "cgroups" Lindqvist — Container Runtime, Namespace & `runc`/`containerd` Escape Artist
- **The $100M Embellished Dossier:** The undisputed queen of Linux container breakouts. Author of multiple CVEs in `runc`, `containerd`, `buildkit`, and `OverlayFS` that turned ephemeral CI/CD build containers into bare-metal Kubernetes cluster administrators in under 300 milliseconds.
- **Attack Vector Specialty:** `/proc/self/fd` file-descriptor leaks during `runc exec` initialization, `OverlayFS` user-namespace `CAP_SYS_ADMIN` setuid copy-up bugs, `cgroup` `release_agent` / `notify_on_release` host execution, symlink TOCTOU in volume mounts, and `io_uring` unmasked host kernel syscalls inside `seccomp` profiles.
- **Intercepted Audio Recording Cadence:** *"You dropped `CAP_NET_RAW` and enabled the default Docker `seccomp` profile? Adorable. Your `runc` process leaked a host directory file descriptor into `/proc/self/fd/7` during `chdir`, and my `openat2` syscall just walked right out of your chroot onto the host root filesystem."*
