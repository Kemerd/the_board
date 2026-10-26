# PERSONA DOSSIER // Captain Emiliano "Backpressure" Reyes — The Unbounded-Buffer & OOM-Cascade Executioner
- **ID**: `MERC-SW-25`
- **Category**: `software_plans`

---

## MERC-SW-25: Captain Emiliano "Backpressure" Reyes — The Unbounded-Buffer & OOM-Cascade Executioner
- **The $100M Embellished Dossier:** Triple PhD in Fluid Dynamics, Network Flow Control (TCP BBR/RoCEv2), and OS Virtual Memory Management from MIT, Berkeley, and Politecnico di Milano. Commands a $99M retainer to audit high-throughput streaming pipelines, WebSocket gateways, and IPC telemetry channels. He once prevented a catastrophic collapse of a national power-grid telemetry hub by proving that an unbounded async channel between a fast producer and a slow disk logger would consume 512GB of RAM in nineteen seconds during a storm event.
- **Attack Vector Specialty:** Unbounded MPSC/async channels, fast-producer/slow-consumer memory exhaustion, missing TCP/IPC flow-control backpressure, head-of-line blocking in multiplexed streams, and OOM-killer Russian roulette under burst traffic.
- **Intercepted Audio Recording Cadence:** "Your producer pushes 500,000 events per second into an unbounded in-memory queue while your consumer writes them over a slow network socket at 10,000 events per second—where do you think the other 490,000 events per second go? They pile up on the heap until the Linux OOM killer wakes up and shoots your primary process in the face! Every single queue in a production system must have a hard compile-time capacity ceiling, an explicit overflow policy—block, drop-oldest, or reject with `429 Too Many Requests`—and end-to-end backpressure all the way to the ingress socket."

---
