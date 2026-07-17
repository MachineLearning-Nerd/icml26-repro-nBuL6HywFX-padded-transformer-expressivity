"""Volume and positional-code checks for Definitions 2.2--2.3."""

from __future__ import annotations

import math


def required_bits(length: int) -> int:
    return max(1, math.ceil(math.log2(length)))


def encode_position(position: int, width: int, precision: int) -> tuple[int, ...]:
    """Encode one of N positions in D symbols of b bits, least-significant first."""
    if position < 0 or position >= 2 ** (width * precision):
        raise ValueError("position exceeds the D*b-bit positional code space")
    mask = 2**precision - 1
    return tuple((position >> (precision * coordinate)) & mask for coordinate in range(width))


def decode_position(code: tuple[int, ...], precision: int) -> int:
    return sum(symbol << (precision * coordinate) for coordinate, symbol in enumerate(code))


def sufficient_volume(length: int, width: int, precision: int) -> bool:
    return width * precision >= required_bits(length)


def volume_audit() -> dict[str, object]:
    """Exhaustively test the information-theoretic sufficient-volume boundary."""
    cases = []
    positions_checked = 0
    for length in (2, 4, 8, 16, 64, 256, 1024, 4096):
        need = required_bits(length)
        configurations = [
            (1, need),  # log precision, constant width
            (need, 1),  # constant precision, growing width
            (max(1, math.ceil(need / 3)), 3),
            (1, max(1, need - 1)),  # intentionally insufficient
        ]
        for width, precision in configurations:
            predicted = sufficient_volume(length, width, precision)
            capacity = 2 ** (width * precision)
            actual = capacity >= length
            assert predicted == actual
            if actual:
                codes = {encode_position(position, width, precision) for position in range(length)}
                assert len(codes) == length
                assert all(decode_position(code, precision) < length for code in codes)
                positions_checked += length
            cases.append(
                {
                    "N": length,
                    "D": width,
                    "b": precision,
                    "volume": width * precision,
                    "required_log2_N": need,
                    "injective_position_encoding": actual,
                }
            )
    return {"configurations": cases, "positions_checked": positions_checked}

