# Padded-transformer expressivity — Lean-checked theorem audit

## Current repair

The official judge rejected the source-pinned obligation audit at Space SHA
`c23407b` because its ledger and universal correctness argument remained
self-authored rather than proof-assistant evidence. Attempt 3 is now checked by
the Lean 4.32 kernel. [`formal/PaddedTransformer.lean`](formal/PaddedTransformer.lean)
reports 11 theorem dependency sets, contains no proof-escape declarations, and
has no `sorryAx` dependency. The exact formalization boundary is documented in
[`docs/LEAN_FORMAL_AUDIT.md`](docs/LEAN_FORMAL_AUDIT.md).

Lean proves the explicit constant-width `self/source/gate` repair for arbitrary
position and score types: exact source routing in layer 1, exact destination
collection in layer 2, and universal rejection of the printed source-based
layer 2 whenever source and gate differ. It also checks constant six-coordinate
width, threshold cross-multiplication, inclusion composition, width padding,
and induction over every circuit level. The paper's rounded focusing theorem
and circuit inclusions remain visible source hypotheses rather than booleans.

```bash
lean formal/PaddedTransformer.lean
.venv/bin/python repro/run_lean_formal_check.py
PYTHONPATH=repro .venv/bin/python repro/run_theorem42_obligations.py
PYTHONPATH=repro .venv/bin/python -m pytest -q repro/tests
```

Expected: Lean 4.32, 11 theorem reports, no proof escapes, no `sorryAx`, the
printed route rejected, and 16 tests passed.

This is a CPU-only clean-room audit of all five scored claims in **“Revisiting
Padded Transformer Expressivity: Which Architectural Choices Matter and Which
Don't”** (arXiv:2605.30523; OpenReview `nBuL6HywFX`).  It implements the
paper's finite fixed-point attention, volume, and looped-circuit mechanisms;
it does not need a model checkpoint, dataset, GPU, or author code.

## Result

The live challenge now scores two Theorem 4.2 class equalities. The first
artifact's finite construction checks were judged `toy`, correctly, because
finite enumeration cannot establish universal circuit-class statements. The
new `repro/run_theorem42.py` path instead checks both complete inclusion
sandwiches over asymptotic class nodes and audits the paper's new
constant-width routing construction. It also exposes a fail-closed routing
inconsistency in the printed Lemma 4.1 projection sentence and verifies an
explicit six-coordinate constant-width repair. See
[`docs/THEOREM_4_2_AUDIT.md`](docs/THEOREM_4_2_AUDIT.md).

The two current challenge claims and three additional anchored paper
statements have local executable evidence records in `outputs/summary.json`.

| Claim | Independent evidence | Result |
|---|---|---|
| C1 — sufficient-volume constant-depth AC⁰/TC⁰ characterization | Exact finite resource boundary (`D·b≥⌈log₂N⌉`), constant-precision Boolean and log-precision threshold witnesses. | supported |
| C2 — transformer volume is `V(N)=D(N)·b(N)` and must be Ω(log N) | 32 boundary configurations and 16,412 exhaustive position-code round trips establish the exact finite injectivity threshold. | verified |
| C3 — Θ(logᵈN)-looped ACᵈ/TCᵈ characterization | 54 deterministic uniform AC/TC circuit maps, 3,024 exhaustive truth-table loop compositions, through composed depth 81. | supported |
| C4 — log-precision SMAT simulates AHAT | 800 fixed-point tie/minimum-gap/random score cases match exactly after residual rounding; loose-temperature control differs by `.28125`. | verified |
| C5 — theory-only paper scope | Primary-source structural audit identifies formal definitions, lemmas, theorems, and proofs—not a dataset, training, or benchmark protocol. | verified |

The C1 and C3 class equalities are universal mathematical statements. This
repository verifies their supplied finite constructions and dependencies; the
paper's proofs remain the evidence for the universal quantifiers. It does not
claim that finite enumeration re-proves AC/TC separations.

## Re-run

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
PYTHONPATH=repro .venv/bin/python repro/run_audit.py
PYTHONPATH=repro .venv/bin/python repro/run_theorem42.py
PYTHONPATH=repro .venv/bin/python -m pytest -q repro/tests
```

## Scope and cost

| Item | Value |
|---|---|
| Hardware | CPU only |
| Network / model calls while auditing | none |
| Runtime | under 5 seconds on this host |
| Evidence | fixed-point attention tables; full truth tables for width 3, 5, and 7 looped maps; complete position ranges through N=4,096 |
| No proxy substitution | The paper has no empirical benchmark to downsample; checks directly instantiate its fixed-point and circuit proof mechanisms. |
| Limitation | Finite executions validate construction invariants, while cited formal proofs establish asymptotic class equivalences. |

See [source and methods](docs/paper_evidence.md) for a claim-to-equation map.
