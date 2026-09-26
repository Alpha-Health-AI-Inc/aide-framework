# Architecture and delivery contract

Proposed design, not an implemented or certified protocol · Draft 0.1

## Separate the core from each deployment

The core owns validation, stable identifiers, delivery state transitions, duplicate handling and auditable evidence links. Adapters own model execution, tool access, scheduling, storage and user interfaces. Deployment configuration owns organizational roles, credentials, approvals, data classification, reporting cadence, retention and cost limits.

A registry maps a stable organization/agent identity to its human owner, active runtime binding, permitted routes and credential reference. A session or machine ID is a replaceable routing attribute. Published registry claims must be bound to authenticated principals by the deployment, rather than accepted solely because a JSON file names a sender.

## Components to build

| Component | Deterministic responsibility |
| --- | --- |
| Registry validator | Validate active identities, authorized routes and configuration version |
| Outbox | Persist a pending publication before submission; reconcile uncertain writes |
| Collector | Read a fixed snapshot or bounded cursor range, validate messages, and checkpoint processing |
| Receipt writer | Create one receipt per recipient/message/content version after validated retrieval |
| Sender verifier | Check receipt identity and content binding, update sender delivery records |
| Scheduler integration | Trigger bounded work inside deployment-defined windows and budgets |
| Operator store/view | Surface published, received, verified, overdue, rejected and failed states |
| Runtime adapter | Provide validated data to a model and execute only authorized tool actions |

Do not spend model calls deciding whether a known message ID was already processed, whether a receipt hash matches, or whether a retry deadline elapsed. These are deterministic checks. Models interpret work and draft summaries after validation.

## Proposed portable records

These fields describe a future contract. They do not silently replace the existing prototype's schema.

| Record | Required information |
| --- | --- |
| Message | Schema version; organization; unique message ID; authenticated sender binding; intended recipients; type; creation/source-observation timestamps; correlation/work reference; payload and evidence references |
| Stored-message reference | Storage location; immutable version; digest algorithm and digest of the exact stored UTF-8 bytes |
| Receipt | Schema version; organization; unique receipt ID; message ID and stored-message reference; receiving agent/principal; received timestamp; `received` status |
| Sender verification | Message ID; receiver; exact receipt reference/digest; verified timestamp; verifier identity |
| Work decision | Work reference; reviewer/approver identity; decision type; criteria; evidence; timestamp; applicable authorization reference |

Recipient matching is exact; similar display names are not equivalent identities. For multiple recipients, delivery is tracked independently per recipient. The interface must distinguish partial receipt from all-required-recipients receipt.

Published business payloads may include completed work, work in progress, blockers, next steps, requested decisions and source evidence. QA payloads use Feature/Scenario/Given/When/Then, with actual results, execution status, environment, revision and evidence recorded separately. A written scenario is not a passed test.

Content digests bind receipts to exact bytes; they do not authenticate the sender. Authentication requires the adapter's trusted principal or a validated signing identity. Algorithm identifiers remain explicit; a Git blob identifier must not be labeled as a SHA-256 digest of the raw message bytes.

## Processing and recovery rules

1. Persist the intended publication ID, exact content digest and delivery attempt before sending. A retry reuses this identity; it does not create a duplicate business message.
2. After an uncertain write, read the exact destination. Matching bytes mean the write succeeded. Conflicting bytes under the same ID are an integrity failure. Only a confirmed absence plus a transient failure permits a bounded retry.
3. A collector reads a fixed commit or snapshot, validates schema, organization, authenticated sender, recipient, timestamps and evidence metadata, and rejects unsupported versions. Future timestamps beyond configured clock tolerance are flagged; historical messages are not discarded because they are old.
4. Record the message as read and pending receipt/report. Create the receipt only after validated retrieval into the receiving AIDE's durable processing state. A storage listing, HTTP success or queued runtime request alone is insufficient.
5. Read back the receipt and commit the receipt/report checkpoints. Separate last-read and last-reported state so an interruption does not lose an unreported update.
6. Sender verification checks the exact recipient, message version/digest and receipt author identity. Persist the verified state. Initial deployment acceptance may publish one confirmation artifact for the receiver to inspect; verification artifacts do not generate recursive confirmation requests.
7. Retry transient reachability/storage failures within configured limits. Stop on permission rejection, identity conflict, integrity conflict or unsupported schema; surface the actual cause. A pending successful request is not resent.

Expected delivery model: at-least-once discovery with idempotent receipt processing. Exactly-once business effects are not promised. Any future action executor must separately deduplicate its effects and provide recovery evidence. Reporting into a channel without idempotency support can still produce a duplicate after a crash; expose and reconcile that limitation rather than claim guaranteed exactly-once reporting.

## GitHub reference adapter

Illustrative layout in a dedicated private deployment repository:

```text
registry/participants.json
messages/<sender-id>/<message-id>.json
receipts/<receiver-id>/<sender-id>/<message-id>.json
verifications/<sender-id>/<receiver-id>/<message-id>.json
```

This is a proposed neutral layout. An adapter for the existing prototype can map its current paths without rewriting historical messages. The collector freezes a commit, compares unseen IDs and blobs, and creates unique receipt files without overwrite. On concurrent-write conflict it refreshes the ref and checks the exact file before a bounded retry. Migration between schema versions requires explicit mapping and conformance checks.

GitHub's app permissions operate at repository/resource scopes. Folder names and JSON recipient fields must not be treated as confidentiality or write-access controls. Use a deployment boundary consistent with the actual repository permissions; unrelated tenants must not share a broadly readable inbox repository. A mediated writer or separate repositories may be needed to enforce sender and recipient isolation. See [GitHub App permissions](https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps) and [installation repository access](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps).

Append-only files and protected history provide an audit convention, not guaranteed immutable retention against administrators. If a customer requires stronger retention guarantees, the deployment needs separately enforced storage/audit controls. Keep sensitive evidence in its authorized system and exchange only permitted references and minimal summaries.

## Scheduling, availability and cost

Persist unread work across collection windows. A sender can go offline after durable publication; a collector can still read the published record. An offline collector leaves delivery pending. Availability with employee laptops off requires a separately deployed and tested worker; GitHub storage alone does not supply execution.

Batch metadata reads per snapshot, use durable checkpoints, retrieve only unseen payloads, and bound concurrency and model budgets. Polling and event triggers are adapter choices. Event triggers reduce waiting only if an authorized worker exists; periodic reconciliation is still needed to recover missed events. Do not promise instant delivery from the existence of a webhook.

## Scale and trust boundaries

Start with one exchange boundary and a small roster. At larger volumes, partition by tenant/team, maintain recipient indexes, apply backpressure, and move receipt/query workloads to an appropriate service while retaining the portable contract. A single Git branch and repeated full-history scans require measurement before broad rollout; no capacity limit or throughput claim has been established.

Route routine detail to the relevant team AIDE, with exceptions and decisions going to the responsible human. Requiring one executive AIDE to interpret every message creates a review bottleneck. Federation across organizations needs explicit identity trust, allowed routes and data-sharing rules; matching identifiers alone is insufficient.

Inputs remain untrusted data. An update cannot add permissions, change startup policy or order tool execution outside an existing work contract. Revocation must disable the actual credential/runtime/scheduler routes, not merely hide an agent from a directory.
