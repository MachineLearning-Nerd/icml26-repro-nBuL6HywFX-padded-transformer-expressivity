# Lean formal audit boundary

## Why this attempt exists

The official verdict at Space SHA `c23407b0b2e93b0e1c07607a0a504e85af5d411e`
rejected both claims because a self-authored dependency ledger and prose proof
were not proof-assistant or independent formal evidence. Attempt 3 therefore
uses the Lean 4.32 kernel and exposes every source-paper import as a theorem
hypothesis.

## Kernel-checked content

`formal/PaddedTransformer.lean` proves, without finite enumeration:

- extensional language-class equivalence from opposing inclusions;
- simultaneous closure of the AC0 and TC0 inclusion sandwiches;
- exact preservation of every old residual coordinate under width padding;
- constant six-coordinate width for the `self/source/gate` repair;
- exact layer-1 source routing for arbitrary position and score types;
- exact layer-2 destination collection for arbitrary position and score types;
- rejection of the printed layer-2 route whenever source differs from gate;
- transfer from any exact fixed-point focusing operator to repaired routing;
- exact positive-arity threshold cross-multiplication; and
- induction from a correct base level and universally correct level step to
  every circuit level.

The runner strips Lean comments before rejecting `sorry`, `admit`, custom
`axiom`, and `unsafe` tokens. It pins Lean `v4.32.0`, checks the source hash,
parses 11 `#print axioms` reports, and fails if `sorryAx` appears. The resulting
certificate is `outputs/lean_formal_certificate.json`.

## Explicit imported boundary

This artifact does not pretend to formalize the complete foundations of AC0,
TC0, logspace uniformity, or fixed-point exponential arithmetic. The four
source inclusion results and the rounded-PE exact-focusing result are explicit
hypotheses at the formal boundary. Their source-pinned independent derivation
is in `docs/THEOREM_4_2_DERIVATION.md`.

This boundary is materially stronger than the rejected ledger: Lean checks
the new repair and all theorem-composition glue, while imported claims remain
visible rather than being converted into booleans printed by Python.

## Reproduction

```bash
elan toolchain install leanprover/lean4:v4.32.0
lean formal/PaddedTransformer.lean
python repro/run_lean_formal_check.py
PYTHONPATH=repro python -m pytest -q repro/tests
```

Observed locally on 2026-07-19: Lean `4.32.0`, 11 theorem reports, no forbidden
escape tokens, no `sorryAx`, and 16 passing tests.
