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
