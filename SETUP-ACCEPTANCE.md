# Setup acceptance

Use this checklist to prove a particular installation. This page records requirements, not completed test results. The manager approves a concrete evidence report; the agent prepares it.

| Gate | Pass evidence | If missing |
| --- | --- | --- |
| Prepared workspace | Four Ps, organization context, role contracts and rendered configuration exist locally; intended diff reviewed | Prepared only |
| Published workspace | Exact remote repository and branch contain the expected entry point and configuration at a recorded commit | Publication pending or blocked |
| Manager identity | Approved identity mapping agrees with authoritative submission evidence | Identity unverified |
| Employee identity and access | Independent employee session authenticates, reads the approved context and publishes permitted synthetic data | Employee not yet connected |
| Local experience | Employee works in a local checkout without overwriting existing files; remote read-back verifies selected publication | Local setup unverified |
| Product access | Each required system has an owner and independently recorded requested/granted/verified state | Name the blocked system and owner |
| Addressed delivery | Unique employee message names the manager recipient and exists at the configured branch | Test pending |
| Receipt | Manager session reads actual message bytes and publishes a matching receipt | Collection pending |
| Sender verification | Employee session reads that exact receipt and publishes its reference and digest | Verification pending |
| Recovery | Rechecking the same message reuses its receipt; an interrupted pending stage resumes without overwriting history | Recovery unverified |
| Human acceptance | Manager reviews the evidence and expressly accepts the scoped result | Human acceptance pending |

Record actual source paths, commits, observed times, errors and submitting identities in the deployment's `operations/setup-state.json` and a dated `operations/acceptance.md`. Read remote artifacts independently. A tool returning success, a folder existing, or one agent pretending to be the other participant does not establish end-to-end completion.

## Two-session walkthrough

1. Manager session prepares and publishes the approved workspace, then provides the employee link.
2. Employee session independently reads the approved context, prepares a local working folder and publishes one unique synthetic message with its own token.
3. Manager session freezes the branch commit, reads and validates the message and publishes its receipt with the observed token.
4. Employee session retrieves that receipt, verifies the identity and exact content binding, and publishes a sender-verification record.
5. Manager session reads the verification. Both sessions recheck once to confirm they reuse existing records rather than sending another test.
6. Manager reviews the linked evidence. Record product-access gaps and any unmet deployment criteria separately.

If a participant is not active, stop at pending and provide the next manual command. Do not create a schedule or retry loop to conceal the missing counterpart.

The broader [pilot checklist](ADOPTION.md#acceptance-checks) remains required before claiming a reliable enterprise runtime or unattended service. Passing this manual walkthrough alone does not certify all providers, file-level authorization or production readiness.

## Lifecycle acceptance

These are required scenarios, not claimed passes. Use synthetic content and appropriately authorized test identities. Record actual provider, client, versions, date, actors, source commits and observed errors for each result; classify unrun cases as not tested. Never revoke a real employee's access merely to exercise a test.

| Scenario | Required evidence |
| --- | --- |
| Fresh session | Rebuild scope from approved context and checkpoint without private prior-chat access; retain unresolved work. |
| Planned employee computer change | Stop old publisher, independently authenticate replacement, restore selected work and attachments, verify round trip. |
| Manager computer change | Preserve incoming backlog and decision ownership; reconcile last-read versus last-reported status and expose uncertainty. |
| Lost-device recovery | Confirm authorized containment, restore permitted backups, name unrecoverable local work and verify new publisher. |
| Two-device overlap | Detect proposed competing publishers and prevent manual cutover until the old executor is stopped; do not claim this proves an enforced lock. |
| Different agent client | Read pinned procedures, recheck tools and product access, preserve identity and verify independent delivery. |
| Interrupted publication or receipt | Resolve uncertain exact-path writes; rechecking the same record reuses receipt and does not repeat a business effect. |
| Role or manager transfer | Preserve historical identities; transfer pending work with successor acceptance; old-recipient messages remain distinct from forwarded messages. |
| Pause and resume | Observe actual trigger pause, retain backlog and resume against current authorization without resending successful requests. |
| Offboarding | Authorized test identity loses real access; workers stop, work has a successor and history remains readable by authorized team members. |
| Backup restore | Isolated restore matches inventory and checksums, including non-Git dependencies, without activating a second worker. |
| Framework or provider migration | Review pinned diff, retain old evidence and map moved references; verify destination route and recovery plan. |
| Organization expansion | Each added team proves its own identity, routing, permitted data boundary and onboarding; measure operational limits. |

Store outcomes in dated transition and acceptance records. A documentation review or metadata validator cannot satisfy these behavioral gates. See [device change](DEVICE-CHANGE.md), [recovery](RECOVERY.md) and [organization rollout](ORG-ROLLOUT.md).
