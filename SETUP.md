# Set up your team

[Overview](README.md) / [Employee onboarding](ONBOARDING.md) / [Daily use](DAILY-USE.md)

Give your agent the link below. It prepares the workspace and explains what needs your approval. You authenticate with your Git provider and approve the proposed scope. You do not need to design a folder structure or write operating instructions.

```text
Set up our team's AIDE workspace using
https://github.com/Alpha-Health-AI-Inc/aide-framework/blob/main/SETUP.md
Follow the agent setup runbook. Prepare sensible defaults and the actual
files before asking me to approve publication or access changes.
Ask me only for missing organization facts, authentication, and decisions
that require my authority. Verify each completed step and tell me what
is still pending. Do not call setup complete until the stated checks pass.
```

> This is an agent-led documentation and skill kit, not an installer. It requires an agent with permitted filesystem and Git tools or equivalent repository APIs. The complete two-person experience has not yet been independently validated on a customer deployment. No authentication, access or automation is created by opening this link.

```mermaid
flowchart LR
  A["1. Agent prepares<br/>Workspace and defaults"] --> B["2. Manager approves<br/>Authenticates and confirms"]
  B --> C["3. Team verifies<br/>Employee handoff and receipt"]
```

## What you will be asked to do

| Your part | What the agent prepares |
| --- | --- |
| Confirm the organization and pilot team | A short setup proposal with the destination, owners and defaults filled in |
| Authenticate | The supported provider sign-in or credential-manager flow, without asking for secrets in chat |
| Approve publication and access when needed | Exact repository visibility, files, people, permissions and purpose |
| Confirm the first employee and their role | Their People entry, agent identity, product-access checklist and onboarding link |
| Accept the pilot result | Links to the published test message, receipt, sender verification and remaining gaps |

If the agent cannot infer a necessary fact, it asks one compact question. It should not invent your organization, employees, policies or product assignments.

## Recommended starting point

| Setting | Default proposal |
| --- | --- |
| Provider | Your existing approved Git provider; ask only if the destination is ambiguous |
| Workspace | A new private repository named `aide-workspace`, subject to availability and approval |
| Readers | Named pilot team members; everything committed is visible to all authorized team readers |
| Structure | People, Products, Processes and Projects, plus organization context and exchange records |
| Branch | One explicitly recorded exchange branch; propose `main` for a new dedicated workspace and honor existing branch policy |
| Participants | Manager and one employee, each with their own human and agent identity |
| Operation | Local working folders, deliberate publication and manual collection on request |
| Product access | Existing approved accounts; track requirements and verification separately from repository access |
| Infrastructure | No new paid service, background worker or schedule by default |
| Data | Synthetic delivery tests first; team-shareable work only after scope approval |

Read the [agent runbook](AGENT-SETUP.md) for the execution procedure. Start there automatically when the manager supplies this page. Use [templates](templates/README.md) to prepare the files and [skills](SKILLS.md) to load only the relevant procedure.

## What completion means

**Workspace prepared:** local files exist and have been reviewed. **Workspace published:** approved files are readable at the exact remote branch. **Employee connected:** the employee's independent session has read the workspace and verified its permitted access. **First handoff verified:** message, receiver receipt and sender verification all agree. **Pilot accepted:** the responsible human reviews the evidence.

The agent reports these states separately. A missing employee response remains pending; it is not a reason to repeat a delivered request or claim the employee is onboarded.

## Beyond the first team

This link starts a guided team pilot. For organization-wide preparation, follow [organization rollout](ORG-ROLLOUT.md). Each employee still authenticates and verifies their own onboarding. The agent prepares the structure and links; it cannot infer the whole company's roster or grant access from a manager's team-level approval.

Plan continuity at setup: assign an accountable owner and backup, pin the procedure version, and prepare a checkpoint for every manager and employee. [The lifecycle guide](LIFECYCLE.md) covers new sessions, computer changes, role transfers, pauses, departures, upgrades and retirement.

## Start with the human, then grow

The first manager can prepare their own workspace before another employee joins. Keep the independent counterpart test pending until a real authorized participant is available. The framework supports their growing scope through [new humans and specialist AIDEs](GROW-YOUR-TEAM.md).

Create a team-readable `aides/README.md` catalog. Employees can propose improvements, build approved specialists in their own instances and share them through that catalog. [Creating an AIDE](CREATE-AIDE.md) covers delegated ownership and approval; [using an existing AIDE](SHARED-AIDES.md) covers discovery and actual access. The manager directs scope while employees can own implementation and maintenance.

## What the agent must verify in your client

[Runtime setup](RUNTIME-SETUP.md) adds saved-profile read-back, fresh-session startup, actual Git and product-tool connections, and explicit availability checks. Existing bots are reconciled before creating new ones. [Readiness](READINESS.md) separates the included documentation from untested runtime behavior and missing implementation.
