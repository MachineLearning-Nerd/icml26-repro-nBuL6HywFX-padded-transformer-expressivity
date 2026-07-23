"""Claim-level proof-instance audits for arXiv:2605.30523."""

from __future__ import annotations

from .circuits import loop_audit, precision_divide_audit
from .fixedpoint import lemma31_audit
from .theorem42 import theorem42_audit
from .volume import volume_audit


def source_scope_audit() -> dict[str, object]:
    """Record the primary-source scope check for the theory-only fifth claim."""
    return {
        "primary_pdf_sha256": "fbc31ec9024e20bef85e4e12a262991f098c093d171d6063d57bcf62419b562b",
        "source_sections": [
            "2. Preliminaries",
            "3. SMATs Can Simulate AHATs",
            "4. Padded Constant-depth Transformers Are Constant-depth Circuits",
            "5. Looped Padded Transformers Are Highly Uniform Growing-depth Circuits",
            "6. Discussion",
            "A--C formal definitions and proofs",
        ],
        "empirical_benchmark_or_training_protocol": False,
        "interpretation": "The paper is a theoretical characterization; its claims are theorem/proof claims rather than dataset, training, or benchmark results.",
    }


def run_all() -> dict[str, object]:
    """Run all five claim-audit components."""
    volume = volume_audit()
    attention = lemma31_audit()
    loops = loop_audit()
    precision = precision_divide_audit()
    theorem42 = theorem42_audit()
    scope = source_scope_audit()
    return {
        "paper": {"arxiv": "2605.30523", "openreview": "nBuL6HywFX"},
        "claim_1_constant_depth_AC0_TC0_equivalence": {
            "finite_circuit_resource_witness": precision,
            "sufficient_volume_configurations": volume,
            "scope": "Finite proof-instance checks support the constructions and resource boundary; the universal class equalities remain established by the cited paper proofs.",
        },
        "claim_2_volume_is_D_times_b": volume,
        "claim_3_looped_ACd_TCd_equivalence": loops,
        "claim_4_log_precision_SMAT_simulates_AHAT": attention,
        "claim_5_theory_only_scope": scope,
        "current_challenge_claims_theorem_4_2": theorem42,
    }
