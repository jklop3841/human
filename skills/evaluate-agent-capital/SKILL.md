---
name: evaluate-agent-capital
description: Evaluate whether an AI agent, skill, protocol, workflow, compiler, or agent portfolio qualifies as a durable and economically capturable Agent Provenance Capital asset. Use when assessing creator-to-agent ownership claims, signed identity and lineage, source or artifact hashes, runtime authorization, invocation metering, benchmark lift, reputation records, licensing, forks, revenue sharing, governance, security, or readiness to charge per invocation, certification, subscription, or verified outcome.
---

# Evaluate Agent Capital

Evaluate the asset as a chain of independently verifiable claims. Do not treat a repository, hash, signature, invocation count, benchmark, or payment record as sufficient by itself.

Read [standard.md](references/standard.md) for the proposed architecture and [rubric.md](references/rubric.md) for scoring. Read [evidence.md](references/evidence.md) when deciding what a technical artifact actually proves.

## Establish the claim

Identify:

- the claimed creator or rights holder;
- the protocol or method embedded in the agent;
- the exact artifact and version;
- the runtime instances that execute it;
- the economic right being claimed;
- the decision the evaluation will support.

Separate legal ownership, publisher identity, artifact integrity, runtime identity, delegated authority, measured performance, reputation, and revenue entitlement.

## Build the provenance chain

Trace:

`principal → signed protocol → agent artifact → attested build → runtime instance → invocation receipt → evaluation attestation → settlement`

For every edge, record:

- identifier;
- signer and verifier;
- evidence location;
- revocation or expiry mechanism;
- confidence and missing proof.

Remember:

- a hash proves content equality, not authorship;
- a signature proves that a key signed a claim, not that the claim is true;
- an artifact attestation proves provenance, not safety or performance;
- an Agent Card describes claimed capabilities, not demonstrated results;
- a payment proves settlement, not task success;
- an invocation count proves little without deduplication and anti-Sybil controls.

## Test economic capture

Classify execution paths:

- hosted and controlled;
- marketplace or certified runtime;
- enterprise private deployment with reconciliation;
- locally copied or fully offline.

Do not claim reliable per-call metering for fully offline, user-controlled copies. Identify the actual control point: hosted runtime, authorization server, evaluator, registry, certification mark, update service, or payment gateway.

Evaluate forks separately. A fork must receive a new artifact hash and runtime identity, retain its parent lineage, and must not inherit verified reputation automatically.

## Evaluate outcomes

Require a baseline and a versioned task suite before accepting “performance improvement.”

Prefer a reputation vector over one opaque score:

- verified invocations;
- independent evaluators;
- task coverage;
- success-rate confidence interval;
- median lift over baseline;
- cost and latency;
- critical failure rate;
- compatibility;
- recency and maintenance;
- paid or enterprise adoption.

Reject benchmarks that allow the asset owner to control tasks, execution, evaluation, and publication without independent checks.

## Assign maturity

Assign the highest fully satisfied level:

- **APC-0 Archive** — static knowledge or source only.
- **APC-1 Executable** — runnable agent or workflow.
- **APC-2 Identified** — signed manifest, immutable version, lineage and revocation.
- **APC-3 Metered** — deduplicated signed invocation receipts and privacy controls.
- **APC-4 Verified** — versioned baselines and independent evaluation attestations.
- **APC-5 Economic** — enforceable authorization, settlement, licensing, forks and revenue allocation.
- **APC-6 Standard** — multi-party adoption, neutral conformance tests, governance and succession.

Do not average away a missing lower level. If a required level is incomplete, cap the result there.

## Attack the claim

Test at least:

- copied or renamed source;
- stripped telemetry;
- replayed receipts;
- fake callers and self-invocation;
- benchmark leakage or cherry-picking;
- compromised signing key;
- stale or vulnerable runtime;
- fork attribution disputes;
- offline use;
- model upgrades that erase measured lift;
- legal rights that do not match technical claims;
- single-platform or single-payment dependency.

For each failure mode, specify prevention, detection, response, residual risk, and owner.

## Return the assessment

Use this structure:

1. Claim and decision.
2. Observed evidence and unsupported assertions.
3. Provenance graph and broken edges.
4. Current APC maturity level.
5. Reputation vector.
6. Metering and payment feasibility by execution path.
7. Rights, forks, and revenue allocation.
8. Security, privacy, and governance failures.
9. Countermodels and falsifiers.
10. Minimum evidence needed for the next level.
11. Build / do-not-build recommendation.

State clearly that Agent Provenance Capital and PIRS are proposed economic and technical frameworks, not current legal personhood or a new statutory intellectual-property right.
