# Workspace templates

These files are source templates. The setup agent renders them locally, reviews the diff, then publishes to the approved private workspace. They are not live organization records.

| Source | Destination and use |
| --- | --- |
| `workspace/workspace.json` | `workspace.json`; exact provider, repository, branch and manual profile |
| `workspace/organization/README.md` | Organization context from approved sources |
| `workspace/people/person.md` | `people/<person-id>/README.md`; one for each person |
| `workspace/products/product.md` | `products/<product-id>/README.md`; one for each assigned product |
| `workspace/products/access.md` | `products/<product-id>/access.md`; requirements and verified access state, never secrets |
| `workspace/processes/process.md` | `processes/<process-id>/README.md`; approved procedure or explicitly pending draft |
| `workspace/projects/project.md` | `projects/<project-id>/README.md`; scoped work with links to the other Ps |
| `workspace/registry/participants.json` | Human and agent identities, attribution mechanism and routes |
| `workspace/registry/teams.json` | Explicit membership and routing version |
| `workspace/operations/setup-state.json` | Stage progress and sanitized evidence references |
| `workspace/.gitignore` | Merge the ignore rules into a new workspace; preserve existing rules |
| [Employee handoff](EMPLOYEE-HANDOFF.md) | `people/<person-id>/ONBOARDING.md`; the private link given to the employee |
| [Startup template](../START-HERE-TEMPLATE.md) | `START-HERE.md`; fill organization-specific values |
| [Role template](../ROLE-TEMPLATE.md) | `roles/<agent-id>.md`; approved scope and owner |

Create `people/<person-id>/work/`, team entries, and the required message/receipt/verification directories as needed. Git does not preserve empty directories; use a short README when an empty working area must appear in a clone. Store the profile guides or pinned readable references in the private startup instructions so another session can find the same procedure.

Create entries for both the manager and employee, including each human and their agent. Expand the sample registry entries rather than overwriting one identity with another. Confirm that every team member and recipient resolves to an entry in the same registry.

Replace angle-bracket placeholders with confirmed values. Preserve genuinely unknown business information as a dated pending item with an owner; do not publish unresolved destination, identity or routing placeholders. Never place credentials, personal HR details or private chat transcripts in these records. All committed pilot content is team-readable.

The templates describe the new workspace convention. Do not copy them over an existing operational registry or rewrite its history without an explicit reviewed migration.
