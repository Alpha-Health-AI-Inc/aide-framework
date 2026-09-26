# Employee onboarding

For a request to connect as an employee with a repository URL, follow [Employee start](EMPLOYEE-START.md). Treat it as an action request, check authentication/access before cloning, and do not ask the person to choose a documentation task or a credential architecture.

**First action:** run the [Git connection check](GIT-FIRST.md) against the supplied private destination. No Claude Projects container or HTML form is required. Use the personal handoff and confirmed identity, then ask the employee about missing assignments. Do not create a second organization.

[Manager setup](SETUP.md) / [Daily use](DAILY-USE.md) / [Acceptance checks](SETUP-ACCEPTANCE.md)

The manager gives the employee a private `people/<person-id>/ONBOARDING.md` link and arranges repository access. The employee gives that link to their agent:

```text
Onboard me using this team link: <private onboarding link>.
Read the approved startup instructions, prepare my local workspace,
check my role and product access, and complete the first delivery test.
Ask me to authenticate or approve only when needed. Preserve existing work.
```

```mermaid
flowchart LR
  A["1. Get connected<br/>Read context and authenticate"] --> B["2. Publish a test<br/>From the employee workspace"]
  B --> C["3. Verify delivery<br/>Read the manager receipt"]
```

## Use the visual guide

Open [onboard.html](onboard.html) and choose **I’m joining a team**. Use the private repository, branch and onboarding link your manager provided. For Claude Projects, select the core and employee context packs using [this guide](CLAUDE-PROJECTS.md). Knowledge sync alone does not create a local checkout or prove publication access.

## Procedure for the employee's agent

1. **Resolve the destination.** Read the handoff, approved `START-HERE.md`, deployment configuration and registry from the exact branch. Verify the assigned human and agent IDs and the manager recipient. If the authenticated identity conflicts, stop that action and report the cause. Do not create a new identity to bypass a mismatch.
2. **Prepare local work.** Choose a new folder or inspect the provided checkout. Confirm its remote and branch, preserve uncommitted work, fetch current approved content, and make the employee's `people/<person-id>/work/` available. Do not reset or overwrite another checkout. The folder becomes shared when selected changes are pushed.
3. **Learn the Four Ps.** Read the assigned People entry, Products, Processes and Projects. Confirm sources and revisions. Summarize the role and current assignment in plain language. Ask for missing work scope rather than inventing tasks.
4. **Check access.** Confirm remote read and permitted publication capability with synthetic content. Separately inspect product access requirements. Use permitted read-only checks where available, and record not checked, requested, granted or verified working. Prepare any missing access request for the named owner. Do not copy credentials into Git.
5. **Publish onboarding evidence.** Save `people/<person-id>/onboarding-status.md` with the observed context revision, assigned IDs, local workspace status, product access gaps and pending decisions. Publish only sanitized evidence. Read it back from the remote branch.
6. **Test delivery.** Generate one unique synthetic token locally, create an addressed test message using [the exchange contract](EXCHANGE-CONTRACT.md), publish it and read it back. Tell the employee that the manager agent must next run “Check team updates.” The token is delivery-test data, never a credential.
7. **Verify the receipt.** On a later authorized check, read the matching manager receipt, validate its exact message reference and submitting identity, and publish one sender verification. Preserve all three artifact references. Do not resend a successful test while waiting.
8. **Report readiness.** Mark the employee connected only after identity, startup and permitted Git read/write checks pass. Mark delivery verified only after the three artifacts agree. Product access and human acceptance retain their own states.

## The employee's everyday experience

Work locally with the agent. Say “Publish these findings to my manager” when ready. Later say “Check whether my update arrived.” There is no automatic sharing of private chat history. The default shared folder is team-visible after publication.

If onboarding is interrupted, inspect `operations/setup-state.json`, the person's onboarding status, and existing remote messages and receipts. Resume the first incomplete stage instead of re-creating accounts, folders or successful tests.

## Keep your AIDE when the session or computer changes

Create your shared continuity checkpoint from [this template](templates/CONTINUITY.md) after onboarding. Record your stable identity, current assignment, source revisions and pending work. Update it at meaningful handoffs and before leaving a session with unfinished work. Keep private chat and credentials out of it.

A new session reads the checkpoint and reconciles remote records. For a new computer or agent client, use [device change](DEVICE-CHANGE.md). A fresh clone restores published work; unpublished files, local reporting state and attachments need their own verified recovery path. [The lifecycle guide](LIFECYCLE.md) also covers role changes and departures.

## Discover and create capabilities

Read your team's `aides/README.md` during onboarding. Your agent can explain existing QA, Product or other specialists, their approved use and their availability. Follow [shared AIDEs](SHARED-AIDES.md) to use one.

If a useful capability is missing, ask your agent to [prepare a proposal](CREATE-AIDE.md). After the manager's required approval, you can build it in your authorized instance, publish the reusable package and verify it with a colleague. You may own its maintenance; the manager does not need to operate it for you.

Before marking your AIDE connected, use [runtime setup](RUNTIME-SETUP.md) to read back saved settings where supported and verify startup in a fresh session. Existing profile names do not prove access, persistence or isolation. Keep manual startup and missing product connections visible.

## Multiple teams and roles

Follow [team structure](TEAM-STRUCTURE.md) for nested managers and people who participate in several teams. Onboarding applies to the selected organization, workspace and team, not to an entire machine. Reuse the person's verified identity within an organization and create a separate scoped membership for each team. A manager of an existing team joins its private deployment; they do not bootstrap another organization. Use the [two-machine pilot](TWO-MACHINE-PILOT.md) to verify these routes.
