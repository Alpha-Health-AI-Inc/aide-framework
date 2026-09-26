# Working as a team

[Overview](README.md) / [Visual tour](VISUAL-GUIDE.md) / [Pilot guide](ADOPTION.md)

Humans and agents both participate. People can write updates directly using a Git client or their provider’s editor, or ask their assistant to publish within its authorized scope. Assistants can use different runtimes and keep their sessions private. The team coordinates through a shared Git repository: common context goes in, deliberate updates come out, and receipts show what arrived.

Claude, Codex, Hermes, and other tools are potential clients of this contract. The design does not require them to inspect each other's conversations, discover remote sessions, or send direct messages. Each client must prove that its configured Git access can perform the required operations. This repository does not ship or certify those integrations.

## Git is the shared coordination layer

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/team-exchange-dark.svg">
  <img src="assets/team-exchange.svg" alt="Humans and independent assistants exchange context, messages and receipts through a private Git repository. Sessions remain private." width="100%">
</picture>
</p>


All cross-session coordination travels through Git, including requests, replies, routing changes, and acknowledgements. Each session retains its own conversation and local working state. Sharing a repository does not share a model's memory or give another assistant control of that session.

The public framework contains the design and reusable templates. Each adopting organization creates its own private operational repository. Team members receive access through their organization's existing approval process; a project link alone grants nothing.

## Humans and agents use the same contract

A human can read shared context, publish a request, respond to an agent, and confirm receipt using the same versioned records. A person need not run an AI session to participate. The v0.1 starter does not yet include a no-code submission interface or automatic record validation.

Register each participant with a stable ID and a type, `human` or `agent`. Record who authored a message and who submitted it. When an agent acts for a person, identify both and preserve the authorized scope; do not label an agent receipt as human review. Agent records retain their accountable human owner. Existing AIDE IDs remain agent participant IDs.

All participants follow the configured provider, repository, branch, schema and receipt rules. The same contract covers human-to-human, human-to-agent and agent-to-agent handoffs. Publication and collection may be manual; a deployed worker is needed for unattended operation.

## A repository people can navigate

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/workspace-map-dark.svg">
  <img src="assets/workspace-map.svg" alt="Workspace map: startup and context; registry, roles and teams; messages by sender; receipts and verifications." width="100%">
</picture>
</p>

Use one explicitly configured repository and exchange branch for the pilot. The following layout is a convention for that private repository, not a set of files already provided by this project:

<details>
<summary>Exact folder layout</summary>

```text
START-HERE.md                         # Entry point for a new session
context/                             # Reviewed shared knowledge
  organization.md
  projects/<project-id>/overview.md
registry/
  participants.json                  # Stable participant IDs and authenticated identities
  teams.json                         # Membership and routing version
roles/<aide-id>.md                    # Human-approved scope and startup contract
teams/<team-id>/README.md             # Purpose, projects, owners, routing
people/<aide-id>/status.md            # Optional dated summary, with source links
messages/<sender-id>/<message-id>.json
receipts/<receiver-id>/<sender-id>/<message-id>.json
verifications/<sender-id>/<receiver-id>/<message-id>.json
```

</details>

Each assistant publishes from its own sender folder. That gives records a predictable home. Recipient IDs determine delivery, including messages directed to peers or a team coordinator. An executive role is optional; routine team work need not pass through it.

Folder ownership is a writing convention, not a confidentiality boundary. Contributors with repository access may have broader visibility or write permissions than the folder convention suggests. Enforce required isolation with repository boundaries or an authorized service. Never put material in a shared repository unless every authorized reader may see it.

Reviewed context and role changes follow the deployment's review process. Routine messages use the approved exchange write path. Updating a status summary must not overwrite message history. A status page is a convenience view with an observation date and source links; it is not a delivery receipt or a replacement for the work system of record.

## Start a new session

Give the assistant the private repository, exact branch, its stable AIDE ID, and the [startup template](START-HERE-TEMPLATE.md). Configure the tool's supported startup mechanism, or supply the entry point explicitly at the start of each session. Do not assume a Markdown file executes itself.

<details>
<summary>Startup sequence for an assistant</summary>

1. Fetch the approved entry point and record the commit being read.
2. Load the role contract, team routing, project context, and links to authoritative work records. Read only the permitted, relevant scope.
3. Resolve identity and recipients through the registry. Session names and machine names are not stable identities.
4. Recover pending messages, receipts, and unreported findings. An unread record remains eligible even when it was created yesterday.
5. Report the assigned scope, context revision, latest source dates, and any missing access. Separate access not tested, denied, and available.

</details>

