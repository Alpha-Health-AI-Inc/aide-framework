# Start in Claude Projects

This is an optional context-reading route. For local setup and publication, [Claude Code onboarding](CLAUDE-CODE.md) checks actual Git access first and does not require Projects. Sync is not a provider write connection.

[Openable HTML guide](onboard.html) / [Manager setup](SETUP.md) / [Employee onboarding](ONBOARDING.md)

Create a project in Claude Desktop or the web app. Choose a name such as your organization's knowledgebase name, then provide that name explicitly in the onboarding brief or project instructions. A project label is not automatically model context.

## Select a small starting set

In Project knowledge, choose **+**, then **GitHub**. Select an accessible repository or paste its URL, choose the branch and select files. Start with:

| Person | Select from this framework |
| --- | --- |
| Manager setting up a team | `context/CORE.md`, `context/MANAGER.md`, `skills/aide-start-onboarding/SKILL.md`, `onboard.html` |
| Employee joining a team | `context/CORE.md`, `context/EMPLOYEE.md`, `skills/aide-start-onboarding/SKILL.md`, `onboard.html` |

These role packs are generated from the canonical runbooks. Do not select the original runbooks as well unless you need a section missing from the pack. Add the relevant private workspace entry point, assigned People/role records and current work only after permitted access is available.

Open a downloaded copy of `onboard.html` to prepare the brief, or ask the agent to guide the same questions. Include the HTML source when you want the agent to launch or materialize the flow from synced context. If you open it manually, omit it from Project knowledge to save capacity. GitHub's normal file view displays its source; download the file and open it in a browser to use the form.

## Say “Start onboarding”

After sync, enter **Start onboarding** in the project. In a capable Cowork session, the agent can inspect its available file tools and use the launch procedure. In a chat-only session, it may need to provide a downloadable file or link. Either route ends with the same HTML form, which generates the brief the agent uses to continue. The launch path must be verified in the actual client; it has not been certified by a synced repository tile.

## Manage capacity

The Git Service stores the complete authorized knowledgebase. Project knowledge is the selected working context for a person or task, not a mirror of every file.

1. Begin with the core, one role pack and the launcher skill. Add the HTML for agent-led launch. The generated `context/manifest.json` reports file sizes and word counts, not Claude's token quota.
2. Add only relevant current product, process and project references. Keep a small context index pointing to sources that can be loaded when needed.
3. If the UI reports a capacity problem, remove unrelated histories, generated duplicates, screenshots, large exports, logs and source trees from the selected sync set. Keep authoritative originals in Git.
4. Use **Configure files** to adjust selection and **Sync** to refresh it. Recheck after material changes; the guide does not promise push delivery or background synchronization.
5. Ask Claude to identify the files it can actually read, their recorded versions and missing material. A pasted link is not proof that content was downloaded or synced.

Do not hardcode a universal capacity percentage or token maximum. Plan, model, file processing and project features affect capacity; use the actual UI and account documentation. Paid Projects may use retrieval mode as knowledge grows, but this does not remove every ingestion or file-size constraint.

## Separate reading from execution

The GitHub knowledge integration documents selection and synchronization of repository file contents. It is not evidence that the session can create a local folder, write to Git, install a skill, grant access or launch an agent. Check the actual available tools.

- With permitted filesystem and Git write tools, the agent can prepare files and use the normal publication procedure.
- With knowledge access and file generation only, the agent can produce a reviewed file bundle and exact publication instructions. A permitted tool or human performs the write; remote read-back and receipts remain pending until verified.
- With read-only chat, the agent prepares the plan and names the missing execution capability. It must not report setup complete.

For employees, the manager provides the private repository and onboarding link. The employee uses their own project and permitted account. Syncing is not invitation acceptance or successful onboarding. Existing approvals apply within scope, and current provider restrictions remain in force.

## Project instructions to paste

```text
Use the AIDE core and my selected manager or employee pack for this project.
When I say Start onboarding, follow aide-start-onboarding and open onboard.html
using available tools, or give me its downloadable file if launch is unavailable.
My workspace name, organization, role and scope are in my onboarding brief.
Read accessible sources before acting. Name files you cannot access.
Use the Git Service for shared context, updates and exact-content receipts.
Verify my identity, recipients, branch and actual tool capabilities.
Prepare concrete changes; ask for missing facts, authentication or still-required
approval. Do not infer Git write access from knowledge sync. Preserve existing
work and pending requests. Keep local, published, received and accepted states
separate. Retrieve only context relevant to my task and identify stale evidence.
```

## Source and verification

Procedure checked against Anthropic's documentation on September 26, 2026: [GitHub integration](https://support.claude.com/en/articles/10167454-use-the-github-integration), [project management](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects), [Cowork projects](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork), and [file uploads and limits](https://support.claude.com/en/articles/8241126-upload-files-to-claude). This is documentation-backed guidance, not a completed test in an organization's signed-in Claude account. Menu wording may change.
