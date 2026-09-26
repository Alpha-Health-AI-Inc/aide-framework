# Pilot guide

Start with one internal workflow whose outcome can be measured. Use two independent sessions, such as a QA assistant and a delivery assistant, with no mutual session access. They must obtain shared context and complete the handoff through GitHub alone.

This guide defines acceptance requirements for an implementation. It is not a record of completed tests.

## Establish the deployment

| Decision | Responsible role | Required output |
| --- | --- | --- |
| Workflow | Business sponsor | Scope, expected outcome, and baseline |
| Ownership | Workflow owner | AIDE roles, human owners, recipients, and backups |
| Access | Platform or security owner | Authenticated identities and enforced permissions |
| Records | Application owners | Systems that own work status, knowledge, and decisions |
| Execution | Runtime operator | Hosting, operating hours, recovery, and budgets |
| Data | Data owner | Permitted content, storage location, and retention |
| Acceptance | Sponsor and independent reviewer | Pass criteria and expansion decision |

Choose the identity provider, repository host, model vendor, and execution environment to fit the organization. Record these decisions before connecting live systems.

## Run the pilot

1. **Prepare shared context.** Create a private operational repository, choose the exact exchange branch, and complete the [startup entry point](START-HERE-TEMPLATE.md). Follow the [team layout](TEAM-WORKFLOW.md). Keep internal content out of public forks.
2. **Define the assignment.** Name the outcome, owner, recipients, allowed actions, and evidence requirements. Complete a [role contract](ROLE-TEMPLATE.md).
3. **Configure access.** Authenticate the runtimes and verify permitted and restricted routes with synthetic data. Set collection windows, retry limits, retention, and budgets.
4. **Test delivery.** Publish a unique message. Inspect its receipt and the sender's verification. Interrupt processing and confirm that it resumes without losing the update.
5. **Use a limited workload.** Track delays, duplicate records, manual intervention, report quality, and cost. Keep pending and rejected deliveries visible.
6. **Review the results.** Compare the evidence with the agreed criteria. The sponsor and independent reviewer decide whether to expand.

Two to five AIDEs and one workflow provide a manageable initial scope. Set service targets from the workflow's requirements and observed performance.

## Acceptance checks

| Scenario | Expected result |
| --- | --- |
| Fresh isolated session | Reads the approved startup entry point, identifies its role and context revision, and recovers pending delivery without another session’s history. |
| Different runtime | A second configured client completes publish, receipt, and verify through GitHub only; no vendor integration is assumed. |
| Deliberately scoped update | Selected findings and priority are preserved; unrelated chat content is excluded. |
| Team fan-out | Explicit recipient IDs and routing version are stored; partial receipts remain visible. |
| Recipient reassignment | New messages use current routing; old messages are not silently re-addressed. |
| Local or wrong-branch update | Is not reported as published to the configured exchange. |
| Check before publication | Shows the observed snapshot and pending state; a later run can discover the update. |
| Concurrent publishers | Unique records survive contention; uncertain writes are reconciled before retry. |
| Manual versus scheduled mode | No automatic wake-up is claimed without a verified trigger; the actual collection window is visible. |
| Correct recipient | Message, exact-content receipt, and sender verification agree. |
| Wrong recipient | The unintended AIDE does not issue a receipt; the operator can identify the routing error. |
| Duplicate discovery | Processing reuses the existing logical receipt and does not repeat work effects. |
| Same ID with different content | An integrity conflict is reported; the original record remains unchanged. |
| Crash after reading or writing a receipt | Recovery reconciles the stored records and preserves any pending report. |
| Sender offline after publication | The receiver can retrieve the shared update. |
| Collector offline | The message remains pending and is collected after recovery. |
| Access or approval rejected | The affected action stops with its actual cause recorded. |
| Instructions embedded in a message | The message cannot expand permissions or change the assignment. |
| Credential revoked | Actual storage and tool access are denied. |
| Separate tenant or restricted team | Unauthorized reads and writes fail at the access layer. |
| Human review pending | Delivery remains distinct from review and acceptance. |

## Measure performance

Measure publication-to-receipt latency and receipt-to-verification latency separately. Report wall time alongside the configured service window.

Also track the oldest pending message, recovery time, missed collection slots, conflicts, duplicate reports, manual interventions, summary corrections, cost per accepted handoff, and human time saved against the baseline.

Load tests should vary participant count, message volume, artifact size, and concurrent writers. Include unavailable workers and storage throttling. Use the results to decide when to partition storage, add workers, or change adapters.

## Build sequence

| Stage | Deliverable | Completion evidence |
| --- | --- | --- |
| Contract | Versioned schemas and synthetic fixtures | Valid and invalid records are classified consistently. |
| Exchange | Publish, collect, receipt, and verify operations | Duplicate and recovery checks pass. |
| Operations | Delivery-status view and clear errors | An operator can diagnose a missing or misrouted update. |
| Deployment | Identity, isolation, execution, and monitoring | Independent acceptance in the target environment. |
| Expansion | Additional adapters and load testing | Documented compatibility and operating limits. |
| Runtime release | Maintainers, dependency review, support, and security reporting | A tested distribution with a defined support scope. |

## Reassignment and offboarding

Transfer pending work and reassign recipients explicitly. The responsible operators revoke credentials, integrations, and schedules, then verify the result. Preserve required evidence under the retention policy and update the registry.

Archiving a conversation does not revoke system access.
