# AIDE, visually

[Overview](README.md) / [Team workflow](TEAM-WORKFLOW.md) / [Architecture](ARCHITECTURE.md) / [Pilot guide](ADOPTION.md)

Nine diagrams explain the shared workspace, everyday handoffs and the first pilot.

> **Design reference:** v0.1 is documentation and templates. These diagrams describe the contract, not a shipped runtime or completed deployment.

## 1. Connect teams through the Git Service

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/team-exchange-dark.svg">
  <img src="assets/team-exchange.svg" alt="The Git Service exchanges context, messages and receipts between humans and independent agents. Sessions remain private." width="100%">
</picture>
</p>

Independent sessions read shared context and publish deliberate updates. Their conversations stay private. [Read the details](TEAM-WORKFLOW.md).

## 2. Organize work with the Four Ps

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/workspace-map-dark.svg">
  <img src="assets/workspace-map.svg" alt="The Four Ps: People for who does the work, Products for what the team builds and uses, Processes for how work gets done, and Projects for what is being delivered." width="100%">
</picture>
</p>

People, Products, Processes and Projects give both humans and agents a common map. Product entries include access instructions; process entries explain how work is done. [Read the details](TEAM-WORKFLOW.md#the-four-ps-a-workspace-people-can-navigate).

## 3. Make delivery observable

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/receipt-sequence-dark.svg">
  <img src="assets/receipt-sequence.svg" alt="Sender publishes to the Git Service. Receiver reads and validates, then stores a receipt. Sender checks the receipt and stores verification. Human review is separate." width="100%">
</picture>
</p>

The sender can independently verify retrieval. Human review and completion require separate evidence. [Read the details](ARCHITECTURE.md#processing).

## 4. Keep team delivery explicit

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/team-routing-dark.svg">
  <img src="assets/team-routing.svg" alt="Synthetic message QA-042 has explicit recipients qa, delivery and product at routing version 7. Two receipts are stored; product remains pending. Delivery is partial." width="100%">
</picture>
</p>

A team name resolves to named recipients. Track each receipt so partial delivery stays visible. [Read the details](TEAM-WORKFLOW.md#send-to-a-team).

## 5. Publish a usable QA report

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/qa-report-example-dark.svg">
  <img src="assets/qa-report-example.svg" alt="Synthetic project export QA specification in Feature, Scenario, Given, When, Then form. Execution is not run and has no pass/fail result or evidence." width="100%">
</picture>
</p>

Pair readable findings and Gherkin specifications with honest execution status. A specification alone is not a test result. [Read the details](TEAM-WORKFLOW.md#publish-a-useful-update).

## 6. Diagnose a missing update

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/delivery-triage-dark.svg">
  <img src="assets/delivery-triage.svg" alt="No message: inspect remote branch and path. No receipt: inspect routing and collector. Receipt but no reply: do not resend. Rejection or conflict: stop and preserve the cause." width="100%">
</picture>
</p>

Use the last durable record to locate the gap. A repeated send is not the default fix. [Read the details](ARCHITECTURE.md#failure-handling).

## 7. Run a bounded pilot

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/pilot-path-dark.svg">
  <img src="assets/pilot-path.svg" alt="Pilot stages: prepare private context; connect and test access; prove publication, receipt and verification; review recovery, quality and human acceptance." width="100%">
</picture>
</p>

Test two isolated sessions, then review the evidence before expanding. [Read the details](ADOPTION.md).

## 8. Adapt it for your organization

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/fork-boundary-dark.svg">
  <img src="assets/fork-boundary.svg" alt="Public upstream contains reusable design. A public fork contains adaptations and synthetic examples. A separate private deployment holds organization context and operational records." width="100%">
</picture>
</p>

Fork the reusable framework. Create a separate private workspace for real team operations. [Read the details](FORK-GUIDE.md).

## 9. Plan enterprise access

<p>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/enterprise-access-dark.svg">
  <img src="assets/enterprise-access.svg" alt="Humans and agents access shared or restricted records through an enforced boundary. Fine-grained path access is an investigation, not a shipped capability." width="100%">
</picture>
</p>

One logical workspace can use separate repository boundaries or a carefully enforced service. [Read the enterprise investigation](ENTERPRISE.md).
