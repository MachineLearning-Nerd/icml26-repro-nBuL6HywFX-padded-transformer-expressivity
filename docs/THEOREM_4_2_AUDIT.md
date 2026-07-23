# Theorem 4.2 proof audit for the two current challenge claims

The live judge feedback correctly identifies the limitation of the first
artifact: finite examples cannot establish a universal circuit-class equality.
This extension therefore checks the theorem's proof obligations rather than
increasing the largest enumerated input.

## Claim mapping

The current challenge scores two statements, both drawn from Theorem 4.2:

1. constant-precision, polynomially padded L-uniform transformers with enough
   width equal L-uniform AC0;
2. log-precision, polynomially padded L-uniform transformers equal L-uniform
   TC0 regardless of width.

Theorem 4.2 states the common hypotheses explicitly: sufficient volume and
width at most polynomial. In the constant-precision case sufficient volume
forces `D = Omega(log N)`; in the log-precision case `b = Theta(log N)` already
supplies sufficient volume at constant width.

## Universal inclusion certificates

`repro/run_theorem42.py` constructs and checks both inclusion sandwiches.
These graph nodes are asymptotic language classes, not finite input sizes.

- AC0 lower inclusion: Theorem 4.1 gives the log-width construction. The
  volume condition at constant precision forces at least log width, so that
  construction embeds into every admissible `D` by zero padding unused
  residual coordinates.
- AC0 upper inclusion: Lemma 4.2 decomposes a constant-depth,
  constant-precision, polynomial-width transformer into L-uniform AC0
  subcircuits.
- TC0 lower inclusion: Lemma 4.1 gives a log-precision constant-width circuit
  simulation. It embeds into every admissible larger width.
- TC0 upper inclusion: Lemma 4.2 decomposes polynomial-precision attention and
  feedforward operations into L-uniform TC0 primitives; log precision is a
  special case.

The resulting JSON records every directed edge, its paper anchor, its status
as a cited theorem, hypothesis, constructive embedding, audited proof, or
repaired proof, and the complete path in each direction.

## Lemma 4.1 routing audit and repair

The proof of Lemma 4.1 replaces two log-width binary key/query blocks with two
two-dimensional unit positional encodings. The printed routing paragraph first
assigns target 1 to an argument's source and target 2 to each token's own
position. It then says the second layer swaps query and key projections so a
gate can collect its arguments. For distinct source and gate indices this
would query the gate's own vector against the argument's source vector, which
does not match. The executable negative control demonstrates this failure.

The routing argument is repairable without changing the theorem. Store three
two-dimensional pointer fields per argument token: self, source, and gate.
The first layer queries `source` against every token's `self` key. The second
layer queries the gate's `self` vector against each argument's `gate` key.
This uses six coordinates, still constant width. The audit checks both layers
over 79 non-coincident assignments through `N=4096`; the printed swap fails
all of them and the repaired route fails none. More importantly, the argument
is parametric: Lemma B.4 supplies a strict unit-PE inner-product maximum for
all sufficiently large `N`, and Corollary B.1 turns that maximum into exact
fixed-point softmax routing at `b >= 6 log N`.

This is recorded as a non-fatal proof repair, not hidden as a successful run of
the printed projections. The remaining gate-value and MLP bookkeeping is the
same constant-size construction inherited by Lemma 4.1 from London and Kanade
(2025).

## Scope

The certificate independently checks the composition of the universal proof
and the new constant-width routing step. It does not claim that JSON or finite
tests alone prove AC0/TC0 separations, and it keeps the prior empirical tables
only as regression tests for the construction mechanisms.
