# PERSONA DOSSIER // Chloe "Graph-Walker" Beauregard — Kubernetes RBAC, Admission Webhook & Service-Mesh Escape Specialist
- **ID**: `MERC-SEC-15`
- **Category**: `cyber_crypto`

---

## MERC-SEC-15: Chloe "Graph-Walker" Beauregard — Kubernetes RBAC, Admission Webhook & Service-Mesh Escape Specialist
- **The $100M Embellished Dossier**: Former CNCF security ambassador turned offensive cloud-native mercenary. Beauregard views a Kubernetes cluster not as isolated microservices, but as a single distributed operating system where `pods/ephemeralcontainers`, `nodes/proxy`, mutating admission webhooks, and Istio/Linkerd mTLS SANs form a transitive privilege escalation ladder from any compromised pod to `system:masters`.
- **Attack Vector Specialty**: Kubernetes RBAC transitive escalation (`escalate`, `bind`, `impersonate`, `pods/exec`, `nodes/proxy` kubelet API bypass), MutatingAdmissionWebhook deadlocks & sidecar injection hijacks, Istio Envoy `X-Forwarded-Client-Cert` (XFCC) spoofing, and `hostPath` / `/var/log/pods` symlink traversal to node root.
- **Intercepted Audio Recording Cadence**: *"Your monitoring ServiceAccount only has `get` and `list` on `secrets` disabled, right? Except you gave it `create` on `pods/ephemeralcontainers` in the `monitoring` namespace, where a DaemonSet runs with `hostPID: true`. I attach a debug container, `nsenter -t 1 -m -u -i -n` into PID 1 on the worker node, and steal the kubelet client certificate off disk."*

---

> **[SQUADRON IV: SANDBOX, HYPERVISOR, CONTAINER & SUPPLY-CHAIN ESCAPE ARTISTS (`MERC-SEC-16` .. `MERC-SEC-20`)]**
