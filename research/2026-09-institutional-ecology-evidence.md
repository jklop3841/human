# Institutional Ecology Evidence Map — 2026-09

Status: active external calibration  
Related: `cases/human-casebook/VOLUME-004.md`  
Graph: `cases/human-casebook/institution-ecology-graph.yaml`

## Purpose

This file separates:

1. externally documented institutional relationships;
2. Lu Cheng's structural synthesis;
3. relationships that are plausible but still need jurisdiction-specific verification.

Core warning:

> A graph edge is not automatically a causal coefficient, a corruption claim, or proof of unified institutional intent.

---

## EVIDENCE-001 — Healthcare payment can alter provider incentives

Source: Centers for Medicare & Medicaid Services (CMS), Hospital Value-Based Purchasing Program.

URL: https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/hospital-value-based-purchasing

CMS states that the Hospital Value-Based Purchasing Program adjusts Medicare hospital payments based on quality of care. Measures include outcomes and dimensions such as mortality/complications, healthcare-associated infections, patient safety, patient experience, efficiency and cost.

### What this supports

External fact:

`payer -> hospital` can be both a `funds` edge and an `incentive/oversight` edge.

### What this does not prove

It does not prove that every payment-linked metric improves care or distorts care. The effect of a specific metric requires separate evaluation.

---

## EVIDENCE-002 — Criminal justice is a sequence of distinct discretionary institutions

Source: U.S. Bureau of Justice Statistics, The Justice System.

URL: https://bjs.ojp.gov/justice-system

BJS describes common criminal justice stages including entry into the system, prosecution and pretrial services, adjudication, sentencing/sanctions, and corrections. It also explicitly states that discretion is exercised throughout the system by police, prosecutors, judges/magistrates, correctional officials, and parole authorities.

### What this supports

External fact:

`law_enforcement -> prosecution -> court -> corrections` is a real institutional processing chain, with distinct decision points and discretion.

### What this does not prove

It does not prove that one jurisdiction's exact procedure generalizes globally. Justice systems vary by legal system and jurisdiction.

---

## EVIDENCE-003 — Banking supervision forms a monitoring and intervention feedback loop

Source: Federal Reserve Board, Supervision & Regulation.

URL: https://www.federalreserve.gov/supervisionreg.htm

The Federal Reserve describes supervision as monitoring financial institutions, collecting and analyzing banking-sector data, developing rules and guidance, and taking timely and proportionate action to address material financial risks.

### What this supports

External fact:

`bank -> regulator` carries risk/reporting information and `regulator -> bank` carries supervision, policy and intervention.

### Author synthesis

Human models the additional loop:

`institution condition -> public/market expectations -> funding behavior -> institution condition`

This expectation loop is consistent with banking-run dynamics but its strength varies by institution, depositor structure, liquidity, guarantees and communication environment.

---

## EVIDENCE-004 — Scientific funding is multi-stage rather than a single gate

Sources: NIH Grants & Funding, Review; NIH Grants Policy Statement §2.4.

URLs:

- https://www.grants.nih.gov/grants-process/review
- https://grants.nih.gov/grants/policy/nihgps/HTML5/section_2/2.4_the_peer_review_process.htm

NIH describes a two-level peer-review system: scientific/technical review by expert scientific review groups, followed by advisory-council review and institute/center funding decisions. NIH also maintains processes for appeal/reconsideration under specified review problems.

### What this supports

External fact:

`researcher -> peer_review -> advisory/funder -> funding_decision` contains multiple institutional filters rather than one unified evaluator.

### Human implication

Multiple filters can create both error correction and cumulative gatekeeping. Which dominates is empirical, not predetermined by the graph.

---

## EVIDENCE-005 — Rules can shorten the delay between private discovery and shared knowledge

Source: National Human Genome Research Institute, Human Genome Project Fact Sheet.

URL: https://www.genome.gov/about-genomics/educational-resources/fact-sheets/human-genome-project

NHGRI states that Human Genome Project researchers agreed through the Bermuda Principles to rapid public release of sequence data, and identifies this as an influential data-sharing legacy.

### What this supports

External fact:

Institutional rules can deliberately create an `open_information` correction edge.

This supports Volume 004's claim that information topology is partly designed, not simply inherited.

