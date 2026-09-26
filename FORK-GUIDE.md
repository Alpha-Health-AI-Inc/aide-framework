# Fork guide

Fork this repository to adapt the design and templates for your organization. Version 0.1 contains documentation; implementation starts in your fork. Internal team context and operational records belong in a separate private deployment repository.

## Setup

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/fork-boundary-dark.svg">
  <img src="assets/fork-boundary.svg" alt="Public upstream contains reusable design. A public fork contains adaptations and synthetic examples. A separate private deployment holds organization context and operational records." width="100%">
</picture>
</p>

1. [Fork the upstream project on GitHub](https://github.com/Alpha-Health-AI-Inc/aide-framework/fork), or import a copy into your chosen Git provider. Keep the upstream reference and license notice.
2. Read the [overview](README.md), [team workflow](TEAM-WORKFLOW.md), [architecture](ARCHITECTURE.md), and [pilot guide](ADOPTION.md).
3. Choose one workflow and complete its [role contract](ROLE-TEMPLATE.md).
4. Keep credentials, internal policies, deployment identities, and operational messages outside the public repository. Use synthetic data in examples and tests.
5. Preserve the [MIT license](LICENSE) notice in copies or substantial portions of the project. Use your own project name, organization identity, and visual theme. See [branding your fork](BRANDING.md).

## Implementation brief for Claude

Copy this brief into Claude or another implementation assistant:

```text
Use https://github.com/Alpha-Health-AI-Inc/aide-framework as the upstream design.
Read README.md, TEAM-WORKFLOW.md, START-HERE-TEMPLATE.md, ARCHITECTURE.md,
ADOPTION.md, ROLE-TEMPLATE.md, ENTERPRISE.md, and FORK-GUIDE.md.
The repository contains documentation, not a working runtime.

Our team includes human contributors and independent Claude, Codex, Hermes,
or other agent sessions. Humans must also be able to read and publish records.
These sessions cannot access each other. Our chosen Git provider must carry
all cross-session context,
requests, replies, updates, receipts, and sender verification. Do not require
direct messaging, remote session discovery, or a shared vendor account.

Prepare a private operational repository layout and startup entry point
with the Four Ps: People, Products, Processes and Projects. Keep shared
organization context alongside them. Include product owners, source links,
environments and access instructions; verify product access separately.
Use stable identities, roles, sender folders,
and explicit recipient routing. Keep internal data out of the public fork.
Verify each configured client’s actual Git access. Begin with a manual
publish/check workflow; do not claim autonomous operation without a tested
worker or trigger.

Prepare a pilot plan and implementation backlog for one internal workflow.
Identify the human owner, recipients, allowed actions, evidence requirements,
and acceptance criteria. Establish our identity, hosting, model, and Git
configuration from available requirements. Flag unresolved choices explicitly.

Investigate file and folder authorization for enterprise use. Do not claim
Drive-like access control from folder names, CODEOWNERS or sparse checkout.
Compare separate repositories with a mediated service that has no raw-access
bypass. Document tested provider capabilities and unresolved restrictions.

Implement in our fork only when authorized. Begin with versioned schemas,
synthetic fixtures, and deterministic publish, collect, receipt, and verify
operations. Preserve stable identities, exact-content receipts, persistent
recovery state, scoped access, and separate human acceptance.

Use the acceptance scenarios in ADOPTION.md. Report which checks passed,
which failed, and what remains unimplemented. Keep organization data and
credentials private. Obtain the applicable authorization before connecting
live systems, granting access, or creating infrastructure.
```

## First implementation

Start with the shared context and manual workflow in TEAM-WORKFLOW.md. Build schemas and synthetic fixtures, then the Git adapter with a persistent outbox and collector. Verify restart recovery, duplicates, content conflicts, and wrong recipients before adding model execution.

Add role configuration and a delivery-status view. Complete access-isolation checks and independent pilot acceptance before expanding to other workflows or adapters.
