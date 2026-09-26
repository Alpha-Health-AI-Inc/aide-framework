# Enterprise deployment and access

[Overview](README.md) / [Visual tour](VISUAL-GUIDE.md) / [Architecture](ARCHITECTURE.md) / [Pilot guide](ADOPTION.md)

**Status: investigation and implementation plan.** AIDE is a collaboration contract for humans and bots using shared Git records. It ships agent instruction skills, setup runbooks and templates. It does not currently ship a runtime, a human-facing submission app, provider adapters, or file and folder authorization.

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/enterprise-access-dark.svg">
  <img src="assets/enterprise-access.svg" alt="Humans and agents use authenticated access enforcement before retrieving shared or restricted Git records. Provider controls and a proposed gateway are alternatives to investigate, not released features." width="100%">
</picture>
</p>

## Any Git provider, one record contract

An organization chooses GitHub, GitLab, Bitbucket, Azure Repos, or self-hosted Git. The shared records remain ordinary versioned files. The current upstream happens to live on GitHub; that does not make GitHub a deployment dependency.

Each provider adapter must demonstrate authenticated publication, exact-version read-back, immutable message IDs, receipts, sender verification, recovery after interruption, and conflict handling. Authentication, API pagination, branch rules, webhooks, rate limits and hosting differ by provider. A provider name in this guide is a target option, not a verified integration.

## Humans are participants too

People can read context, publish requests and updates, receive replies, and confirm retrieval through a Git client or a provider editor. Agents use the same contract through permitted tools. Human-to-human, human-to-agent and agent-to-agent exchanges all retain author identity and source evidence.

Record the human author, submitting agent or service, and any on-behalf-of scope separately. Only an explicit human review record can establish human review. A future form-based interface should make correct records easy to create without hiding publication failures or pending delivery.

## Investigating Drive-like permissions

The desired experience is familiar: share a workspace, limit a folder or file to named people and agents, and remove access when a role changes. Treat this as an authorization problem, not a folder-naming convention.

The baseline uses repositories whose contents may be seen by every authorized reader. If a team cannot share all those records, separate the access boundary before publishing sensitive work. The logical workspace may span several repositories.

| Approach | What to investigate | What it does not establish |
| --- | --- | --- |
| Separate private repositories | Team membership, service identities, cross-repository routing and allowed context sharing | Per-file isolation within an otherwise readable repository |
| Provider-native controls | Exact read, write, review and administrative permissions for the chosen edition | Uniform capabilities across providers |
| Mediated file service, proposed | Check identity and path policy on every operation; audit access; deny raw repository access to restricted clients | Confidentiality if a client can bypass it through clone, APIs, raw objects, refs, search or artifacts |
| Restricted evidence kept elsewhere | Publish only authorized references and require access in the source system | Permission to copy the restricted payload into shared Git history |

Write approval and read confidentiality are distinct. CODEOWNERS or branch review rules may govern changes; do not infer that they hide files. Sparse checkout selects working-tree content and is not an authorization mechanism. These are design conclusions to validate against the chosen provider and all access paths. See [GitHub repository roles](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization), [GitLab repository protections](https://docs.gitlab.com/user/project/repository/protect/), [Azure Repos permissions](https://learn.microsoft.com/en-us/azure/devops/repos/git/set-git-repository-permissions?view=azure-devops), and [Git sparse checkout](https://git-scm.com/docs/git-sparse-checkout).

## Enterprise deployment questions

| Area | Evidence required before rollout |
| --- | --- |
| Identity | Human and service accounts map to participant IDs; impersonation is rejected. |
| Access | Allowed reads and writes succeed; denied paths and alternate access routes fail. |
| Hosting | SaaS or self-hosted location, network access, operating window and responsible operator are recorded. |
| Data | Classifications, permitted payloads, retention, backups and residency requirements are resolved. |
| Recovery | Interrupted writes and processing recover; no silent loss or uncontrolled resend occurs. |
| Operations | Delivery age, errors, audit records, worker health and cost are visible. |
| Revocation | Credentials, sessions and worker access are removed and tested; previously downloaded copies remain a separate retention concern. |
| Usability | A human can publish and confirm a handoff without confusing delivery with completion. |

## Investigation sequence

1. Document one team's human and agent workflow and its permitted data.
2. Select a provider and test the repository-level baseline with synthetic records.
3. Compare separate repositories with a mediated path-access prototype. Document bypass attempts and failures.
4. Test startup, publication, receipt, verification and recovery on every selected provider.
5. Record results, unsupported cases and operating limits. Obtain the organization's deployment acceptance before expanding.

No enterprise certification, universal provider support, or Drive-like file permissions are claimed by v0.1. Publish measured results as implementation work progresses.
