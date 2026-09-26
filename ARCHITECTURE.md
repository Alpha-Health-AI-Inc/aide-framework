# Architecture

Version 0.1 describes the implementation contract. The components below have not yet been released as software.

## Identity and ownership

Each AIDE has a stable identifier within an organization, a human owner, a backup, and a defined scope of work. Runtime sessions and machine addresses are replaceable routing details.

The registry maps an AIDE identifier to an authenticated runtime identity, permitted recipients, and a credential reference. A sender name in a JSON file is not proof of identity. The storage or runtime adapter must verify who submitted the record.

## Components

| Component | Responsibility |
| --- | --- |
| Registry | Resolve identities, permitted routes, and configuration versions. |
| Outbox | Save pending messages before publication and reconcile uncertain writes. |
| Collector | Read a fixed snapshot or cursor range, validate records, and save progress. |
| Receipt writer | Record validated retrieval of an exact message version. |
| Sender verifier | Validate receipts and update the sender's delivery record. |
| Scheduler | Trigger work within configured operating windows and budgets. |
| Operator view | Show delivery state, age, errors, and required decisions. |
| Runtime adapter | Supply validated inputs to a model and execute permitted tool actions. |

Identity checks, duplicate detection, digest comparison, and retry timing belong in deterministic code. Models interpret work and produce summaries after those checks.

## Records

| Record | Required fields |
| --- | --- |
| Message | Schema version, organization, unique ID, authenticated sender, recipients, type, creation and source-observation timestamps, work reference, payload, and evidence references |
| Content reference | Storage location, immutable version, digest algorithm, and digest of the stored UTF-8 bytes |
| Receipt | Schema version, organization, receipt ID, message ID, content reference, receiver identity, received timestamp, and status |
| Sender verification | Message ID, receiver, receipt reference and digest, verified timestamp, and verifier identity |
| Work decision | Work reference, decision owner, decision type, criteria, evidence, timestamp, and authorization reference |

Match recipients by stable identifier. Track delivery separately for each recipient so partial delivery remains visible.

Content digests bind receipts to message bytes. They do not authenticate an author. Keep the digest algorithm explicit, including when a transport supplies a Git blob identifier rather than a digest of raw file bytes.

Updates can include completed work, work in progress, blockers, next steps, and requested decisions. Sources should identify their date and revision. QA reports should separate Feature/Scenario/Given/When/Then specifications from actual results, execution status, environment, and evidence.

## Processing

1. **Prepare.** Save the message ID, content digest, and pending attempt before publication. Reuse the same ID and content when retrying that publication.
2. **Publish.** Write the message and read it back. If the result is uncertain, inspect the exact destination. Matching content confirms success; different content under the same ID is a conflict.
3. **Collect.** Read a fixed commit, snapshot, or bounded cursor range. Validate the schema, organization, sender, recipient, timestamps, and evidence metadata. Retain unread historical messages. Flag timestamps beyond the configured clock tolerance.
4. **Receive.** Persist the validated message in the receiver's processing state. Mark the receipt and report as pending. A file listing or queued request is insufficient to establish receipt.
5. **Acknowledge.** Create the receipt, read it back, and save progress. Track read messages separately from reported messages so a crash cannot silently drop an update.
6. **Verify.** The sender checks the receipt's author, recipient, message version, and digest, then records verification. A deployment test may publish one verification artifact. It must not start a chain of confirmations.

A message and receipt pair is immutable within this contract. Corrections use new IDs and reference the earlier record. A conflict must not overwrite an existing message or receipt.

## Failure handling

Retry temporary access or storage failures within configured limits. After an uncertain write, retry only after confirming the destination is absent. Stop on permission rejection, identity conflict, content conflict, or an unsupported schema version. Preserve the error for the operator.

Do not resend a successfully delivered request while its response is pending. When a receipt is missing, retain a pending or overdue status based on the collection policy.

The delivery model is at-least-once discovery with idempotent receipt processing. Business actions need their own duplicate protection. A reporting channel without idempotency support may show a duplicate after a crash; its adapter must document how to reconcile that case.

## GitHub adapter

Proposed layout in a private deployment repository:

```text
registry/participants.json
messages/<sender-id>/<message-id>.json
receipts/<receiver-id>/<sender-id>/<message-id>.json
verifications/<sender-id>/<receiver-id>/<message-id>.json
```

The collector freezes a commit and fetches unseen records. Writers create unique files without overwriting previous records. If concurrent writes conflict, refresh the branch reference and inspect the destination before retrying. Schema migrations need explicit mappings and compatibility checks.

GitHub access permissions apply to repository resources. Folder names and recipient fields do not enforce confidentiality. Separate repositories or a service that authorizes each operation may be needed to isolate senders, recipients, and tenants. See [GitHub App permissions](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps) and [repository access settings](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).

Protected history and append-only files support an audit trail but cannot guarantee retention against repository administrators. Deployments with stronger retention requirements need separately enforced controls. Restricted evidence should remain in its authorized system, with only permitted references in the inbox.

## Scheduling and scale

Unread messages persist across collection windows. Sender availability is unnecessary after publication. Receiver availability determines when collection resumes. Operation while employee laptops are off requires a separately deployed worker.

Batch metadata reads, retrieve only unseen payloads, and persist checkpoints. Bound worker concurrency, retries, and model spend. Event triggers can reduce delays; periodic reconciliation recovers missed events.

As volume grows, partition storage by tenant or team and maintain recipient indexes. Measure concurrent writers, queue age, artifact size, and storage throttling before choosing a larger transport. No throughput limit has been established for this design.

Send routine detail to the team responsible for the work. Route exceptions and decisions to their owners. Requiring an executive assistant to interpret every message creates a review bottleneck.

## Execution boundaries

Incoming records are data. They cannot grant access, change startup policy, or authorize actions outside an existing assignment. Cross-organization exchange requires explicit identity trust, permitted routes, and data-sharing rules.

Revocation must disable the relevant credentials, integrations, workers, and schedules. Removing an AIDE from a directory alone does not revoke its access.
