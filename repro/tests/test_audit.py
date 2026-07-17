from __future__ import annotations

from src.audit import run_all
from src.circuits import deterministic_map, loop_audit, precision_divide_audit, table_composition
from src.fixedpoint import (
    average_hard_attention,
    exact_temperature,
    lemma31_audit,
    softmax_attention,
)
from src.volume import decode_position, encode_position, sufficient_volume, volume_audit


def test_lemma31_fixed_point_simulation_matches_exactly_after_rounding():
    result = lemma31_audit()
    assert result["fixed_point_cases"] == 800
    assert result["max_post_round_difference"] == 0.0
    assert result["negative_control_loose_temperature_difference"] > 0.1


def test_tie_case_is_preserved_by_focusing_softmax():
    scores = [[1.0, 1.0, 0.0, -1.0]]
    values = [[0.0], [1.0], [-1.0], [0.25]]
    ahat = average_hard_attention(scores, values, 6)
    smat = softmax_attention(scores, values, 6, exact_temperature(4, 6))
    assert (ahat == smat).all()
    assert ahat[0, 0] == 0.5


def test_volume_boundary_is_exact_for_injective_position_codes():
    assert sufficient_volume(256, 1, 8)
    assert not sufficient_volume(256, 1, 7)
    code = encode_position(255, 2, 4)
    assert decode_position(code, 4) == 255
    assert volume_audit()["positions_checked"] > 5_000


def test_looped_circuit_table_agrees_with_direct_iteration():
    circuit = deterministic_map(width=5, depth=2, thresholds=True)
    table = table_composition(circuit, loops=9)
    assert all(circuit.iterated(bits, 9) == value for bits, value in table.items())


def test_polylog_loop_audit_covers_AC_and_TC_gate_sets():
    result = loop_audit()
    assert result["AC_and_TC_maps"] == 54
    assert result["exhaustive_input_loop_checks"] > 3_000


def test_log_precision_retains_all_threshold_counts_where_constant_precision_cannot():
    rows = precision_divide_audit()["threshold_count_capacity_rows"]
    assert all(row["log_b_can_retain_count"] for row in rows)
    assert any(not row["constant_b_can_retain_count"] for row in rows)


def test_top_level_claim_record_is_complete():
    report = run_all()
    assert set(report).issuperset(
        {
            "claim_1_constant_depth_AC0_TC0_equivalence",
            "claim_2_volume_is_D_times_b",
            "claim_3_looped_ACd_TCd_equivalence",
            "claim_4_log_precision_SMAT_simulates_AHAT",
            "claim_5_theory_only_scope",
        }
    )
