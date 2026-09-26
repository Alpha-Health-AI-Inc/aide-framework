<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/aide-framework-cover-dark.svg">
    <img src="assets/aide-framework-cover.svg" alt="AIDE Framework. Humans and agents. One shared Git workspace." width="100%">
  </picture>
</p>

<p align="center">
  <a href="SETUP.md">Set up your team</a> &nbsp; / &nbsp;
  <a href="VISUAL-GUIDE.md">Visual tour</a> &nbsp; / &nbsp;
  <a href="TEAM-WORKFLOW.md">Team workflow</a> &nbsp; / &nbsp;
  <a href="ARCHITECTURE.md">Architecture</a> &nbsp; / &nbsp;
  <a href="ADOPTION.md">Pilot guide</a> &nbsp; / &nbsp;
  <a href="FORK-GUIDE.md">Fork and build</a>
</p>

# AIDE Framework

A shared Git workspace for humans and AI agents to communicate, learn the project context, and hand work to one another. People can contribute directly or through Claude, Codex, Hermes, or another assistant. Everyone uses the same durable records, explicit recipients, and delivery receipts.

**Git is the team’s coordination layer.** No session needs access to another session or a direct chat connection. Context, requests, replies, updates, and receipts all travel through the repository. Each participant has a stable identity and a defined scope. Agent identities also name their accountable human owner.

**Choose your Git provider:** GitHub, GitLab, Bitbucket, Azure Repos, or self-hosted Git. The contract is provider-neutral; adapters and enterprise controls must be implemented and verified for each deployment.

> **Project status:** Version 0.1 contains agent-led runbooks, five instruction skills, workspace templates and a manual record profile. It is not an installer or a verified enterprise runtime. Independent two-session deployment acceptance is still required.

## Start with your agent

Give Claude or another capable agent the [manager setup link](SETUP.md) and say, “Set up our team workspace using this guide.” The agent prepares the files, defaults and verification steps. You supply missing organization facts, authenticate and approve concrete changes. [Employee onboarding](ONBOARDING.md) and [daily use](DAILY-USE.md) continue the same flow.

## Grow from a human workspace

The manager starts with their own scope and shared context. Employees build their workspaces and can propose specialist AIDEs as new needs emerge. With the required approval, an employee can build a capability in their own instance, publish it in the team catalog and maintain it for colleagues. [Grow your team](GROW-YOUR-TEAM.md) explains adding humans, creating specialists and reusing shared AIDEs.

## Keep the AIDE, change the computer

The [lifecycle guide](LIFECYCLE.md) covers joining, daily work, new sessions, device changes, role handovers and retirement. Use [device change](DEVICE-CHANGE.md) to restore context and pending work without creating a new identity. Use [organization rollout](ORG-ROLLOUT.md) to expand a proven team pilot.

## The Four Ps

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/workspace-map-dark.svg">
  <img src="assets/workspace-map.svg" alt="The Four Ps: People for who does the work, Products for what the team builds and uses, Processes for how work gets done, and Projects for what is being delivered." width="100%">
</picture>
</p>

**People. Products. Processes. Projects.** Who does the work, what they build and use, how they work, and what they are delivering. Organization-wide context sits alongside these four sections. [Explore the workspace](TEAM-WORKFLOW.md#the-four-ps-a-workspace-people-can-navigate).

## A handoff you can verify

A QA assistant sends a report to a delivery assistant. The receiver reads it and writes a receipt tied to that exact report. The sender checks the receipt. A manager can then review the findings without first chasing confirmation that they arrived.

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/delivery-flow-dark.svg">
  <img src="assets/delivery-flow.svg" alt="Three steps: publish the update, receive it and write a receipt, then verify the receipt. Human review remains separate." width="100%">
</picture>
</p>

The records distinguish publication, receipt, sender verification, human review, and acceptance. Missing deliveries remain visible, and interrupted processing can resume from saved progress.

## Start with one workflow

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pilot-path-dark.svg">
  <img src="assets/pilot-path.svg" alt="Pilot stages: prepare private context; connect and test access; prove publication, receipt and verification; review recovery, quality and human acceptance." width="100%">
</picture>
</p>

**1. Establish the shared workspace.** Follow the [team workflow](TEAM-WORKFLOW.md) to organize the Four Ps, shared organization context, and delivery records in a private repository. Use the [startup template](START-HERE-TEMPLATE.md) to bring a new session up to speed.

**2. Connect independent sessions.** Define each [role](ROLE-TEMPLATE.md), verify its permitted Git access, and use the [architecture](ARCHITECTURE.md) for publishing, receipts, and recovery.

**3. Prove the handoff.** Run the [pilot checks](ADOPTION.md) with two isolated sessions. Verify publication, receipt, and sender confirmation using Git alone.

## Use your own systems

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/fork-boundary-dark.svg">
  <img src="assets/fork-boundary.svg" alt="Public upstream contains reusable design. A public fork contains adaptations and synthetic examples. A separate private deployment holds organization context and operational records." width="100%">
</picture>
</p>

Choose your models, tools, identity provider, and execution environment. The exchange uses a shared Git repository on your chosen provider. Each tool’s configured access must be tested; this project does not ship vendor integrations. Keep business rules and operating hours in deployment configuration.

Operational messages stay in your private deployment, separate from this public project. Credentials stay in approved credential storage.

A published update remains available when the sender goes offline. Collection requires an active session or worker. Manual checks work; automatic collection needs a configured and tested trigger.

## Enterprise deployment

The [enterprise investigation](ENTERPRISE.md) covers human and agent access, private deployment options, and Drive-like file and folder permissions. Granular access is a research and implementation goal. Folder names, recipient fields, and review rules do not provide confidential file access.

## Readiness

See [what is included and what still needs proof](READINESS.md) and [the design review](DESIGN-REVIEW.md). The next implementation gate is a concrete runtime recipe and an independent manager, employee and specialist workflow using actual tools.

## Documentation

For implementation, begin with [manager setup](SETUP.md), [agent procedures](SKILLS.md), and [workspace templates](templates/README.md).

Start with the [visual tour](VISUAL-GUIDE.md) for a short illustrated walkthrough.

- [CI Source documentation](CI-DOCUMENTATION.md): a documentation skill, evidence-aware template and human/machine generator.
- [Team workflow](TEAM-WORKFLOW.md): shared context, team routing, daily use, and delivery lessons.
- [Startup template](START-HERE-TEMPLATE.md): an entry point for independent sessions.
- [Architecture](ARCHITECTURE.md): components, records, processing, and access boundaries.
- [Pilot guide](ADOPTION.md): deployment decisions, acceptance checks, and scale measurements.
- [Role template](ROLE-TEMPLATE.md): a reusable operating contract for each assistant.
- [Fork guide](FORK-GUIDE.md): setup instructions and a brief for Claude or another implementation assistant.
- [Enterprise investigation](ENTERPRISE.md): access boundaries, provider adapters, and deployment acceptance.
- [Branding](BRANDING.md): visual conventions and adapting the identity for your fork.

## Roadmap

- Machine-validated schemas and automated synthetic fixtures for the manual record profile.
- Provider adapters and enterprise access-control research.
- Publish, collect, receipt, and verify operations with persistent state.
- Recovery tests and an operator delivery-status view.
- Runtime integrations and measured deployment limits.

AIDE stands for **Ambient Intelligent Digital Employee**. Originally published by Alpha Health AI. [MIT License](LICENSE).
