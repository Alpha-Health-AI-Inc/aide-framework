# AIDE transition record

<!-- Render to operations/transitions/<unique-transition-id>.md. Use one record per transition. -->

- Transition ID and kind: <device change, client change, recovery, role handover, pause, offboarding, upgrade or retirement>
- Status: <prepared / awaiting approval / in progress / verified / blocked / accepted>
- Organization and affected stable IDs: <confirmed IDs>
- Accountable human and operator: <confirmed owners>
- Reason: <routine operational description; no private personnel details>
- Requested at / last observed at: <UTC timestamps>
- Authorization: <actual scoped reference and unresolved decisions>

## Before and after

| Item | Before | Proposed or verified after |
| --- | --- | --- |
| Publishing session | <label and observed state> | <label and observed state> |
| Role, manager and route | <IDs and routing version> | <IDs and routing version> |
| Repository, branch and profile | <exact references> | <exact references> |
| Framework/client procedures | <pinned version> | <pinned version> |
| Actual access and triggers | <operator evidence> | <verified change or pending> |

## Checklist and evidence

- [ ] Inventory published, unpublished and ignored work, attachments and pending exchanges.
- [ ] Verify approved backup or record unrecoverable items.
- [ ] Read back published checkpoint at <commit>.
- [ ] Reconcile in-flight writes and uncertain external effects.
- [ ] Observe old publisher stopped or authorized containment completed.
- [ ] Verify destination identity, current role and permitted access.
- [ ] Restore work; compare content and attachment checksums.
- [ ] Reconcile delivery, read and reported state; identify unknowns.
- [ ] Publish approved cutover and routing change; retain historical mappings.
- [ ] Verify synthetic round trip and reuse of an existing receipt, or explain why not applicable to retirement.
- [ ] Confirm new work owners, product-access gaps and operator responsibilities.
- [ ] Record human acceptance with an explicit dated source.

- Evidence: <exact artifact paths, commits, observations and actual actor>
- Cutover commit/time: <observed boundary>
- Remaining gaps: <owner and next action>
- Recovery or rollback plan: <reviewed steps preserving existing history>
- Retention/cleanup decision: <policy and actual authorization; no implied deletion>

An unchecked or unverified item remains pending. Never fill evidence with a planned action or treat this document as technical access enforcement.
