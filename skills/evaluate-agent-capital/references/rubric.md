# APC maturity rubric

## APC-0 Archive

Required:

- identifiable source material;
- version or date;
- author or publisher claim.

Fails if the asset is presented as executable or metered without a runtime.

## APC-1 Executable

Required:

- runnable entrypoint;
- declared inputs and outputs;
- deterministic validation or repeatable acceptance test;
- explicit permissions and dependencies.

## APC-2 Identified

Required:

- canonical protocol and agent identifiers;
- semantic version;
- content digest;
- publisher signature or equivalent identity-bound attestation;
- lineage for forks;
- key rotation and revocation path.

## APC-3 Metered

Required:

- unique invocation and idempotency identifiers;
- signed runtime receipt;
- replay prevention and deduplication;
- counter definitions;
- privacy-preserving trace references;
- distinction between self-reported and independently verified use.

## APC-4 Verified

Required:

- versioned benchmark suite;
- baseline;
- sample and time window;
- independent or segregated evaluator;
- failure publication;
- lift, cost and latency;
- confidence interval or uncertainty statement.

## APC-5 Economic

Required:

- authorization and entitlement;
- enforceable control point;
- pricing and settlement;
- rights-holder and contributor allocation;
- fork policy;
- refund, dispute and revocation process;
- enterprise and jurisdictional caveats.

## APC-6 Standard

Required:

- multiple independent implementers;
- public conformance tests;
- published change process;
- conflict-of-interest policy;
- governance succession;
- compatibility and deprecation policy;
- no single operator able to rewrite history silently.

## Decision matrix

| Finding | Consequence |
|---|---|
| Static Markdown only | Cap at APC-0 |
| Runs but lacks signed identity | Cap at APC-1 |
| Signed artifact but no trusted receipts | Cap at APC-2 |
| Counts without baseline or evaluator | Cap at APC-3 |
| Verified but no controllable economic path | Cap at APC-4 |
| Commercial product with one owner only | Cap at APC-5 |
| Ecosystem claim without independent adoption | Do not award APC-6 |
