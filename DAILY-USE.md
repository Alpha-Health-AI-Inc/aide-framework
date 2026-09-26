# Working day to day

[Manager setup](SETUP.md) / [Employee onboarding](ONBOARDING.md) / [Exchange contract](EXCHANGE-CONTRACT.md)

These are commands a person can give their configured agent. They are instruction-driven workflows, not commands provided by an installed AIDE executable.

| Say this | The agent does this | Evidence it returns |
| --- | --- | --- |
| “Refresh my team context.” | Fetches current approved Four Ps records, preserves local work, and summarizes relevant changes. | Observed commit, source dates and changed records |
| “Publish these findings to my manager.” | Keeps the selected scope, prepares a message and selected work artifacts, publishes and reads them back. | Message ID, remote path and commit; delivery initially pending |
| “Check team updates.” | Reads a frozen branch commit, collects unseen addressed records and writes exact-content receipts. | New work, blockers, decisions and source links; read and reported progress stored separately |
| “Did my update arrive?” | Reads and validates the intended receiver's receipt; records sender verification if absent. | Received, verified, pending or blocked, with the exact evidence |
| “What is the new hire's status?” | Compares onboarding proof, published work and product-access state. | Onboarding and work-publication status reported separately |

## Before publishing

Confirm the recipient and requested action from the assignment and registry. Ask only when ambiguous. Resolve team aliases to explicit recipient IDs and retain the routing version. Inspect the intended diff, exclude private conversation and credentials, and preserve source dates and evidence. QA updates include readable findings plus Feature, Scenario, Given, When, Then, with actual execution status separate.

Use existing standing authority for routine scoped publication. Escalate only a changed scope, consequential action or applicable current approval gate. An old approval does not bypass a current tool rejection.

## When collecting

Retrieve the current exchange branch and freeze its commit. Validate and read only eligible addressed records. Reconcile prior receipts and separate read/reported progress. Do not filter out unseen messages because they were created yesterday. Create one logical receipt per message and receiver; repeated discovery must not repeat a business action.

Tell the manager what changed, who reported it, the evidence date, and what needs a decision. Suppress synthetic tests from business summaries. A useful empty result is: “At [time / commit], no new addressed update was published. Onboarding is [separately evidenced status].” Do not say the employee has done no work.

## When something is missing

| Last evidence | Next action |
| --- | --- |
| Local work only | Publish the approved selection and confirm it on the exact remote branch. |
| Message published, no receipt | Check recipient and collection state; wait for the next authorized reader. |
| Receipt stored, no reply | Delivery succeeded. Keep the requested work pending without resending it. |
| Uncertain publication result | Read the exact path and compare bytes before one bounded retry. |
| Permission, identity or content conflict | Stop the affected action, preserve the cause and name the responsible owner. |

Default checking is manual. Scheduling requires a separately approved and verified trigger, operating window and operator. The manager's laptop being asleep does not stop a published record from existing, but something must run to collect it.

## End a session with a usable checkpoint

Before a planned move, handover or pause, refresh `people/<person-id>/continuity.md` with selected published work, outstanding messages, pending decisions and the next action. Keep local-only work and recovery state accounted for through approved backup references. Routine publication does not automatically publish private session memory.

Say “Resume my AIDE” for a fresh session, “Move my AIDE to this computer” for [device change](DEVICE-CHANGE.md), or “Recover my AIDE” for [interruption recovery](RECOVERY.md). Read [the lifecycle guide](LIFECYCLE.md) before changing ownership or stopping service.

## Improve how the team works

Say “Find an AIDE that can help with this,” “Help me propose a specialist,” or “Build the specialist approved in this proposal.” Read the team catalog before creating another capability. Use [creation](CREATE-AIDE.md) for employee-led proposals and implementation, and [sharing](SHARED-AIDES.md) for existing capabilities. Colleagues use published instructions and Git requests, without needing the creator's chat history.