---

## EVIDENCE-006 — Critical infrastructure dependencies can be bidirectional

Source: Federal Energy Regulatory Commission / North American Electric Reliability Corporation, February 2021 Freeze Final Report summary.

URL: https://www.ferc.gov/news-events/news/final-report-february-2021-freeze-underscores-winterization-recommendations

FERC/NERC reported that 2021 generation outages involved both freezing and fuel-supply problems. It also reported natural-gas production declines caused partly by power losses at gas-system facilities.

### What this supports

External fact:

`natural_gas -> electric_generation` and `electricity -> natural_gas_production/processing` can form a bidirectional dependency under relevant conditions.

### Human implication

A dependency graph may contain feedback loops; linear supply-chain models can miss such cascades.

### Safety boundary

This material is for resilience and dependency analysis, not attack-target ranking or disruption planning.

---

## EVIDENCE-007 — Platform governance inserts transparency and external-scrutiny edges

Sources: European Commission, Digital Services Act transparency and platform-impact materials.

URLs:

- https://digital-strategy.ec.europa.eu/en/policies/dsa-brings-transparency
- https://digital-strategy.ec.europa.eu/en/policies/dsa-impact-platforms

The Commission describes transparency reporting, machine-readable reporting templates, risk assessments, researcher/regulator data access, advertising repositories, recommender-system transparency, and user options regarding personalized recommendations.

### What this supports

External fact:

`regulator -> platform` includes oversight/transparency obligations, while `platform -> researcher/regulator` can include mandated information-access edges.

### What this does not prove

Transparency does not guarantee correction. The effect depends on data quality, audit quality, enforcement and whether external actors can translate visibility into action.

---

## EVIDENCE-008 — Fragmentation and overlap must not be equated automatically with waste

Sources: U.S. Government Accountability Office, Fragmentation, Overlap, and Duplication guide and annual reports.

URLs:

- https://www.gao.gov/products/gao-15-49sp
- https://www.gao.gov/products/gao-26-108505

GAO distinguishes fragmentation, overlap and duplication and evaluates when these create inefficiency. GAO also recognizes that some overlap or fragmentation may be warranted and should be assessed with trade-offs and unintended consequences in mind.

### What this supports

Human hard rule:

`multiple_nodes_or_redundant_edges != automatic_bureaucratic_failure`

Redundancy can sometimes be waste; it can also provide specialization, independent verification, competition, backup capacity or checks and balances.

---

# Author synthesis vs external evidence

The following are **Lu Cheng / Human structural synthesis**, not claims directly stated by the sources above:

1. `institutional failure is often relational failure`;
2. `node quality alone is insufficient; edge quality matters`;
3. `handoff_loss`, `responsibility_gap`, `boundary_blindness`, and `correction_blocking` are useful cross-domain diagnostic categories;
4. system outcomes can be analyzed as `node state + typed edges + direction + delay + feedback`;
5. a correction mechanism in one node can propagate through payment, standards, precedent, public data or oversight.

These are currently analytical hypotheses/frameworks. They should be retained only if repeated cross-domain cases continue to make them useful.

---

# Evidence discipline for future graph expansion

Before adding a high-confidence edge between two of the 106 institution archetypes, record:

```yaml
edge_evidence:
  from: ""
  to: ""
  type: "funds | authority | information | certification | enforcement | dependency | oversight | appeal | reputation | feedback"
  jurisdiction: ""
  source: ""
  externally_verified: false
  direction_verified: false
  persistence: "episodic | recurring | structural | unknown"
  evidence_level: "E0 | E1 | E2 | E3 | E4"
  author_inference: ""
  counterexample: ""
  revision_condition: ""
```

Do not infer that an edge exists everywhere merely because it exists in one country or institutional design.

---

# Current research conclusion

Volume 004 is strong enough to justify a new **analysis layer**, but not a universal law of institutions.

The best-supported current proposition is narrower:

> Many socially important outcomes are generated through sequences of institutions with distinct roles, information, incentives and discretionary decisions; therefore, analysis that stops at one institution may miss handoff effects, feedback loops, cross-system dependencies and correction channels.

The next empirical milestone is not to invent more categories. It is to connect the existing 106 institution archetypes gradually, with evidence on each important edge.
