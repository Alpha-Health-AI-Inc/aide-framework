# Fork guide

Fork this repository to adapt the design and templates for your organization. Version 0.1 contains documentation; implementation starts in your fork. Internal team context and operational records belong in a separate private deployment repository.

## Setup

1. [Create a fork](https://github.com/Alpha-Health-AI-Inc/aide-framework/fork) in an organization you control.
2. Read the [overview](README.md), [team workflow](TEAM-WORKFLOW.md), [architecture](ARCHITECTURE.md), and [pilot guide](ADOPTION.md).
3. Choose one workflow and complete its [role contract](ROLE-TEMPLATE.md).
4. Keep credentials, internal policies, deployment identities, and operational messages outside the public repository. Use synthetic data in examples and tests.
5. Preserve the [MIT license](LICENSE) notice in copies or substantial portions of the project. Identify your version as a derivative of the Alpha Health AIDE Framework.

## Implementation brief for Claude

Copy this brief into Claude or another implementation assistant:

```text
Use https://github.com/Alpha-Health-AI-Inc/aide-framework as the upstream design.
Read README.md, TEAM-WORKFLOW.md, START-HERE-TEMPLATE.md, ARCHITECTURE.md,
ADOPTION.md, ROLE-TEMPLATE.md, and FORK-GUIDE.md.
The repository contains documentation, not a working runtime.

Our team uses independent Claude, Codex, Hermes, or other sessions. They
cannot access each other. GitHub must carry all cross-session context,
requests, replies, updates, receipts, and sender verification. Do not require
direct messaging, remote session discovery, or a shared vendor account.

Prepare a private operational repository layout and startup entry point
with reviewed team/project context, stable identities, roles, sender folders,
and explicit recipient routing. Keep internal data out of the public fork.
Verify each configured client’s actual GitHub access. Begin with a manual
publish/check workflow; do not claim autonomous operation without a tested
worker or trigger.

Prepare a pilot plan and implementation backlog for one internal workflow.
Identify the human owner, recipients, allowed actions, evidence requirements,
and acceptance criteria. Establish our identity, hosting, model, and GitHub
configuration from available requirements. Flag unresolved choices explicitly.

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

Start with the shared context and manual workflow in TEAM-WORKFLOW.md. Build schemas and synthetic fixtures, then the GitHub adapter with a persistent outbox and collector. Verify restart recovery, duplicates, content conflicts, and wrong recipients before adding model execution.

Add role configuration and a delivery-status view. Complete access-isolation checks and independent pilot acceptance before expanding to other workflows or adapters.
