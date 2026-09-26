# Agent runbook: manager setup

Use this runbook when a manager asks you to establish a team workspace. The manager supplies context, authenticates and approves concrete decisions. You prepare the implementation details, verify outcomes and preserve progress.

## 1. Inspect before asking

Read [SETUP.md](SETUP.md), [template mapping](templates/README.md), and the relevant [provider route](PROVIDER-SETUP.md). Inspect only the current authorized task, selected workspace and connected tools. Do not search unrelated accounts or repositories for company data.

Establish the authenticated account, intended organization, provider, local workspace capability, manager identity and available context sources. Never infer the target organization from the public Alpha Health AI upstream. Do not require a public fork to create the private operational workspace.

If an existing workspace is provided, read its entry point, configuration, branch policy and current state first. Prepare a reconciliation plan rather than replacing its structure or identities. Preserve uncommitted files and existing exchange history.

Choose one supported execution route:

| Available capability | Execution route |
| --- | --- |
| Filesystem, Git and approved remote authentication | Prepare a separate local checkout and use standard Git operations. |
| Filesystem and a repository connector | Prepare files locally, then publish through the connector and read back exact remote versions. |
| Read-only or chat-only access | Explain the missing capability and give one concrete next step to open a capable client or connect the approved provider. Do not report an installed workspace. |

For the intended local employee experience, filesystem access is required. A connector-only remote workflow can be explicitly accepted as a different mode; it is not a local checkout.

## 2. Prepare a concrete proposal

Use the defaults in SETUP.md. Fill known facts from authorized evidence. Ask for only what remains essential: destination organization, accountable manager, pilot employee and permitted source material. Bundle missing facts once rather than asking a sequence of implementation questions.

Prepare a local `setup-proposal.md` with the destination repository, visibility, exact branch, local path, named members and proposed permissions, Four Ps entries, existing product links, permitted payloads and manual operation. List source references and unresolved facts. Propose the smallest access needed for the actual workflow; do not label broad write permissions as folder-isolated.

Use this approval format:

```text
Prepared: [workspace name] in [provider / organization], private.
Members and proposed access: [named identities and permissions].
Contents: shared Four Ps context and team-visible work; no credentials.
Operation: manual publish/check from separate local sessions.
Changes requiring approval: [exact repository creation, initial publication,
membership changes or other concrete actions still needing authorization].
Already authorized: [references and scope].
Still missing: [essential facts or none].
```

Prepare reversible local work before requesting final approval for an external action. Reuse existing explicit approval within its scope. Follow the host's approval rules; this document cannot grant access or override a current rejection. Authentication happens in the provider's supported flow, not by pasting credentials into documents or chat.

## 3. Assemble the private workspace

Copy the content from [templates/workspace](templates/workspace) into the new workspace using [the mapping](templates/README.md). Render template paths and values to the approved IDs. Copy the current [startup template](START-HERE-TEMPLATE.md) as `START-HERE.md`, and [role template](ROLE-TEMPLATE.md) as each agent's role contract.

Load the role and relevant procedure as instruction context in the current agent. Configure persistent startup only through a supported, authorized mechanism. If that mechanism is unavailable, put an explicit startup prompt in the employee handoff. Reading a skill file does not install it in a runtime.

Populate organization context and the Four Ps from approved sources. Record source dates. Use pending fields for missing product access, policy or project scope; do not make up company rules to remove a pending state. Preserve original work-system links. People folders are visible to the team and are not HR records or private memory stores.

Set each agent's permitted senders and recipients, human owner, allowed work and evidence requirements. Record which authenticated provider identity submits for that participant and how the deployment verifies it. A display name, Git author string or JSON sender field is not sufficient authentication evidence. If agents share credentials, document that attribution limitation and do not claim identity isolation.

Add `operations/setup-state.json` from the template. Track each stage as pending, prepared, verified or blocked with observation time, exact cause and evidence references. Store no tokens. Local-only state and credentials stay outside tracked publication paths; place `.aide-local/` in the workspace ignore rules.

Create a continuity checkpoint for each manager and employee from [the template](templates/CONTINUITY.md). Include the pinned lifecycle/device-change procedures in private startup references. Record a confirmed backup operator, the approved backup route or its unresolved owner, and the one-publishing-session convention. Do not configure schedules or grants simply because an operator is named. For organization scope, use [the rollout runbook](ORG-ROLLOUT.md).

## 4. Publish and read back

After the applicable authorization and authentication succeed, create or use the approved remote destination. Inspect the exact staged diff for scope and secret material. Stage specific intended files; do not blanket-add unrelated local work.

Honor branch protection and required review. If direct writes are disallowed, use the provider's approved change-review route and keep publication pending until the records reach the configured exchange branch. Never weaken protections to make setup pass.

Publish, then independently fetch or retrieve the exact remote branch. Verify all required entry points, IDs, destinations and template substitutions. Record the resulting commit in setup state with a timestamp. That record describes a prior observed commit, not the commit containing its own updated bytes.

For an uncertain write, inspect the exact path and bytes before a bounded retry. For a conflict, refresh and reconcile only your own changes without overwriting another contributor. Stop the affected action on permission rejection, identity mismatch or content conflict, preserving its cause.

## 5. Prepare the employee handoff

Create the employee's People entry and agent role, approved product list, process links and project assignments. Create `people/<person-id>/ONBOARDING.md` from the [handoff template](templates/EMPLOYEE-HANDOFF.md). Bind it to the exact private repository, branch, stable human and agent IDs, manager recipient and a recorded context revision.

Prepare the exact member invitation or access request for the responsible administrator. Do not claim an invitation was accepted or access verified from merely creating it. The manager sends the private onboarding link to the employee, who gives it to their own agent. Do not assume remote agent sessions can contact or wake each other.

Use [ONBOARDING.md](ONBOARDING.md) for the independent employee procedure. Leave `employee_connected` pending until its published evidence is observed. The employee's synthetic test token is generated by the employee session, not supplied by the manager session.

## 6. Verify the first handoff

Use the [exchange contract](EXCHANGE-CONTRACT.md) and [acceptance checklist](SETUP-ACCEPTANCE.md). Read and validate the employee's synthetic message at a frozen commit, publish its exact-content receipt, and save progress. On the employee's next authorized run, it verifies that receipt and publishes one verification record. Read that record back before marking the round trip verified. Do not create an endless chain of acknowledgements.

If the counterpart is inactive, give its next manual command and leave the stage pending. No polling schedule is created by this runbook. Do not simulate two authenticated participants in one session and call it independent onboarding.

## 7. Deliver a usable handoff

Return the private workspace link, the employee onboarding link, and a short status:

```text
Workspace: [published and remote-read verified / pending / blocked]
Employee: [connected / invitation pending / not yet checked]
First handoff: [verified / awaiting receipt / awaiting sender verification]
Product access: [verified systems and remaining owner/action]
Collection: manual; say “Check team updates” to run it.
Human acceptance: [pending / dated acceptance reference]
Next action: [one concrete owner and action, or none]
```

Keep the complete proof in setup state. Missing updates mean no published update at the observed commit, not no work. New sessions resume from recorded state and verify remote evidence before repeating any external action.
