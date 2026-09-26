# Recover an interrupted AIDE

[Lifecycle](LIFECYCLE.md) / [Device change](DEVICE-CHANGE.md) / [Exchange contract](EXCHANGE-CONTRACT.md)

First establish the exact repository, branch, identity, last confirmed operation and current tool access. Preserve local work and error evidence. Resume from observed records rather than repeating the whole setup.

| Situation | Inspect first | Safe next step |
| --- | --- | --- |
| New chat or lost context | Approved startup, role, continuity and remote records | Rebuild a concise context summary with sources; resume the first unresolved step. |
| Network failure while publishing | Exact intended path, ID and bytes on remote | Treat matching content as published; retry once only after confirmed absence and restored access. If still unreadable, leave uncertain. |
| Branch advanced or merge conflict | Current remote plus intended own diff | Reconcile without overwriting another contributor; honor review rules. No force push. |
| Message exists, receipt absent | Recipient, routing version and receiver availability | Leave delivery pending until an authorized receiver runs. Do not resend the message as new work. |
| Receipt exists, action incomplete | Receipt and requested action status | Delivery is complete; request progress only within authority. Receipt does not imply execution. |
| Crash after reading | Remote receipt and local receipt-pending state | Reuse a valid existing receipt or create the missing one after validation. |
| Crash after notifying a person | Output-channel evidence and report-pending state | Reconcile reporting separately. When unprovable, disclose uncertainty before a possible repeated summary. |
| Permission or approval rejection | Exact current rejection and requested action | Stop that action, name the owner and required decision; do not switch accounts or routes to bypass it. |
| Identity mismatch or same ID with different content | Registry, submission evidence and frozen records | Stop affected processing and preserve references for investigation. Do not overwrite the conflicting record. |
| Unavailable manager | Published updates and approved coverage | Continue authorized local work; keep receipt pending or use an explicitly authorized new forwarding route. |
| Repository unavailable | Provider status through supported tools and permitted backups | Keep writes uncertain until access returns or an approved migration is verified. |
| Restricted data accidentally published | Sanitized incident reference | Stop further sharing and involve the designated incident owner. A later deletion commit does not erase Git history or existing clones. |

## Lost or unavailable computer

1. Record the last verified checkpoint and what may exist only on the old computer. Do not claim unsynced work was restored from a clone.
2. Ask the responsible operator to establish whether the old publisher or worker can still run. For a lost or compromised device, the authorized security owner contains its sessions and credentials through actual provider/runtime controls. A registry edit is not containment.
3. Prepare a replacement checkout and restore authorized remote content and approved backups. Keep publication paused until the risk of competing writers is resolved. Record any unrecoverable files and unknown reporting progress.
4. Establish the new active session under the same approved role or an explicitly approved replacement identity. Authenticate through supported flows and verify product access separately.
5. Run the independent delivery and duplicate-receipt checks in [device change](DEVICE-CHANGE.md). Keep unresolved device containment and data loss visible in the final report.

## Backup and restore

The deployment owner must select permitted backup locations, retention, access and restore frequency before relying on this system for important work. This kit does not configure a backup service or promise a recovery time.

Back up the repository and necessary non-Git dependencies under that policy: approved attachments, large-file objects, referenced artifacts, permitted local recovery state and worker configuration. Keep secrets in approved credential management. Record which external sources are references only and how their continued availability is checked.

Test restoration into an isolated location. Compare an explicit inventory and content checksums, validate startup and identity mappings, and verify that old receipts and pending work remain usable. Do not activate a restored worker alongside the original. Document the last tested recovery point and any missing evidence. A local clone alone is not proof that every dependency is backed up.

## Avoid repeated side effects

Messages and receipts support reconciliation; they do not provide exactly-once execution in another system. Before repeating a product write, deployment or other consequential action after interruption, inspect that system's authoritative result and any supported idempotency record. If the outcome cannot be established, keep the action uncertain and involve its owner. Never infer “safe to repeat” merely from a missing chat reply.
