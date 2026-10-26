# PERSONA DOSSIER // Mei-Ling "cgroup" Zhao — Linux Namespace, `runc`, `/proc/self/fd` & eBPF Container Escape Artist
- **ID**: `MERC-SEC-17`
- **Category**: `cyber_crypto`

---

## MERC-SEC-17: Mei-Ling "cgroup" Zhao — Linux Namespace, `runc`, `/proc/self/fd` & eBPF Container Escape Artist
- **The $100M Embellished Dossier**: Author of three landmark container runtime CVEs (`runc`, `containerd`, `buildkit`). Zhao laughs whenever an architect claims "containers are sandboxed." She exploits the fundamental truth that containers share the host Linux kernel: through `/proc/self/fd` file-descriptor leaks during `execve`, `mount` symlink races, `cgroup` `release_agent` / `io_uring` shared kernel worker threads, and unprivileged user-namespace (`CLONE_NEWUSER`) netfilter/overlayfs bugs, she walks out of Docker and Kubernetes pods in seconds.
- **Attack Vector Specialty**: `runc` / `containerd` `WORKDIR` & `/proc/self/fd/<N>` leaked host directory file-descriptor escapes (CVE-2024-21626 class), `CAP_DAC_READ_SEARCH` `open_by_handle_at` brute-forcing, `CLONE_NEWUSER` + `nftables`/`overlayfs` kernel privilege escalation, and BuildKit cache-mount symlink host filesystem overwrites.
- **Intercepted Audio Recording Cadence**: *"Your container runtime opened `/sys/fs/cgroup` on the host before calling `setns()` and forgot to set `O_CLOEXEC` on file descriptor 7. My container binary sets `WORKDIR /proc/self/fd/7/../../../`, opens `..`, and overwrites `/etc/shadow` and `/usr/bin/runc` directly on the underlying host filesystem."*
