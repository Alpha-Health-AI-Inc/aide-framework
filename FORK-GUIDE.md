# Fork and adapt the Alpha Health AIDE Framework

This repository is a documentation starter under MIT. Forking it copies the design and templates; it does not install a working AIDE runtime or connect any organization systems.

## Start here

1. Fork this repository into an organization you control, using your authorized GitHub identity.
2. Read README.md, ARCHITECTURE.md, ADOPTION.md and ROLE-TEMPLATE.md.
3. Choose one internal pilot workflow and record its accountable owner, allowed data, recipients, tools and acceptance criteria.
4. Keep deployment identities, credentials, internal policies and real message data outside the public fork. Use synthetic fixtures for development.
5. Implement the contract and recovery checks before adding model-driven work. Track proposed, implemented and verified capabilities separately.
6. Preserve the MIT copyright and permission notice in copies or substantial portions. Describe your version as a derivative; do not imply Alpha Health endorsement or production certification.

## Prompt to give Claude or another implementation assistant

> Use https://github.com/Alpha-Health-AI-Inc/aide-framework as the upstream design for an organization-specific derivative. First read all five documentation files and identify what is proposed versus implemented. This repository currently has no runtime. Prepare a concrete pilot plan and implementation backlog for one authorized internal workflow. Preserve stable agent identity, accountable ownership, scoped tools, exact-content delivery receipts, sender verification, durable recovery and separate human acceptance. Keep organization-specific configuration and operational data private; public fixtures must be synthetic. Do not assume our organization has any particular identity provider, repository host, model vendor or hosting environment. Identify those deployment decisions explicitly. Start with deterministic message validation, publish/collect/receipt/verify behavior and the acceptance scenarios in ADOPTION.md. Do not create infrastructure, grant access or connect live systems without the applicable authorization. If authorized to implement, work in our fork and report actual tests and remaining gaps; do not claim the documentation itself provides working features.

## Implementation order

- Contract schemas and valid/invalid synthetic fixtures.
- A single transport adapter with durable outbox, bounded collection and receipt verification.
- Restart, duplicate, integrity-conflict and wrong-recipient checks.
- Role configuration, scoped runtime adapter and operator delivery-status view.
- Customer-environment access isolation and independent pilot acceptance.
- Additional adapters, scheduling integrations and measured scale.

Project branding is Alpha Health AIDE Framework. Each adopter owns its deployment decisions and remains responsible for its actual runtime, data handling and approvals.
