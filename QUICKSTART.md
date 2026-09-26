# Open, choose, hand off

**Start with Git access:** In Claude Code or another local agent, paste the [single onboarding prompt](CLAUDE-CODE.md). It checks the actual Git connection before building files. No Projects setup or browser launch is required. The HTML route below is optional.

Use [onboard.html](onboard.html) as the human entry point. It runs locally in a browser, with no build, server or external assets. Both managers and employees use the same file and choose their own path.

## Claude Projects

Create your project, connect the GitHub repository from Project knowledge and select the core plus one role pack. Follow [the Claude Projects guide](CLAUDE-PROJECTS.md) for the exact file list, sync and capacity handling. Opening a repository link is not a local clone and synced knowledge does not establish write access.

Download `onboard.html`, open it in your browser, complete the brief and copy its agent instructions into your project. Give the downloaded JSON to the agent if it can work with files. Authenticate through the provider's supported flow when needed.

## Local clone route

If your agent has permitted local filesystem and Git tools:

1. Clone or download the public framework.
2. Rename `WORKSPACE` to your knowledgebase name, such as `TEAM.KNOWLEDGE`.
3. Open `onboard.html`. Select **I'm setting up a team** and use that same folder name.
4. Give the brief and instructions to your agent. It prepares the local workspace with the included script, then follows the manager runbook.

The agent's local preparation command, from the clone root, is:

```sh
python3 scripts/bootstrap_workspace.py --workspace "TEAM.KNOWLEDGE" --config /path/to/aide-onboarding.json
```

Python 3.10+ is required; the bootstrap has no third-party dependencies. The JSON brief is optional for the script, but organization facts are still required for actual setup. The script creates missing files and preserves existing ones. It does not authenticate, run Git commands, create a remote or configure live agents.

## Employee route

The manager shares a private repository and a personal onboarding link. The employee opens `onboard.html`, selects **I'm joining a team**, and gives the brief to their own agent. Use the existing destination and assigned role. Do not bootstrap a second organization. The agent follows [employee onboarding](ONBOARDING.md), verifies actual access and completes the first message/receipt cycle with the manager's independent session.

## Keep work private and portable

The public framework's root ignore file excludes renamed first-level workspace folders. This reduces accidental staging; it is not an access-control or secret-scanning boundary. Verify the staged files and the remote before publishing. The agent prepares a separate private repository with the selected workspace contents at its root. Team records never belong in this public upstream.

The scaffold bundles its reference guides, templates and skills in `.aide-framework/`, plus the HTML guide at its root. A later private checkout therefore retains the procedures. Pin and verify the upstream revision during setup. Preserve the actual local snapshot hashes in `operations/framework-snapshot.json`.

The form creates a brief, not an account or verified deployment. Local preparation, remote publication, employee access, delivery and human acceptance have separate evidence. Draft storage is opt-in and local to this browser/path; download the brief for a portable handoff.
