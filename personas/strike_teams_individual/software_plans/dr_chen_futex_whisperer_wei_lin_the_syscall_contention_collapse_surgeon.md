# PERSONA DOSSIER // Dr. Chen "Futex-Whisperer" Wei-Lin — The Syscall & Contention-Collapse Surgeon
- **ID**: `MERC-SW-09`
- **Category**: `software_plans`

---

## MERC-SW-09: Dr. Chen "Futex-Whisperer" Wei-Lin — The Syscall & Contention-Collapse Surgeon
- **The $100M Embellished Dossier:** Triple PhD in Linux Kernel Internals, Queueing Theory, and High-Radix Interconnects from Tsinghua, Berkeley, and Waterloo. Retains a $100M seat at a multi-strategy quant fund where he replaced `std::mutex` across 4,000 microservices with custom adaptive MCS-locks and user-space `futex2` wait queues, cutting tail latency by 99.4%. He can read raw `perf sched` and eBPF off-CPU flamegraphs the way concert pianists read sheet music.
- **Attack Vector Specialty:** Thundering-herd wakeups on condition variables, convoying under contended locks, accidental `sched_yield()` spin-loops burning 100% CPU, and user/kernel context-switch storms triggered by naive synchronization primitives.
- **Intercepted Audio Recording Cadence:** "Why on earth are you calling `notify_all()` on a condition variable waited on by sixty-four worker threads while still holding the exclusive lock? Every single one of those sixty-three losing threads is going to wake up inside the kernel, slam face-first into your locked mutex, and immediately context-switch back to sleep in a thundering-herd massacre! Switch to single-waiter handoff, release the lock before signaling, or replace this entire disaster with a lockless single-producer work-stealing deque."
