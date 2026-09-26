# AIDE Framework entry point

For onboarding, read `GIT-FIRST.md` first and verify the actual Git/provider route before generating organization files. Resolve administrator, team-manager or employee scope from supplied facts. Existing-team managers and employees join their private deployment; only first-organization setup uses the starter-folder bootstrap. The HTML form and Projects sync are optional. Do not invent assignments, reporting lines, schedules or policies.

For a request to build an organization's workspace from this clone:

- Look for the user-selected first-level folder containing `.aide-workspace.json`. If several exist, ask which one to use. If only `WORKSPACE` exists, obtain the intended name and rename it before organization work.
- Read that folder's `START-HERE.md`, then use `scripts/bootstrap_workspace.py` and the manager setup runbook. Build local files before asking for final approval of external changes.
- Treat the folder name as a workspace display name. Verify the destination account, organization, human owner and scope separately.
- Keep organization work in its selected folder, and publish its contents only to the approved private destination. Do not push organization records to this public upstream.
- Reconcile existing files and setup evidence before repeating actions. Do not invent identities, approvals, source facts or working integrations.

For work on the framework itself, preserve provider-neutral terminology and synthetic examples. The shared coordination layer is called the Git Service. Read the relevant guide and tests for the area being changed.

These instructions are a portable entry point, not a claim that every runtime auto-loads this filename. A user can explicitly ask any capable agent to read the selected workspace's START-HERE.md.
