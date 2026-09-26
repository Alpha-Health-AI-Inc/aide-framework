# Find and use a shared AIDE

[Create an AIDE](CREATE-AIDE.md) / [Grow your team](GROW-YOUR-TEAM.md) / [Daily use](DAILY-USE.md)

Use `aides/README.md` as the private team's capability catalog. All authorized repository readers can discover its entries. An entry explains how the capability is used; it does not distribute credentials or automatically create running instances.

## Two ways to share

| Mode | What is shared | How a colleague uses it | Identity and availability |
| --- | --- | --- | --- |
| Reusable definition | Reviewed instructions, templates, dependencies and tests | Reads the pinned package and configures an approved instance with their own permitted tools | New durable instances receive their own registered participant IDs. Each user's runtime and access are verified separately. |
| Shared instance | One registered specialist with an operator and an addressed Git request route | Publishes a request to its participant ID; collects its reply and evidence | The operator's instance must run to collect and execute. No direct access to its session or credentials is needed. |

A capability may support both modes, but each must have its own instructions and evidence. A temporary helper running entirely inside a user's permitted session can return its result to that parent session; the parent publishes under its own identity with honest attribution. Temporary spawning depends on the host runtime. It does not automatically make the helper a durable shared AIDE.

## “Give me access to the QA AIDE”

1. Read the catalog entry and approved audience. Check whether the team member already has permission to use the capability. Do not ask for approval again when the existing scope covers the request.
2. Resolve the execution mode. For a shared instance, verify the requester and destination IDs and update permitted routes only if authorized and necessary. For a local instance, follow the package's supported setup and verify its own tools and attribution.
3. Prepare any missing access request for the actual system owner. Catalog visibility, permission to submit work, runtime activation and product access are separate states.
4. Publish one allowed synthetic request and verify the complete result path. Return the catalog link, request example, availability and evidence. Keep access or runtime gaps pending.

The team's approved default can permit all team members to submit work to a specialist. This does not mean they all receive the specialist's privileged product access. The specialist validates each request against its role, requester, permitted source scope and approved output audience; it must not use broader credentials to retrieve or disclose information that requester is not authorized to receive.

## The request and result loop

```mermaid
sequenceDiagram
  participant E as Employee's agent
  participant G as Shared Git repository
  participant Q as Specialist AIDE
  E->>G: Publish addressed request and evidence
  Q->>G: Read request during an authorized run
  Q->>G: Publish receipt, then result reply
  E->>G: Read reply and verify its source
  Note over E,Q: Human reviews the result; receipt is delivery only
```

Use `type: request` with an explicit registered recipient, requested output and immutable evidence references. A result uses `type: reply`, a new message ID and `in_reply_to` pointing to the original request. Include the capability version and actual execution evidence in the payload. Use [the existing exchange contract](EXCHANGE-CONTRACT.md) without inventing incompatible record types.

If the specialist is asleep, stopped or unavailable, the published request remains queued. Report the last observation and named operator; do not create repeated copies of the request. If it has receipted the request but no result exists, report work pending. Do not claim that Git starts the agent or supplies an execution scheduler.

## Example: employee-created QA capability

An employee notices repeated release checks and proposes a QA specialist. The manager approves synthetic and staging-only checks, a team-wide request audience and a named operator. The employee builds the package, verifies it with a colleague, and publishes it to `aides/release-qa/`.

Another employee finds the catalog entry and submits an allowed request through Git. The QA instance reads it when running, publishes findings and execution evidence, and the requester collects the reply. Production access, release approval and independent-review claims remain governed by their separate actual authorizations.

This is an illustrative workflow, not a shipped QA bot. The framework provides the creation, sharing and acceptance procedure.
