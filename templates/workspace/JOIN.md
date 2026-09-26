# Join this workspace

Give your agent this private repository link and say:

> Start my onboarding in this existing workspace. Verify my Git connection,
> read START-HERE.md, and resolve my approved identity and team. Ask me about
> my assignments. Preserve existing work and publish only within my scope.

“Start employee onboarding” is an action request, not a request to design onboarding documentation. Use the supplied URL and selected working folder. Check sign-in and private access before cloning. If sign-in is missing, use the supported browser/device flow; do not ask the employee to choose keys or tokens.

The agent first reads `.aide-framework/GIT-FIRST.md`, `START-HERE.md`, the workspace configuration and relevant registry entries. Verify the person's approved membership and personal handoff if one already exists. Ask only for missing identity, team and scope facts. Do not assign a role merely because someone can read this file, and do not enroll an unapproved participant automatically.

If no approved membership or personal handoff exists yet, prepare the proposed record for the workspace owner and leave activation pending. Once resolved, follow `.aide-framework/ONBOARDING.md` for local setup, assigned context and the message/receipt test. Do not create a second organization or overwrite another person's files.

Repository access must be arranged through the Git provider separately. This link does not grant access, establish assignments or prove that onboarding has completed.
