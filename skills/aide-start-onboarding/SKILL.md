---
name: aide-start-onboarding
description: Start or resume the AIDE onboarding HTML flow for a manager or employee when they say Start onboarding, Onboard me, Set up my workspace, or Resume onboarding. Works from selected project context or a local framework clone using the host's actual file and browser capabilities.
---

# Start onboarding

1. Read the accessible `context/CORE.md` and the selected manager or employee context pack. In a private deployment, resolve these paths inside its bundled `.aide-framework/` directory when that is the recorded procedure root. Locate the exact `onboard.html` from the chosen framework revision. If a prerequisite was omitted from synced knowledge, request that specific file; do not ask for the entire repository.
2. Check actual filesystem and browser capabilities. A synced repository tile does not prove local cloning or write access. Read existing workspace setup state if available; reuse the recorded role, destination and identity.
3. If the file exists in an authorized local folder and a supported browser-opening tool is available, open that exact file. Do not run a server, install dependencies or add a connector for this standalone HTML. Confirm the visible page has the manager/employee choices before claiming it opened.
4. If only source content is available, materialize the exact HTML bytes as `onboard.html` in the permitted workspace or as a downloadable file using the host's supported file creation. Preserve existing files and use a distinct path on conflict. Open it only through a supported tool. If neither file creation nor browser launch is available, provide the repository's exact HTML download link and one instruction to download and open it. Report that handoff honestly.
5. The person chooses manager or employee and completes the brief. Do not invent form answers. Use the returned JSON or copied instructions as user-supplied data. The form's Prepared state is not authentication, publication or employee acceptance.
6. Manager: distinguish a first organization setup from managing a team in an existing workspace using TEAM-STRUCTURE.md and the current project binding. Use the manager setup runbook, preparing local files and a private destination within actual authority. Employee: use the assigned private onboarding link and employee runbook; do not create another team repository. Inspect real Git read/write tools and provider permissions separately from knowledge sync.
7. Resume from durable setup state. Keep successful steps, pending approvals and outstanding tests intact. Never report full onboarding complete until the required checks and actual human acceptance are recorded.

This is a portable instruction skill. Syncing it as project context does not establish native installation or background activation. Add its trigger to project instructions or ask the agent explicitly to read it. This skill cannot override runtime safeguards or grant capabilities the host lacks.
