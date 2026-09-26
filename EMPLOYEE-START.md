# Start employee onboarding

“Start employee onboarding” or “Connect me as an employee” plus a repository URL is an instruction to execute onboarding. Do not ask whether the person wants documentation, process design or help for a specific employee.

## Before cloning

1. Use the supplied repository URL. Check actual Git/provider authentication and read access using [GIT-FIRST.md](GIT-FIRST.md). Do not ask for a local repository path before inspecting the selected working folder. If no folder is available, request one folder selection, not a search across the computer.
2. If signed out, guide supported browser/device sign-in. Do not make a nontechnical employee choose SSH keys versus a personal access token. Reuse working approved authentication; do not silently switch accounts or change global credentials.
3. If signed in but the private repository is inaccessible, show the verified account and exact destination. Explain that the manager must grant that account access or the employee must accept the invitation/complete required organization authorization. A 404 is ambiguous; it is not proof of an SSH problem. Do not keep retrying clone while access remains unresolved.
4. Once access is confirmed, reuse a matching checkout or clone into a new folder inside the selected working directory. Preserve collisions and uncommitted work. Discover the actual branch from the destination; do not guess it.

## When cloning fails

Capture the actual command's sanitized error. Distinguish missing Git, authentication, repository access, transport/configuration, network and host-policy failures. If HTTPS reports an SSH error, inspect the narrow relevant URL rewrite/transport settings before diagnosing keys. Git's `url.<base>.insteadOf` can rewrite URLs; do not dump credentials or all config, or change global settings without appropriate authorization. Retry once only after a concrete cause has changed. A policy rejection stops the affected action.

Browser/device login is documented by [GitHub CLI](https://cli.github.com/manual/gh_auth_login); URL rewriting is documented in [Git configuration](https://git-scm.com/docs/git-config). These explain possible routes, not the cause of an error without its actual output.

## After connecting

Read the deployed root `JOIN.md`, `START-HERE.md`, `workspace.json` and relevant participant/team records. Use a supplied personal handoff if available. A path under `templates/workspace/` is source material, not a configured employee entry point. If only the public framework/template tree was copied, report “Manager setup incomplete” with the missing deployed paths. Do not make the employee build the organization's foundation.

Resolve approved membership, then ask one compact question only for missing personal details, team and current work. Never invent the employee's manager or assigned folder. Continue [ONBOARDING.md](ONBOARDING.md). Authentication, membership, local setup, publication and delivery remain separate checks.

## What the employee should hear

Start: “I'll connect to your team's repository, prepare your local workspace and load your onboarding instructions. I'll ask you to sign in if needed.”

Access blocker: “You're signed in as [verified account], but I cannot read [repository]. Ask the workspace owner to grant this account access, or accept the pending invitation. I'll resume from here once access is available.”

Ready: “Your local workspace is ready at [path]. Your team is [verified team], your assigned work folder is [path], and [verified state or next action].”

Do not report a connected or ready employee while an essential gate remains unresolved.

## Manager handoff

Include an explicit employee instruction with the private URL, not just a bare link. Before private instructions can be read, the new agent needs enough direction to authenticate. Use `scripts/make_employee_handoff.py` against the configured deployment to prepare the copyable message. It checks local entry paths and destination consistency; the manager agent must separately verify those same files at the remote commit. It does not grant access or certify onboarding.

Updates to public upstream do not automatically update existing private deployments. Reconcile the selected procedure changes into each private workspace, preserve its local instructions and identities, then verify remote publication before telling employees they have the fix.
