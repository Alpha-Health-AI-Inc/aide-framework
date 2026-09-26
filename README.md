<p align="center">
  <img src="assets/aide-framework-cover.svg" alt="Alpha Health AIDE Framework. Defined roles. Shared records. Confirmed delivery." width="100%">
</p>

<p align="center">
  <a href="ARCHITECTURE.md">Architecture</a> &nbsp; / &nbsp;
  <a href="ADOPTION.md">Pilot guide</a> &nbsp; / &nbsp;
  <a href="FORK-GUIDE.md">Fork and build</a> &nbsp; / &nbsp;
  <a href="LICENSE">MIT license</a>
</p>

# Alpha Health AIDE Framework

A reference design for AI assistants that coordinate work across teams. Each assistant has a defined role, a human owner, and a shared record of what it sent and received.

> **Project status:** Version 0.1 contains documentation and templates. The runtime and SDK are planned.

## A handoff you can verify

A QA assistant sends a report to a delivery assistant. The receiver reads it and writes a receipt tied to that exact report. The sender checks the receipt. A manager can then review the findings without first chasing confirmation that they arrived.

<img src="assets/delivery-flow.svg" alt="Three steps: publish the update, receive it and write a receipt, then verify the receipt. Human review remains separate." width="100%">

The records distinguish publication, receipt, sender verification, human review, and acceptance. Missing deliveries remain visible, and interrupted processing can resume from saved progress.

## Start with one workflow

**1. Define the role.** Name the owner, allowed actions, recipients, and evidence requirements using the [role template](ROLE-TEMPLATE.md).

**2. Build the exchange.** Follow the [architecture](ARCHITECTURE.md) for message identity, delivery receipts, duplicate handling, and recovery.

**3. Prove the handoff.** Run the [pilot checks](ADOPTION.md) before connecting a broader workload.

## Use your own systems

Choose your models, tools, identity provider, and execution environment. Keep business rules and operating hours in deployment configuration.

The first planned storage adapter uses a private GitHub repository. Other adapters can follow the same delivery contract. Operational messages and credentials stay in your deployment, separate from this public project.

A published update remains available when the sender goes offline. Collection still requires a running worker on a schedule or event trigger.

## Documentation

- [Architecture](ARCHITECTURE.md): components, records, processing, and access boundaries.
- [Pilot guide](ADOPTION.md): deployment decisions, acceptance checks, and scale measurements.
- [Role template](ROLE-TEMPLATE.md): a reusable operating contract for each assistant.
- [Fork guide](FORK-GUIDE.md): setup instructions and a brief for Claude or another implementation assistant.

## Roadmap

- Versioned schemas and synthetic fixtures.
- Publish, collect, receipt, and verify operations with persistent state.
- Recovery tests and an operator delivery-status view.
- Runtime integrations and measured deployment limits.

AIDE stands for **Ambient Intelligent Digital Employee**. Published by Alpha Health under the [MIT License](LICENSE).
