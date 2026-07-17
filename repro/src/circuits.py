"""Uniform layered Boolean/threshold circuits and loop-composition checks."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

import numpy as np


@dataclass(frozen=True)
class Gate:
    kind: str
    inputs: tuple[int, ...]
    threshold: int = 0


@dataclass(frozen=True)
class LayeredMap:
    width: int
    layers: tuple[tuple[Gate, ...], ...]

    @property
    def depth(self) -> int:
        return len(self.layers)

    def apply(self, bits: tuple[int, ...]) -> tuple[int, ...]:
        current = tuple(int(bit) for bit in bits)
        if len(current) != self.width:
            raise ValueError("input width mismatch")
        for layer in self.layers:
            next_values = []
            for gate in layer:
                selected = [current[index] for index in gate.inputs]
                if gate.kind == "AND":
                    next_values.append(int(all(selected)))
                elif gate.kind == "OR":
                    next_values.append(int(any(selected)))
                elif gate.kind == "NOT":
                    next_values.append(1 - selected[0])
                elif gate.kind == "THR":
                    next_values.append(int(sum(selected) >= gate.threshold))
                else:
                    raise ValueError(f"unknown gate type {gate.kind}")
            current = tuple(next_values)
        return current

    def iterated(self, bits: tuple[int, ...], loops: int) -> tuple[int, ...]:
        result = bits
        for _ in range(loops):
            result = self.apply(result)
        return result


def deterministic_map(width: int, depth: int, thresholds: bool) -> LayeredMap:
    """A logspace-describable indexed circuit family with width-preserving layers."""
    layers = []
    for layer_index in range(depth):
        layer = []
        for output in range(width):
            inputs = tuple((output + shift + layer_index) % width for shift in range(3))
            if thresholds and output % 4 == 0:
                layer.append(Gate("THR", inputs, threshold=2))
            elif output % 3 == 0:
                layer.append(Gate("AND", inputs))
            elif output % 3 == 1:
                layer.append(Gate("OR", inputs))
            else:
                layer.append(Gate("NOT", (inputs[0],)))
        layers.append(tuple(layer))
    return LayeredMap(width=width, layers=tuple(layers))


def table_composition(reference: LayeredMap, loops: int) -> dict[tuple[int, ...], tuple[int, ...]]:
    """Independent truth-table composition of a looped map."""
    domain = list(product((0, 1), repeat=reference.width))
    one_step = {entry: reference.apply(entry) for entry in domain}
    table = dict(one_step)
    for _ in range(1, loops):
        table = {entry: one_step[table[entry]] for entry in domain}
    return table


def loop_audit() -> dict[str, object]:
    """Audit Lemma 5.1's f^r depth composition for AC and TC gate sets."""
    exhaustive_inputs = 0
    map_checks = 0
    maximum_depth = 0
    for thresholds in (False, True):
        for width in (3, 5, 7):
            for base_depth in (1, 2, 3):
                circuit = deterministic_map(width, base_depth, thresholds)
                for exponent in (1, 2, 3):
                    loops = int(np.ceil(np.log2(width + 1))) ** exponent
                    composed = table_composition(circuit, loops)
                    for bits, expected in composed.items():
                        assert circuit.iterated(bits, loops) == expected
                        exhaustive_inputs += 1
                    maximum_depth = max(maximum_depth, loops * base_depth)
                    map_checks += 1
    return {
        "AC_and_TC_maps": map_checks,
        "exhaustive_input_loop_checks": exhaustive_inputs,
        "maximum_composed_depth": maximum_depth,
    }


def precision_divide_audit() -> dict[str, object]:
    """Finite resource witness for the AC/TC precision divide in Theorem 4.2.

    A threshold gate needs enough numeric range to retain an exact count.  The
    check is deliberately a resource witness, not a claim to prove the
    asymptotic circuit separation by enumeration.
    """
    rows = []
    for width in (8, 16, 32, 64, 128):
        constant_precision = 3
        log_precision = int(np.ceil(np.log2(width + 1))) + 1
        rows.append(
            {
                "fan_in": width,
                "constant_b": constant_precision,
                "constant_b_exact_count_capacity": 2**constant_precision - 1,
                "log_b": log_precision,
                "log_b_exact_count_capacity": 2**log_precision - 1,
                "constant_b_can_retain_count": width <= 2**constant_precision - 1,
                "log_b_can_retain_count": width <= 2**log_precision - 1,
            }
        )
    assert any(not row["constant_b_can_retain_count"] for row in rows)
    assert all(row["log_b_can_retain_count"] for row in rows)
    return {"threshold_count_capacity_rows": rows}

