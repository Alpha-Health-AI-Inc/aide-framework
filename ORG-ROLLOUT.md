# From one manager to the organization

[Manager setup](SETUP.md) / [Lifecycle](LIFECYCLE.md) / [Enterprise controls](ENTERPRISE.md) / [Acceptance](SETUP-ACCEPTANCE.md)

A manager can give the setup link to a capable agent to prepare a scoped team workspace. That does not automatically enroll the whole company. Organization-wide use requires approved ownership, membership, permitted data and independent access checks for the people who will use it.

```mermaid
flowchart LR
  A["One team<br/>Prove the handoff"] --> B["More teams<br/>Prove routing and recovery"]
  B --> C["Organization<br/>Approve measured rollout"]
```

## What the agent prepares

| Stage | Agent work | Human or operator decision | Exit evidence |
| --- | --- | --- | --- |
| Organization foundation | Inventory existing approved workspace, prepare organization context and Four Ps, owner and backup roles, registry, version and data boundary | Confirm actual authority, source scope and destination | Approved plan and remote-read verified files |
| Manager and first employee | Prepare private onboarding links, verify separate identities and local workspaces | Authenticate and approve exact access when needed | Independent message, receipt and sender verification |
| Lifecycle pilot | Exercise a new session, device move, interrupted write, manager handover and offboarding with synthetic records | Accept results and named gaps | Dated evidence from the lifecycle matrix |
| Additional teams | Reuse organization context; add only confirmed membership, team routes and assigned Products, Processes and Projects | Approve each access boundary and accountable owner | Team-specific verified onboarding, routes and access |
| Operational rollout | Prepare observability, backup, support, version and change procedures; propose automation only if requested | Approve operating model, limits and infrastructure | Measured acceptance for the selected providers and runtimes |

The agent fills in implementation details and bundles missing business facts into a short request. It must not invent the employee roster, reporting lines, policies or access authority. A manager's team authorization does not grant company administration rights.

## Shared context without duplicate organizations

Start from the existing approved organization workspace when one exists. Reference common organization and product records; place team-specific context under the established team entries. Do not have each manager blindly initialize a second organization or overwrite a shared registry.

Everything in the default repository is visible to its authorized readers. If teams require different confidentiality boundaries, prepare separate repositories or another verified access design before adding their data. Personal folders organize work; they do not hide it. Provider review requirements may also mean that publication waits for an approved merge.

## How employees join at scale

The manager's agent prepares a confirmed roster and a personal onboarding link for each person. Actual account invitations and permissions use the organization's approved mechanism. Each employee independently authenticates, reads their assigned context and runs the delivery test. Track prepared, invited, connected, delivery verified and human accepted separately. Do not mark an entire roster onboarded because their folders exist.

For manager replacement or departures, use [lifecycle handover](LIFECYCLE.md#role-and-manager-handover) so pending work has an owner. Assign a backup operator who can restore continuity through authorized access without sharing the original manager's credentials.

## What must be measured

Record tested team size, repository volume, collection duration, oldest unreceived message, publication conflicts, duplicate-processing attempts, recovery time, provider limits and operating cost where available. Pick acceptable thresholds with the responsible operator and owner. Do not invent capacity claims from a successful two-person demonstration.

Manual collection requires an active session. Organization-wide unattended operation needs an implemented, monitored executor, supported authentication, bounded retries and tested handover. The documentation provides the contract; it does not ship or automatically deploy that service.

## Current readiness

The public kit contains guides, instruction skills and templates. Structural validation is not an end-to-end deployment. A new organization should begin with a clearly labeled pilot, then use [acceptance evidence](SETUP-ACCEPTANCE.md) to decide whether to expand. No universal bot compatibility, unattended operation or enterprise readiness is claimed.

## Let employees build shared capabilities

Managers establish direction and approve scope. Employees can identify gaps, propose specialists, implement approved packages and maintain them in a discoverable team catalog. Use [growing the team](GROW-YOUR-TEAM.md) and [creating an AIDE](CREATE-AIDE.md) to delegate this work rather than routing every implementation task through the manager. Add specialist-instance onboarding and independent requester acceptance to each team's rollout evidence.

## Multiple teams and roles

Follow [team structure](TEAM-STRUCTURE.md) for nested managers and people who participate in several teams. Onboarding applies to the selected organization, workspace and team, not to an entire machine. Reuse the person's verified identity within an organization and create a separate scoped membership for each team. A manager of an existing team joins its private deployment; they do not bootstrap another organization. Use the [two-machine pilot](TWO-MACHINE-PILOT.md) to verify these routes.
