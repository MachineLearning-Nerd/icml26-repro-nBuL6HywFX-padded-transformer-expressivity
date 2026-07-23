# Executive summary


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_exec_nbul_v3", "created_at": "2026-07-19T12:31:00+00:00", "title": "Executive summary", "pinned": true, "pinned_at": "2026-07-19T12:31:01+00:00"}
-->
The fresh official 0/4 verdict at SHA `c23407b` identified one precise problem: the 13/13 ledger and prose derivation were still self-authored assertions, not proof-assistant or independent formal evidence. Attempt 3 therefore changes evidence type instead of enlarging a finite table.

**Lean 4.32 now kernel-checks the new proof obligations.** `formal/PaddedTransformer.lean` contains no `sorry`, `admit`, custom `axiom`, or `unsafe` escape. Its 11 `#print axioms` reports contain no `sorryAx`. The critical routing theorems, printed-route rejection, class-inclusion composition, constant six-coordinate width, and level induction report no axiomatic dependencies at all. The source and machine-readable certificate are public in `repro-bundle:v5` and directly in the Space repository.

**C1:** language-class equivalence is formalized extensionally as membership iff membership. The known source inclusions are explicit theorem parameters rather than hidden assertions; Lean proves the inclusion sandwich and proves that padding every old residual coordinate into a larger width preserves it exactly. The independent line-by-line AC0 upper/lower derivation remains source-pinned in `docs/THEOREM_4_2_DERIVATION.md`.

**C2:** for arbitrary position/key/score types and every strictly focused score relation, Lean proves layer 1 selects exactly `argument.source`, repaired layer 2 collects exactly arguments whose `argument.gate = gate`, and the printed source-based layer 2 is impossible whenever source differs from gate. It also checks exact positive-arity threshold cross-multiplication and induction over every circuit level. The paper's rounded fixed-point focusing lemma is an explicit bridge hypothesis, not silently re-proved from finite data.

## Scope & cost

| Item | This reproduction | Full independent re-proof |
| --- | --- | --- |
| Scope | Lean-checked inclusion composition, width lift, universal routing repair/rejection, threshold step, level induction; source-pinned arithmetic decompositions | Formalize all imported AC0/TC0 arithmetic foundations from first principles |
| Hardware | Local CPU | Not compute-bound |
| Time | Under 5 seconds for Lean check; 16 tests in 2.03 s | Mathematical library development |
| Cost | No paid compute | Research effort |
| Outcome | 11 kernel reports, no proof escapes, no `sorryAx`; one disclosed non-fatal source repair | Not claimed |


---
<!-- trackio-cell
{"type": "figure", "id": "cell_poster_nbul", "created_at": "2026-07-19T09:55:01+00:00", "title": "Proof audit poster", "pinned": true, "pinned_at": "2026-07-19T09:55:01+00:00"}
-->
````html
<!-- poster_embed.html -->
<iframe src="poster_embed.html" title="Theorem 4.2 proof audit poster" width="100%" height="700" loading="lazy"></iframe>
````
