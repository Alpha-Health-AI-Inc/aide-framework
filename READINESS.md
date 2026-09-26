# What is ready, and what still needs proof

[Manager setup](SETUP.md) / [Runtime setup](RUNTIME-SETUP.md) / [Acceptance](SETUP-ACCEPTANCE.md)

The public framework is a documentation and instruction-skill kit with an offline onboarding brief, local workspace scaffold and CI Source validator and generator. It describes how to prepare human workspaces, add specialist AIDEs and coordinate through Git. It does not yet ship the runtime implementation described in the architecture.

| Area | Included now | Remaining proof or implementation |
| --- | --- | --- |
| Human and team setup | Offline HTML guide, local scaffold, runbooks, Four Ps templates and approval handoffs | Clean independent manager/employee deployment |
| Nested teams and multiple roles | Membership/context templates, manager paths and two-machine pilot | Actual identity, routing, hierarchy and context-switch acceptance |
| Claude Code / Git-first setup | Concise CLAUDE.md, account/destination preflight and local prompt route | Actual signed-in customer authentication, publication and two-machine handoff |
| Claude Projects | Selective core/role packs and capacity guidance from official docs | Signed-in customer account sync and actual write-capability checks |
| Employee-created specialists | Proposal, catalog, creation skill and sharing procedure | Independent builder/requester test with actual tools |
| Runtime configuration | Profile reconciliation, saved-state and fresh-session checks; recipe template | Concrete tested recipe for each supported client/version |
| CI Source documentation | Schema, generation skill, Markdown/JSONL outputs, local hash checks and regression tests | Real-source semantic review, freshness triggers and retrieval evaluation |
| Git exchange | Message/receipt conventions and recovery procedure | Deterministic validator, durable processing and provider acceptance |
| Product integrations | Access inventory and per-operation checks | Actual authorized authentication and tests for each deployment |
| Isolation | Explicit repository and runtime-boundary guidance | Verified enforcement for the selected accounts/environments |
| Availability | Separate execution, trigger and computer-unavailable test plans | Actual monitored executor and bounded tests where claimed |
| Lifecycle | Device moves, handover, offboarding, backup and migration runbooks | Recorded execution of the lifecycle matrix |
| Operations and cost | Named owners, pending states and measurement requirements | Operating dashboard, tested alerts and actual cost evidence |

Published Markdown, template checks and skill metadata checks establish documentation structure only. They do not establish that an arbitrary bot can deploy this system or that every Git provider is supported by a tested adapter.

## Sources of the design

The [design review](DESIGN-REVIEW.md) separates native bot-team experience, Git-coordinated AIDE operations and the generalized contract. Evidence from one does not certify the others.

## Next acceptance sequence

1. Select one actual client/version and Git provider. Complete the runtime recipe from supported tools and verify profile persistence and access.
2. Use separate manager and employee sessions to complete setup, message, receipt and sender verification.
3. Let the employee build one approved specialist, and let a colleague use it entirely through the published package and Git route.
4. Exercise a new session, computer move, duplicate observation and operator handover with preserved work.
5. Only if unattended operation is intended, verify its real trigger, new work while the user's computer is unavailable, stop/recovery controls and cost limits.

Keep results in the private deployment with sanitized reusable compatibility evidence when separately authorized for publication. Do not copy operational records or account details into the public framework. Expand to more runtimes, providers and teams after the relevant gates pass.

## September 26 onboarding verification

Local scaffold regression tests pass for preparation, preservation on resume, invalid brief rejection, existing-team rejection and path boundaries. Context packs are checked against their source runbooks. The standalone HTML passes JavaScript syntax checks. Interactive browser acceptance remains pending: the authoring environment's browser policy blocked local-file opening. No alternate route was used to bypass that restriction. Follow [the two-machine pilot](TWO-MACHINE-PILOT.md) in a permitted customer environment before claiming the Start onboarding journey works there.
