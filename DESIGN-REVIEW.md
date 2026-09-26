# Design review: combine strengths, retain the evidence

[Readiness](READINESS.md) / [Runtime setup](RUNTIME-SETUP.md) / [Grow your team](GROW-YOUR-TEAM.md)

The framework draws from different working experiences. They are not successive, fully implemented versions of one system. A native multi-bot application can offer a useful team experience without Git exchange. A Git-coordinated deployment can have durable receipts while still struggling with activation. A portable specification can describe both without having implemented either runtime.

## What each experience contributes

| Source of experience | Strength to carry forward | What must not be inferred |
| --- | --- | --- |
| Native multi-bot setup | Easy profile creation, recognizable roles, visible team roster and convenient human interaction | Group replies do not prove Git publication, actual product connections, isolated permissions or automatic execution. |
| Git-coordinated AIDE work | Shared context, explicit recipients, versioned artifacts, exact-content receipts and recoverable state | A stored receipt does not prove sender verification, task completion, human acceptance or universal runtime compatibility. |
| Generalized framework | Human workspace first, Four Ps, employee-created specialists, provider-neutral contracts and lifecycle procedures | Documentation and examples are not an installed organization or a tested adapter. |

Borrow the useful experience, then prove it through the chosen deployment. Native chat may remain a convenient local interface; cross-session framework delivery still uses Git. Never label a native acknowledgement as a Git receipt.

## Gaps identified in the documentation review

| Finding | Documentation correction | Remaining implementation or test |
| --- | --- | --- |
| “Configure the bot” lacked an observable completion procedure | [Runtime setup](RUNTIME-SETUP.md) requires existing-profile reconciliation and saved-configuration read-back | Actual client-specific setup recipe and profile evidence |
| Runtime and product connectivity could be collapsed into one readiness label | Separate per-tool connection states and operation evidence | Authenticate and test each real connection |
| Role persistence depended on the reader understanding the startup convention | Require a fresh-session check with only the approved startup entry | Execute on the selected client/version |
| Distinct profile names could be mistaken for isolated environments | Inspect shared accounts, files, browser sessions and tool permissions | Verify the required access boundary with synthetic fixtures |
| Hosted execution, wake-up and laptop independence needed different probes | Separate environment, trigger and new-work-after-device-unavailable tests | Bounded authorized runtime tests and observed results |
| A roster needed reconciliation and partial-delivery reporting | Reuse matched profiles, create only missing approved roles, record one result per intended recipient | Verify the actual roster through Git, with native limits recorded separately |
| Runtime cost and stop controls were too implicit | Record actual billing evidence, operator, usage limits and stop/resume mechanism | Measured usage and tested operational controls |
| Startup receipt wording could imply the wrong hash for the manual profile | Align the startup template with the configured profile; manual v1 uses exact-byte SHA-256 | Deterministic validation and compatibility fixtures |

These corrections are documentation changes. No runtime behavior was made available merely by writing them.

## What to implement next

Use one actual client and one Git provider to complete a tested runtime recipe. Start with a manager's workspace, independently onboard an employee, let that employee build one approved specialist, and have another authorized requester use it from its published instructions. Preserve the same evidence distinctions through fresh sessions, device changes and operator handover.

The longer-term framework should combine a simple human-facing setup and capability catalog with deterministic identity checks, delivery state, duplicate protection and visible pending work. Those implementation items remain on the roadmap until they have code and acceptance evidence. The [readiness page](READINESS.md) is the source for the current shipped scope.
