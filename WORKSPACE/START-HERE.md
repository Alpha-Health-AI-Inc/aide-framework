# Build this workspace

The name of this folder is the proposed knowledgebase name. It is not evidence of the legal organization, authenticated account, participant identities or approved scope.

## First setup

1. If this folder is still named `WORKSPACE`, have the user choose its name. Rename it before adding organization information. If it already has a distinct name, keep it.
2. In the parent framework clone, run `python3 scripts/bootstrap_workspace.py --workspace "<this-folder-name>"` using the supported Python 3.10+ command. This prepares files locally and preserves existing content. It does not authenticate or publish.
3. Read `.aide-framework/AGENT-SETUP.md`, `.aide-framework/SETUP.md` and `.aide-framework/SKILLS.md`. Follow them within the user's assignment. Prepare the manager's workspace first; no employee is required to begin.
4. Use authorized sources to populate organization context, People, Products, Processes and Projects. Prepare approved roles and the AIDE catalog. Use the CI documentation skill for maintained references. Ask one compact question for essential missing facts; do not invent a company roster or policy.
5. Prepare the exact private Git Service destination and initial publication for the user's approval if not already authorized. Authentication happens through supported provider tools, never secrets in chat. Publish this folder's contents as the private deployment repository root, not the public framework clone. Preserve local originals and inspect both source and destination before moving or copying files.
6. Verify remote read-back, actual tools, identities and an independent message/receipt exchange using the bundled acceptance guide. Keep missing counterpart checks pending. Record outcomes in `operations/setup-state.json`.
7. Replace this starter with a filled entry point derived from `.aide-framework/START-HERE-TEMPLATE.md`, preserving the current state and local procedure links. Configure startup loading through the actual runtime's supported mechanism and verify it in a new session.

## Resume or move computers

If `workspace.json` and setup state already exist, read them first. Preserve work and identities. Use `.aide-framework/LIFECYCLE.md` and `.aide-framework/DEVICE-CHANGE.md` for recovery. Do not recreate a remote repository, resend outstanding requests or repeat a successful grant because a new session started.

The initial starter is intentionally small. The agent builds and verifies the organization-specific workspace; the local scaffold alone is not a working multi-agent deployment.
