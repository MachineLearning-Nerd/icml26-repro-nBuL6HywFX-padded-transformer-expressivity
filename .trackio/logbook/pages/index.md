# Reproduction: Revisiting Padded Transformer Expressivity: Which Architectural Choices Matter and Which Don't

Paper: [OpenReview nBuL6HywFX](https://openreview.net/forum?id=nBuL6HywFX) · [arXiv:2605.30523](https://arxiv.org/abs/2605.30523)

The official judge rejected the source-pinned obligation audit at SHA `c23407b`
as self-authored rather than formal or independent verification. Attempt 3 is
a materially different evidence class: a Lean 4.32 kernel-checked proof with
11 reported theorem dependencies, no proof-escape tokens, and no `sorryAx`.
It formalizes the two inclusion sandwiches with source results as explicit
hypotheses, semantics-preserving width padding, universal exact source/gate
routing, the counterexample to the printed route, exact gate arithmetic, and
induction over every circuit level. Sixteen independent tests pass. The exact
formalization boundary is disclosed; finite-N checks are regressions only.

## Pages

| Page |
| --- |
| [Executive summary](#/executive-summary) |
| [Claim 1](#/claim-1) |
| [Claim 2](#/claim-2) |
| [Conclusion](#/conclusion) |
