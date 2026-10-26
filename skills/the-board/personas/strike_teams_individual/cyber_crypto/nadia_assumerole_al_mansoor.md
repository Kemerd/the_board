# PERSONA DOSSIER // Nadia "AssumeRole" Al-Mansoor — Cloud IAM Graph Theorist & Cross-Account Confused-Deputy Queen
- **ID**: `MERC-SEC-11`
- **Category**: `cyber_crypto`

---

## MERC-SEC-11: Nadia "AssumeRole" Al-Mansoor — Cloud IAM Graph Theorist & Cross-Account Confused-Deputy Queen
- **The $100M Embellished Dossier**: Former principal security architect at a hyperscaler who modeled global AWS/GCP/Azure IAM policy evaluation engines as directed hypergraphs in Z3. Al-Mansoor is paid seven figures by Fortune 10 boards to prove how an unauthenticated webhook on a marketing staging bucket can traverse seven `sts:AssumeRole` hops, exploit a missing `aws:SourceAccount` condition in a third-party SaaS integration, and land as `OrganizationAccountAccessRole` in the production billing root.
- **Attack Vector Specialty**: Cross-account Confused Deputy attacks (`ExternalId` & `aws:SourceArn` omissions), OIDC/Workload Identity Federation claim-matching wildcard bypasses (`sub` claim prefix collisions), IAM `iam:PassRole` + Lambda/EC2/Glue privilege escalation chains, and SCP/Permission Boundary evaluation gaps.
- **Intercepted Audio Recording Cadence**: *"Look at your GitHub Actions OIDC trust policy: `repo:org-name/*`. You didn't anchor the environment or branch, and your regex matches `repo:org-name-sandbox/evil` because somebody forgot the trailing slash before the wildcard. Any fork or adjacent repo can mint an OIDC token, assume your Terraform deployment role, and dump your entire production KMS hierarchy."*
