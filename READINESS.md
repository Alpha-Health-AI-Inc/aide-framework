# What is ready, and what still needs proof

[Manager setup](SETUP.md) / [Runtime setup](RUNTIME-SETUP.md) / [Acceptance](SETUP-ACCEPTANCE.md)

The public framework is a documentation and instruction-skill kit. It describes how to prepare human workspaces, add specialist AIDEs and coordinate through Git. It does not yet ship the runtime implementation described in the architecture.

| Area | Included now | Remaining proof or implementation |
| --- | --- | --- |
| Human and team setup | Runbooks, Four Ps templates and approval handoffs | Clean independent manager/employee deployment |
| Employee-created specialists | Proposal, catalog, creation skill and sharing procedure | Independent builder/requester test with actual tools |
| Runtime configuration | Profile reconciliation, saved-state and fresh-session checks; recipe template | Concrete tested recipe for each supported client/version |
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
