# Agent Provenance Capital and PIRS

## Core distinction

- A repository preserves knowledge.
- A protocol defines repeatable behavior.
- An agent is an executable carrier of protocols.
- A runtime instance performs work.
- A receipt records a particular invocation.
- An evaluation attestation estimates performance.
- A reputation graph aggregates verified history.
- A legal or contractual principal receives rights and revenue.

Agent Provenance Capital is present only when these objects form a maintained, verifiable chain.

## PIRS modules

PIRS means Protocol Invocation & Reputation Standard. Its minimal modules are:

1. Protocol Manifest — protocol identity, version, digest, author claim, license and compatibility.
2. Agent Manifest — creator, embedded protocols, artifact digest, lineage, capabilities and revenue policy.
3. License Grant — principal, scopes, quota, expiry, execution path and pricing plan.
4. Invocation Receipt — invocation, instance, task class, status, trace, cost and signatures.
5. Evaluation Attestation — suite, baseline, protocol result, lift, sample and evaluator.
6. Reputation Snapshot — verified aggregate metrics with window and methodology.
7. Settlement Receipt — payment reference and revenue allocation.

## Identity layers

Keep six identities distinct:

1. creator or rights-holder identity;
2. protocol identity;
3. artifact identity;
4. runtime-instance identity;
5. delegated authorization identity;
6. economic settlement identity.

## Standards composition

Prefer existing standards:

- A2A Agent Cards for discovery and signed capability metadata;
- MCP for tool invocation;
- OAuth 2.1 and workload identity for authorization;
- Sigstore and SLSA-style attestations for artifact provenance;
- OpenTelemetry for traces and metrics;
- SPDX identifiers for machine-readable licensing;
- AP2 mandates for intent-bound purchase authorization;
- MPP, x402, or ordinary invoicing for settlement.

PIRS binds references to these proofs; it does not replace their transport, identity, or payment functions.

## Counters

Never publish one undifferentiated count. Keep:

- raw invocations;
- verified and deduplicated invocations;
- completed invocations;
- evaluated invocations;
- verified successes;
- paid invocations;
- unique tenants;
- independent evaluators.

Attach a measurement window, methodology, protocol version, and anti-abuse policy.

## Offline boundary

Fully offline copies controlled by the user cannot be trusted to report every call. Treat local telemetry as self-reported unless a trusted execution environment or independent reconciliation is present. Monetize control points rather than claiming impossible universal metering.
