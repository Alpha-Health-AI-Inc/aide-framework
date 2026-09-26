# Connect Git before building the workspace

For a request to connect as an employee with a repository URL, follow [Employee start](EMPLOYEE-START.md). Treat it as an action request, check authentication/access before cloning, and do not ask the person to choose a documentation task or a credential architecture.

This is the first step for **Start onboarding** in every client. If no working folder is selected, guide the human through the client’s folder picker as the prerequisite; do not claim filesystem access from a screenshot. Complete one bounded connection check before collecting a roster or generating organization files. Use the local folder and permitted tools; a Claude Projects container, browser, HTML form and GitHub MCP are optional.

## 1. Inspect the current route

Read only the supplied task, selected folder and available tools. Preserve existing work. Check `git --version` when a shell is available. Inspect an existing checkout's status and destination without exposing embedded credentials. Never dump environment variables, credential files, tokens or full Git configuration.

Use one existing approved route:

| Route actually available | Check |
| --- | --- |
| GitHub CLI | Run `gh --version`, then `gh auth status --active --hostname <selected-host>`. Never use `--show-token`. Verify the authenticated login using `gh api user --jq .login` on github.com, or the appropriate selected-host equivalent. |
| GitHub MCP or provider connector | Discover actual tools in this session and make a scoped authenticated identity/read request. A connection badge or a connection in another client does not count. |
| Existing Git HTTPS/SSH authentication | Use the supplied private destination and a bounded `git ls-remote <clean-repository-url>` read. Record identity as unverified unless supported account evidence establishes it. Git author name/email is not authentication. |
| No working route | State the missing tool or login, and give one supported installation/sign-in action. Do not generate the organization's workspace or claim readiness to push. |

A public clone proves public read access only. Claude sign-in does not prove Git-provider authentication. GitHub CLI, MCP and Git transport credentials are separate; verify the route that will actually publish. A missing MCP server is not a reason to install one when the approved Git/CLI route already works.

If GitHub CLI is installed but signed out, guide the human through `gh auth login --hostname <selected-host> --web` using supported browser/device authentication and applicable host approval rules. Do not ask for a token in chat. Recheck once after the human completes authentication. Do not change global credentials, switch accounts or rewrite Git remotes silently. Missing software uses the organization's approved installation route, never an improvised download command.

## 2. Resolve the destination and role

Reuse facts already given. If missing, ask one compact question for the exact provider host, owner/namespace and whether the repository exists. The requested knowledgebase name is not enough to infer its owner. For example, a request for `TEAM.KNOWLEDGE` leaves the owner unresolved until confirmed.

Select the actual scope:

- **Organization administrator:** create the first private organization knowledgebase. This person may also be a team member or manager.
- **Team manager:** join the organization's existing knowledgebase, then prepare the assigned team area and personal onboarding links. Do not create another organization by default.
- **Employee:** join the supplied private repository using the personal handoff. Ask the employee about their own assignments later.

For an existing GitHub destination, use `gh repo view <owner/repo> --json nameWithOwner,url,isPrivate,defaultBranchRef,viewerPermission` or the equivalent connector operation. Use the actual returned branch; do not assume `master` or `main`. Record whether the repository is empty. A 404 or denied response is unresolved access/existence, not proof that a new repository should be created.

For a new destination, confirm the owner and requested private repository name. Authentication may pass while repository creation remains pending. Do not claim write access to a repository that does not yet exist. Prepare the minimal creation proposal, then create it within actual authorization. If the provider denies creation, stop that action and state the exact missing permission.

## 3. Report the check, then proceed

Return a brief, evidence-based status before substantial setup:

```text
Git tool: [observed version / unavailable]
Provider route: [actual CLI, connector or Git transport]
Authenticated account: [verified login / unverified / sign-in needed]
Destination: [exact owner/repo and branch / new private destination]
Read: [verified against private destination / not yet possible / blocked]
Write: [reported permission; actual publication unverified / verified after read-back]
Scope: [organization administrator / team manager / employee]
Next: [one concrete action]
```

If authentication or destination is unresolved, finish that connection step first. Public framework retrieval and preserving an existing local draft are allowed, but do not consume credits creating speculative roles and policies. After connection succeeds, follow only the relevant setup/onboarding runbook. For a new repository, actual publication stays pending until creation and an authorized write succeed.

## 4. Prepare, publish and verify

Keep the public framework and private deployment separate. Never change the public upstream remote into the organization destination. Inspect existing work before cloning, copying, staging or initializing Git. Reconcile any files produced by an earlier attempt; do not blindly trust generated identities, policies or invented responsibilities.

Prepare the smallest useful organization/team scaffold. Defer product assignments to each employee. Unknown meeting days, escalation targets, reporting lines and obligations remain pending. A listed name is not evidence that the person reports to the current user. Do not nominate a pilot employee without an explicit choice or existing approved handoff.

Use the approved Git publication route and branch review policy. A permission response or dry-run is not a successful write. Read the exact published commit and expected files back from the destination before reporting publication verified. Return the verified private repository URL and its published `JOIN.md` link as the first milestone. Do not wait for a full roster or employee assignments. State any access invitation still needed. Then prepare personal handoffs as memberships are confirmed. Keep counterpart tests pending until their actual session runs.

Save sanitized connection results in setup state or use [the Git connection record](templates/GIT-CONNECTION.json) at `operations/git-connection.json`. Record the chosen transport, observation time, evidence references and separate read/write status. No credential output or private machine paths belong in a shared record. Recheck on a new computer, account change or access failure; reuse current successful evidence in the same run.

## Avoid another setup loop

Do not reread the full repository. Do not reread generated context packs and their source runbooks. Do not require the HTML form; use supplied answers directly and ask only for missing essential facts. If the user wants HTML and a launch is rejected, stop that action, explain the cause and offer a manual file handoff. Do not try localhost servers, tunnels, alternate browser surfaces or repeated equivalent launches to bypass the rejection.

## Sources and limits

Command guidance checked September 26, 2026 against the official [GitHub authentication status](https://cli.github.com/manual/gh_auth_status), [authentication login](https://cli.github.com/manual/gh_auth_login) and [repository inspection](https://cli.github.com/manual/gh_repo_view) documentation. Use installed-tool help when the installed version differs. Other Git providers use their approved equivalent authentication/read/write checks. This guide is not an automatic connection service or a completed customer deployment test.
