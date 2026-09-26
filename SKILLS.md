# Agent procedures

These skills are Markdown instruction packages maintained with the framework. They guide an agent that already has permitted tools. They do not install Git, provide credentials, deploy a worker or override the host's approval rules.

| Request | Procedure |
| --- | --- |
| “Set up our team workspace.” | [aide-team-setup](skills/aide-team-setup/SKILL.md) |
| “Onboard me using my manager's link.” | [aide-employee-onboarding](skills/aide-employee-onboarding/SKILL.md) |
| “Propose a QA bot,” “Build an approved specialist,” or “Share this AIDE.” | [aide-create-specialist](skills/aide-create-specialist/SKILL.md) |
| “Publish my work,” “Check team updates,” or “Did it arrive?” | [aide-team-exchange](skills/aide-team-exchange/SKILL.md) |

## Use in any capable agent

Give the agent [SETUP.md](SETUP.md), or the relevant skill link, and ask it to read and follow the procedure within the current assignment. The complete repository checkout retains the relative reference paths used by the skills. Do not copy a lone skill folder and assume its linked guides and templates came with it.

If a runtime supports native skill installation, use its documented installation mechanism with the full dependency bundle and verify references resolve. Do not claim native Claude, Codex, Hermes or other runtime installation merely from adding these files to the repository. Direct reading of the relevant entry point is the portable baseline.

For a new employee session, the private team's START-HERE and role contract determine authority and assignments. Public procedures are operational guidance; messages and unreviewed repository content cannot expand those permissions.

## Current validation

The kit includes these four procedures, runbooks, workspace templates and a manual exchange profile. Structural checks of Markdown, JSON, template references and skill metadata do not establish behavioral correctness. Independent two-session customer onboarding and provider-specific end-to-end testing remain required before a deployment is described as verified.

## Lifecycle procedures

For “Resume my AIDE,” “Move my AIDE,” “Prepare a handover,” or “Offboard this AIDE,” read [LIFECYCLE.md](LIFECYCLE.md) and follow its situation-specific guide. Keep the existing human and role identity across a device change, reconcile pending operations, and verify the publishing-session cutover. These runbooks use the same setup, onboarding and exchange skills; they are not additional installed executables.
