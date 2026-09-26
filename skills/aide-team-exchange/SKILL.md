---
name: aide-team-exchange
description: Publish selected work, collect addressed updates or verify delivery in an established AIDE Git workspace. Applies to routine team exchange, not new access grants or product execution.
---

# Team exchange

Read the private deployment's entry point, approved role, configuration and current progress. Follow [daily use](../../DAILY-USE.md) and the configured exchange profile. Use [aide-manual-v1](../../EXCHANGE-CONTRACT.md) only when that profile is selected; preserve an existing deployment schema otherwise.

For publication, preserve the human's selected work and priority, resolve explicit recipients, persist the outbox before attempting, publish selected files and independently read them back. An uncertain write requires destination inspection before retry.

For collection, freeze the remote commit, validate sender and address, read eligible unseen records, and reconcile existing receipts. Keep last-read and last-reported progress separate. Create only the missing exact-content receipts. Do not acknowledge messages addressed solely to another receiver.

For verification, validate the real receiver, message version and stored receipt digest. Publish at most one verification record. A receipt establishes retrieval, not human review or completed work.

Honor manual operation or the deployment's already approved bounded schedule. Stop affected permission, identity or content conflicts. No duplicate delivered requests, new schedules or inferred access. Summarize meaningful work with source dates and links; omit synthetic tests from business summaries.
