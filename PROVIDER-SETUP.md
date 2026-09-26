# Choose the execution route

Start with [GIT-FIRST.md](GIT-FIRST.md). Confirm the route exists and authentication works before preparing the organization workspace. The absence of MCP does not block an already working approved Git/CLI route.

This guide tells the setup agent how to use the organization's existing Git environment. It does not install provider integrations or certify compatibility.

## Prefer what is already approved

Use the explicitly supplied provider, organization and repository. If missing, inspect the authorized current workspace and available connectors, then propose one destination. If several accounts could fit, ask the manager to select the actual organization. Do not infer a company account from the upstream publisher.

| Provider | Agent route |
| --- | --- |
| GitHub | Use an available authorized connector, Git client or supported provider tool. Follow repository membership and branch-review controls. |
| GitLab | Use an available authorized API/tool or Git client. Verify namespace, project membership and protected-branch behavior. |
| Bitbucket | Use an available authorized API/tool or Git client. Verify workspace/project destination and repository access. |
| Azure Repos | Use an available authorized API/tool or Git client. Verify organization, project, repository and its permission rules. |
| Self-hosted Git | Use the approved remote endpoint and SSH/HTTPS authentication. Have the responsible administrator provision a remote when repository creation is not available to the agent. |

Use the tool's current supported documentation for concrete API calls and authentication. The shared contract requires Git records, not a specific command-line application. Never invent CLI flags or ask the manager to choose an adapter architecture.

## Checks the agent performs

- Resolve the authenticated submitting identity and intended destination without printing secrets.
- Fetch the approved branch and read exact commit content.
- Prepare a synthetic unique file and publish via the allowed write/review route.
- Independently read back its exact path and bytes from the exchange branch.
- Verify the deployment's writer-attribution mechanism. Commit author text alone is self-declared; lack of authoritative identity evidence remains an explicit unmet gate.
- Confirm that employee access covers the shared records intended for the pilot. All pilot readers may read all committed team workspace content.
- Record the provider, tools and versions actually tested. Do not infer another provider's compatibility from one passing test.

An organization may require review before records enter the exchange branch. In that case, the work remains unpublished to the exchange until the required merge is complete. The agent prepares the change and names the actual remaining approval, without weakening the policy.

## If the environment is missing a capability

Prepare everything possible locally. Report the exact missing operation and the smallest next action: authenticate the selected provider, obtain the approved repository grant, or use a client with filesystem and Git access. Do not send the manager an open-ended implementation backlog.

Keep a pure documentation review, local file setup, remote publication, authenticated multi-participant delivery and unattended operation as distinct results.

Git access is one part of setup. Use [runtime setup](RUNTIME-SETUP.md) separately for saved profiles, role persistence, tools, shared resources and execution modes. A successful provider check does not establish that the agent will run unattended.