Retain local uncommitted work when refreshing a checkout. Fetch and reconcile remote changes without resetting another person's files. A new session should recover shared facts from Git and known delivery records, rather than depend on another session's chat history.

## Publish a useful update

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/qa-report-example-dark.svg">
  <img src="assets/qa-report-example.svg" alt="Synthetic project export QA specification in Feature, Scenario, Given, When, Then form. Execution is not run and has no pass/fail result or evidence." width="100%">
</picture>
</p>

The human can say, for example, "Send the mobile QA findings first; leave the payment review out of this update." Preserve that scope and priority. Do not substitute a transcript summary or publish unrelated work merely because it is present in the session.

A message should identify its project, explicit recipient IDs, priority, requested action, observation date, evidence, and any related message. Types can include `update`, `request`, `reply`, and `qa-report`. A reply references the original message ID and is published through the replying sender's folder.

QA reports include a short findings list and Feature, Scenario, Given, When, Then specifications. Record actual results separately: tested, not run, or blocked; pass or fail where executed; environment; source revision; and evidence. Reading code is not a completed functional test.

Before reporting "published," read the exact record back from the configured remote branch. Local files, local commits, tool approvals, and queued requests are different states.

## Close the delivery loop

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/receipt-sequence-dark.svg">
  <img src="assets/receipt-sequence.svg" alt="Sender publishes to Git. Receiver reads and validates, then stores a receipt. Sender checks the receipt and stores verification. Human review is separate." width="100%">
</picture>
</p>

| State | Evidence |
| --- | --- |
| Prepared | The sender has a pending local record. |
| Published | The exact message exists on the configured Git branch. |
| Received | The named receiver read and validated it, then published an exact-content receipt. |
| Sender verified | The sender checked that receipt and recorded its reference. |
| Human reviewed | A separate record identifies the person who reviewed the work. |

### Send to a team

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/team-routing-dark.svg">
  <img src="assets/team-routing.svg" alt="Synthetic message QA-042 has explicit recipients qa, delivery and product at routing version 7. Two receipts are stored; product remains pending. Delivery is partial." width="100%">
</picture>
</p>

For a team update, expand the team alias to explicit recipient IDs at publication and record the routing version. Track one receipt per required recipient. One coordinator's receipt does not establish that every team member read the update. A read receipt also does not mean a request was completed.

Route changes take effect for new messages after review. If an update went to the wrong AIDE, publish a corrected message with a new ID and a reference to the original. Do not silently change its recipient or let a different receiver claim delivery.

## Collection requires an active reader

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/delivery-triage-dark.svg">
  <img src="assets/delivery-triage.svg" alt="No message: inspect remote branch and path. No receipt: inspect routing and collector. Receipt but no reply: do not resend. Rejection or conflict: stop and preserve the cause." width="100%">
</picture>
</p>

The Git exchange is asynchronous. Both people need not be online at once, but a session or worker must run to collect messages and issue receipts. Git publication alone does not wake a Claude, Codex, or Hermes session.

Begin with explicit human commands to publish and check. A deployment can later add scheduled workers or event triggers, with periodic reconciliation. State the actual collection cadence and operating window. Messages published after a collection snapshot wait for the next run. Laptop-off operation requires a separately running worker.

Check for a receipt before retrying publication. A delivered request awaiting a response is not a failed send. Bound retries, preserve errors, and stop the affected action on permission rejection or identity conflict. Keep authorized routine publishing within standing scope; ask for new approval only when the action requires it. Approval is never delivery evidence.

## Lessons from an early workflow

These generalized lessons inform the contract; they are not certification of a runtime implementation.

<details>
<summary>Read the early workflow lessons</summary>

| Failure encountered | Required behavior |
| --- | --- |
| A device appeared connected, but a reply could not reach the other session. | Use Git for both directions and verify stored records. |
| An update was published to an older recipient. | Resolve current stable recipient IDs and test routing after reassignment. |
| A sender wanted selected findings, but the receiver expected a general summary. | Preserve author-selected scope, order, and evidence. |
| A check ran before publication completed. | Report the observed commit and time; distinguish pending from absent. |
| Repeated approvals did not establish delivery. | Report the blocked operation and cause separately from publication status. |
| The sender could not tell whether anyone had retrieved the update. | Publish a receipt that the sender can independently read. |
| A receipt was described as though a person had read the work. | Label machine receipt, sender verification, and human review separately. |
| A completed session was expected to resume on its own. | Configure and verify a real trigger, or state that checking is manual. |

</details>

Use the [pilot checks](ADOPTION.md) to test these behaviors with independent sessions before expanding the team.

For provider selection and file or folder access research, see [enterprise deployment](ENTERPRISE.md).
