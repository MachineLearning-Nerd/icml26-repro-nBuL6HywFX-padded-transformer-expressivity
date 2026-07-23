# Lean 4 kernel proof

This directory contains a Lean 4 formalization of the new, universal parts of
the Theorem 4.2 audit. It uses only the official `Std` library bundled with the
pinned compiler.

- `PaddedTransformer.lean` contains no `sorry`, `admit`, or custom axioms.
- Source-paper inclusions are explicit theorem parameters, never silently
  promoted from finite experiments.
- Positional focusing and both repaired routing layers are proved for an
  arbitrary position type and arbitrary strictly-focused score function.
- The printed layer-2 source/gate mismatch is rejected universally whenever
  source and destination differ.
- Width padding, threshold cross-multiplication, inclusion sandwiches, and
  level induction are kernel checked.

Use the pinned Lean toolchain:

```bash
lean formal/PaddedTransformer.lean
```

The `#print axioms` output reports the exact kernel dependencies of every key
theorem. The verification gate rejects `sorryAx`; standard logical primitives
used by bundled library results are reported transparently.
