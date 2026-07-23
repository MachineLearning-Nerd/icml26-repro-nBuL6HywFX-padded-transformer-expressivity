# Independent derivation of Theorem 4.2

## Outcome

This audit supports both current challenge claims under the hypotheses that
actually appear in Theorem 4.2: polynomial padding, constant transformer
depth, L-uniform parameter and positional-encoding generators, sufficient
volume `D(N)b(N)=Ω(log N)`, and width at most polynomial.

The result is not inferred from a largest tested input. It follows from two
universal inclusion sandwiches. Every imported theorem and every locally
derived step is listed below. The fail-closed audit rejects the routing
sentence printed in Lemma 4.1 and substitutes a constant-width construction
whose fields and two attention relations are explicit.

## Pinned primary sources

| Source | SHA-256 | Audited anchors |
| --- | --- | --- |
| Svete, Merrill, Cotterell, Sabharwal, *Revisiting Padded Transformer Expressivity* ([arXiv PDF](https://arxiv.org/pdf/2605.30523)) | `fbc31ec9024e20bef85e4e12a262991f098c093d171d6063d57bcf62419b562b` | Defs. 2.1–2.4/A.5; Thms. 4.1–4.2; Lems. 4.1–4.2; Lems. B.1/B.4/B.5; Cor. B.1; App. C.2 pp. 24–25 |
| London and Kanade, *Pause Tokens Strictly Increase the Expressivity of Constant-Depth Transformers* ([arXiv PDF](https://arxiv.org/pdf/2505.21024)) | `c68e8763f1571acc6713886b82f0b3165704bad2ded7fe4437b0c648e89a715b` | Def. 3.6; Thms. 4.1/4.5; Thm. C.1; Lems. C.2–C.4; Thms. C.5/C.7/C.11 |

The PDFs were independently downloaded on 2026-07-19 and their hashes were
computed before the derivation. Imported arithmetic facts are identified
where used; they are not relabeled as executable discoveries.

## Semantics and hypotheses

For input length `N`:

- `D(N)` is residual width and `b(N)` is fixed-point precision.
- Volume is `V(N)=D(N)b(N)` (Defs. 2.1–2.2).
- “Sufficient volume” means `V(N)=Ω(log N)` (Def. 2.3).
- `LPT⁰_{b,D}` denotes polynomially padded, constant-depth LPT families in
  the specified precision and width regimes.
- L-uniformity means that one logspace machine emits the model for length
  `N`, and another emits the PE at `(N,n)` (Def. A.5).
- `c`, `l`, and `p` mean constant, logarithmic, and polynomial resource
  regimes. As usual for a complexity class, a constant-width construction
  is `O(1)`; it does not assert that a one-coordinate residual is sufficient.

The two challenge statements are therefore read as Eqs. (4a) and (4b) under
the theorem’s stated domain—not as claims about arbitrary unpadded,
nonuniform, super-polynomial-width, or growing-depth transformers.

## Claim 1: constant precision equals L-uniform AC⁰

We prove

```text
L-uniform AC⁰ ⊆ L-uniform LPT⁰_{c,D} ⊆ L-uniform AC⁰.
```

### Lower inclusion

1. London–Kanade Theorem 4.1 proves
   `L-uniform AC⁰ = L-uniform LPT⁰_{c,l}`. Its Appendix C.1 gives the
   constructive direction: one input/gate token per circuit vertex, one
   argument token per circuit edge, and two transformer layers per circuit
   level. A polynomial-size constant-depth AC⁰ circuit therefore yields
   polynomial padding and constant transformer depth.
2. With `b(N)=Θ(1)`, sufficient volume gives
   `D(N)Θ(1)=Ω(log N)`, hence `D(N)=Ω(log N)`. This discharges the width
   premise needed to house the log-width construction.
3. Width lifting is constructive. Given an old state `h∈F^d`, use
   `h'=(h,0)∈F^D`. Extend every PE the same way; replace each linear map `W`
   by `diag(W,0)` and each bias by `(b,0)`; keep attention scores on the old
   block and read the same output coordinate. Induction over the fixed layer
   sequence gives `h'_ℓ=(h_ℓ,0)` at every layer. The L-uniform generator
   emits the original entry for old indices and zero otherwise using only
   the old logspace computation plus index comparisons.
4. Thus every L-uniform AC⁰ language has an admissible
   `LPT⁰_{c,D}` recognizer for every sufficient-volume width regime `D`.

### Upper inclusion, expanded

Fix an arbitrary family in `LPT⁰_{c,D}`. Width and padding are polynomial,
so the full residual table and every per-layer operation have polynomial
size.

1. **Parameters and PEs.** The two logspace uniformity machines emit each
   parameter/PE bit from `(1^N,n,coordinate indices)`. These values are
   hardwired into the circuit for length `N`; the circuit generator remains
   logspace. This is uniformity, not an assumption that an arbitrary
   logspace language is computed inside AC⁰.
2. **Products and nonlinear scalar operations.** At constant precision the
   scalar domain is finite. Product, exponentiation, division, comparison,
   and ReLU are constant-size lookup tables (London–Kanade Lem. C.4).
3. **Polynomial-fan-in sums.** Saturating iterated addition of
   constant-precision values is recognized by a counter-free automaton and
   therefore has an FO[<], hence DLOGTIME-uniform AC⁰, implementation
   (London–Kanade Lem. C.3 and its uniformity remark).
4. **Attention.** Every query–key score is a polynomial-fan-in sum of
   finite-table products. Exponentiation is a finite table; the softmax
   normalizer and value aggregation use the preceding iterated-sum circuit;
   final division is a finite table. Each output coordinate is therefore in
   L-uniform AC⁰. For AHAT, maximum/tie selection over a finite score alphabet
   is an equivalent finite set of threshold/equality cases followed by the
   same sum/average primitives.
5. **Feedforward and residual.** Affine maps use the same product/sum
   primitives; ReLU is a finite comparison table; residual addition is
   constant precision. These stay in L-uniform AC⁰.
6. **Composition.** The transformer has constant depth, so fixed serial
   composition preserves constant depth and polynomial size.

Hence `LPT⁰_{c,D}⊆L-uniform AC⁰`. Together with the lower inclusion,
extensionality gives Claim 1.

## Claim 2: log precision equals L-uniform TC⁰

We prove

```text
L-uniform TC⁰ ⊆ L-uniform LPT⁰_{l,D} ⊆ L-uniform TC⁰.
```

### Sufficient volume

Here `b(N)=Θ(log N)`. Even `D(N)=Θ(1)` gives
`D(N)b(N)=Θ(log N)`, so the volume floor imposes no growing-width
requirement. “Regardless of width” means every admissible asymptotic width
regime at least as large as the fixed constant construction and at most
polynomial, not a literal claim that zero coordinates suffice.

### Lower inclusion and the printed defect

London–Kanade Theorem C.7 gives a log-width TC⁰ simulation. Svete et al.
replace binary pointer blocks with two-dimensional unit PEs. Their Lemma B.4
proves, for every distinct `n,n'` and sufficiently large `N`, a rounded
inner-product gap of at least `1/(4N⁴)` when `b≥5log N`. Corollary B.1 scales
that gap, and Lemma B.5 turns it into exact 0/1 fixed-point softmax weights at
`b≥6log N`.

The routing sentence printed in Lemma 4.1 does not follow from those lemmas.
It assigns an argument’s first target to its source and a token’s second
target to itself, then says layer 2 swaps query/key roles. For a gate `g` and
argument sourced at `s`, that swap compares `μ(g)` with `μ(s)`; it selects the
argument only in the accidental case `g=s`. The fail-closed control therefore
rejects the printed projection.

The following replacement keeps constant width and supplies the two relations
the circuit simulation actually needs. Each token stores three two-dimensional
fields:

```text
self  = μ(its own sequence position)
source = μ(source position), on an argument token
gate   = μ(destination gate position), on an argument token
```

- **Layer 1 (copy a source to an argument):** an argument queries `source`;
  every token exposes `self` as key. Lemmas B.4/B.5 select exactly the token
  whose `self=source`.
- **Layer 2 (collect arguments at a gate):** a gate queries `self`; every
  argument exposes `gate` as key. Exactly the arguments satisfying
  `argument.gate=gate.self` tie at the maximum, so attention averages all and
  only the inputs of that gate.

There are six pointer coordinates independent of `N`. Circuit-type flags,
one value coordinate, and the fixed MLP scratch block are also constant, so
the repaired residual width is `O(1)`. The PE generator obtains source/gate
indices from the L-uniform circuit description and computes `μ` in logspace,
as required by Definition A.5.

### Gate computation and induction

For a threshold gate with arity `h`, source bits `v_j`, and integer threshold
`k`, the second layer returns their average. The PE stores `k/h`. Since
`h>0`, exact cross multiplication gives

```text
(Σ_j v_j)/h > k/h  iff  Σ_j v_j > k,
(Σ_j v_j)/h < k/h  iff  Σ_j v_j < k.
```

The position-wise feedforward step in London–Kanade Eqs. (25)–(29) therefore
recovers the positive- or negative-direction threshold bit exactly and clears
argument scratch values. Base case: input tokens contain the input bits.
Inductive step: if all previous circuit levels are correct, layer 1 copies
their values to every outgoing argument, and layer 2 plus the MLP computes all
gates on the next level. A TC⁰ family has constant circuit depth, so two
transformer layers per level are still constant depth. It has polynomial size,
so its gate/edge tokens require only polynomial padding. This proves the
repaired universal lower inclusion for every L-uniform TC⁰ circuit family.

Any larger admissible width embeds the fixed construction using the exact
zero-coordinate lift already derived for Claim 1.

### Upper inclusion, expanded

Fix an arbitrary `LPT⁰_{l,D}` family. Log precision is a special case of the
polynomial-precision, polynomial-width family in Lemma 4.2.

1. Parameter and PE bits are hardwired by the logspace uniformity generator.
2. A score is an inner product of polynomially many polynomial-bit numbers.
   Uniform TC⁰ contains multiplication and iterated addition (the arithmetic
   results imported in Lemma 4.2).
3. Fixed-point exponential to polynomial precision is reduced to a truncated
   arithmetic circuit; normalization uses iterated addition and division.
4. Value aggregation and affine/ReLU layers use the same TC⁰ primitives.
5. For AHAT, maximum, equality, counting tied maxima, addition, and division
   are in L-uniform TC⁰.
6. A fixed number of transformer layers is a fixed serial composition of
   constant-depth polynomial-size threshold circuits, hence remains TC⁰.

Thus `LPT⁰_{l,D}⊆L-uniform TC⁰`. Combining it with the repaired lower
inclusion proves Claim 2.

## Fail-closed boundary

- The proof does **not** infer an asymptotic theorem from the 79 routing cases,
  the `N≤4096` volume table, or any other finite experiment.
- The executable obligation ledger accepts imported results only with a
  pinned primary source and exact anchors.
- A derived obligation cannot close unless all of its premises have already
  closed and a named checker runs.
- The printed two-field layer-2 route is recorded as false. Only the explicit
  three-field repair is used in the Claim 2 sandwich.
- The conclusions are conditional on the paper’s fixed-point semantics,
  L-uniformity definition, polynomial padding/width, constant depth, and the
  imported standard uniform-circuit arithmetic theorems.

## Reproduction commands

```bash
PYTHONPATH=repro .venv/bin/python repro/run_theorem42_obligations.py
PYTHONPATH=repro .venv/bin/python -m pytest -q repro/tests
```

The generated `outputs/theorem42_obligations.json` contains the source pins,
quantifiers, premises, derivations, check results, and closure state for every
obligation in both sandwiches.
