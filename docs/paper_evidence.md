# Primary source and method map

Primary source: `https://arxiv.org/pdf/2605.30523`, downloaded 2026-07-17.

```text
SHA-256 fbc31ec9024e20bef85e4e12a262991f098c093d171d6063d57bcf62419b562b
```

| Challenge claim | Paper source | Executable audit |
|---|---|---|
| C1 | Theorem 4.2, Lemmas 4.1–4.2 | Test the finite sufficient-volume boundary and the Boolean-versus-threshold resource witnesses underlying the AC⁰/TC⁰ divide. |
| C2 | Definitions 2.2–2.3 | Encode every position in the complete finite range with `D` symbols of `b` bits and check injectivity exactly iff `D·b≥⌈log₂N⌉`. |
| C3 | Theorem 5.1, Lemma 5.1 | Construct deterministic uniform AND/OR/NOT and threshold maps; compare direct repeated execution to an independently composed full truth table for `r=⌈log₂(width+1)⌉^d`. |
| C4 | Lemma 3.1 and proof equations (31)–(36) | Quantize scores and residuals to `F_b`; compare average-hard attention with dyadic-temperature SMAT after rounding, including ties and the minimum score gap `2^-b`. |
| C5 | Sections 2–6 and Appendices A–C | Source-scope audit: the paper presents definitions, constructions, lemmas, theorems, discussion, and proofs, with no experiment/data/training section. |

## Exactness and negative controls

The fixed-point construction deliberately quantizes scores, values, and final
residuals.  `exact_temperature(N,b)` is a conservative dyadic form of the
temperature margin in the Lemma 3.1 proof.  Every high-precision SMAT output
rounds to precisely the AHAT output in 800 cases.  The same pair at
temperature 1 does **not** round to the AHAT output, so the audit fails closed
if the focusing requirement is omitted.

The volume check is an exact finite information statement, not a claim that
finite code counting proves the asymptotic circuit theorem.  Likewise, the
loop audit verifies the `f^r` depth-composition mechanism in Lemma 5.1 rather
than attempting to enumerate an infinite circuit class.

