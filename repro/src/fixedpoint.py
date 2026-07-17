"""Finite fixed-point AHAT/SMAT construction from Lemma 3.1.

The paper's construction chooses a sufficiently small, length-dependent
temperature, performs the softmax sub-layer at a constant-factor higher
precision, and rounds the residual stream back to b bits.  This module
implements that construction directly for finite score/value tables.
"""

from __future__ import annotations

from typing import Iterable

import numpy as np


def quantize(values: np.ndarray, bits: int) -> np.ndarray:
    """Round to the signed b-integer/b-fractional fixed-point grid F_b."""
    if bits < 1:
        raise ValueError("bits must be positive")
    scale = 2**bits
    limit = 2 ** (2 * bits) - 1
    integers = np.clip(np.rint(np.asarray(values, dtype=float) * scale), -limit, limit)
    return integers / scale


def exact_temperature(length: int, bits: int) -> float:
    """A conservative dyadic temperature satisfying the Lemma-3.1 margin.

    Distinct F_b scores are separated by at least 2^-b.  This choice drives a
    non-maximal contribution far below half an F_b unit even after summing all
    length positions.  Dyadic temperatures are exactly representable.
    """
    if length < 2:
        raise ValueError("attention length must be at least two")
    return 2.0 ** (-(2 * bits + int(np.ceil(np.log2(length))) + 6))


def average_hard_attention(scores: np.ndarray, values: np.ndarray, bits: int) -> np.ndarray:
    """AHAT: uniformly average all maximum-score values then round to F_b."""
    scores = quantize(scores, bits)
    values = quantize(values, bits)
    maxima = np.max(scores, axis=1, keepdims=True)
    mask = scores == maxima
    weights = mask / np.sum(mask, axis=1, keepdims=True)
    return quantize(weights @ values, bits)


def softmax_attention(scores: np.ndarray, values: np.ndarray, bits: int, temperature: float) -> np.ndarray:
    """SMAT with stable high-precision internal arithmetic then F_b rounding."""
    scores = quantize(scores, bits)
    values = quantize(values, bits)
    shifted = (scores - np.max(scores, axis=1, keepdims=True)) / temperature
    # All exponents are non-positive after the stable shift.  Underflow means
    # a contribution is below double precision and therefore below the stated
    # fixed-point rounding margin as well.
    exponentials = np.exp(np.maximum(shifted, -745.0))
    weights = exponentials / np.sum(exponentials, axis=1, keepdims=True)
    return quantize(weights @ values, bits)


def score_value_cases(length: int, bits: int, seeds: int = 48) -> Iterable[tuple[np.ndarray, np.ndarray]]:
    """Deterministic tie, minimum-gap, and arbitrary fixed-point attention cases."""
    scale = 2**bits
    values = np.column_stack(
        (
            np.linspace(-0.75, 0.75, length),
            np.linspace(0.625, -0.625, length),
        )
    )
    # Explicit ties and minimum F_b gaps exercise the two cases in the proof.
    base = np.arange(length, dtype=float) / scale
    yield np.vstack((base, base[::-1])), values
    tied = np.zeros((2, length), dtype=float)
    tied[0, : max(2, length // 2)] = 1.0
    tied[1, ::2] = 0.5
    yield tied, values
    for seed in range(seeds):
        rng = np.random.default_rng(10_000 * bits + 100 * length + seed)
        scores = rng.integers(-3 * scale, 3 * scale + 1, size=(3, length)) / scale
        # Guarantee at least one tie in every batch, including a full row tie.
        scores[0, 0] = scores[0, 1]
        scores[1, :] = scores[1, 0]
        random_values = rng.integers(-scale, scale + 1, size=(length, 2)) / scale
        yield scores, random_values


def lemma31_audit() -> dict[str, object]:
    """Check exact rounded AHAT/SMAT agreement over all construction cases."""
    cases = 0
    max_pre_round_difference = 0.0
    for bits in (3, 4, 6, 8):
        for length in (2, 4, 8, 16):
            temperature = exact_temperature(length, bits)
            for scores, values in score_value_cases(length, bits):
                ahat = average_hard_attention(scores, values, bits)
                smat = softmax_attention(scores, values, bits, temperature)
                max_pre_round_difference = max(
                    max_pre_round_difference,
                    float(np.max(np.abs(ahat - smat))),
                )
                if not np.array_equal(ahat, smat):
                    raise AssertionError(f"Lemma-3.1 mismatch at b={bits}, N={length}")
                cases += 1

    # A deliberately non-focusing temperature is a fail-closed control: it
    # must not be credited as an exact AHAT simulator.
    scores = np.array([[0.0, 1.0]])
    values = np.array([[0.0], [1.0]])
    ahat = average_hard_attention(scores, values, bits=5)
    loose = softmax_attention(scores, values, bits=5, temperature=1.0)
    assert not np.array_equal(ahat, loose)
    return {
        "fixed_point_cases": cases,
        "max_post_round_difference": max_pre_round_difference,
        "negative_control_loose_temperature_difference": float(np.max(np.abs(ahat - loose))),
    }

