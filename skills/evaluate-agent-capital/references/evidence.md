# What evidence proves

| Evidence | Supports | Does not prove |
|---|---|---|
| Repository history | publication sequence and edits | original authorship outside the repository |
| Content hash | exact artifact identity | creator, legality, quality or safety |
| Digital signature | a key signed a claim | claim truth or key owner's legal rights |
| Artifact attestation | source/build provenance | correctness, security or performance |
| Signed Agent Card | publisher-bound identity and metadata | demonstrated capability |
| OAuth token | authorization scope and issuer claim | successful execution |
| Invocation receipt | a signer reports an invocation | outcome value without evaluation |
| OpenTelemetry trace | recorded execution path and metrics | unlogged behavior or causal lift |
| Benchmark result | performance on a defined suite | general performance outside the suite |
| Independent evaluation | stronger outcome evidence | universal validity |
| Payment receipt | a settlement occurred | result quality or legal ownership |
| Trademark/certification mark | controlled brand signal | technical superiority by itself |
| License or contract | agreed permissions and obligations | enforcement against non-parties |

## Evidence levels

- **E0 Assertion** — unverified statement.
- **E1 Self-recorded** — first-party record with stable timestamp.
- **E2 Signed** — identity-bound, integrity-protected claim.
- **E3 Corroborated** — independent records agree.
- **E4 Auditable** — reproducible evidence, retained inputs or digests, transparent method.
- **E5 Adjudicable** — contract, governance and dispute process identify who can decide conflicts.

Report each important edge with its evidence level. Do not use the highest evidence level of one edge to upgrade the entire provenance chain.
