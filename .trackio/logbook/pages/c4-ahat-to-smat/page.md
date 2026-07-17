# C4 — AHAT to SMAT


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_39158d617d77", "created_at": "2026-07-17T09:10:51+00:00", "title": "Lemma 3.1 replaces AHAT with a sufficiently low-temperature SMAT and relies on…"}
-->
Lemma 3.1 replaces AHAT with a sufficiently low-temperature SMAT and relies on fixed-point rounding to produce exact residual agreement. Scores/values are quantized to F_b; the audit covers ties, the minimum 2^-b score gap, and deterministic random tables. Every low-temperature output equals AHAT exactly after rounding; temperature 1 fails closed.


---
<!-- trackio-cell
{"type": "code", "id": "cell_92ef6707e85a", "created_at": "2026-07-17T09:10:57+00:00", "title": "Full clean-room proof-instance audit", "command": ["env", "PYTHONPATH=repro", "python", "repro/run_audit.py"], "exit_code": 0, "duration_s": 1.12}
-->
````bash
$ env PYTHONPATH=repro python repro/run_audit.py
````

exit 0 · 1.1s


````python title=run_audit.py
#!/usr/bin/env python3
"""Run the padded-transformer proof-instance audit."""

from __future__ import annotations

import json
from pathlib import Path

from src.audit import run_all


if __name__ == "__main__":
    report = run_all()
    root = Path(__file__).resolve().parents[1]
    target = root / "outputs" / "summary.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))


````


````output
{
  "paper": {
    "arxiv": "2605.30523",
    "openreview": "nBuL6HywFX"
  },
  "claim_1_constant_depth_AC0_TC0_equivalence": {
    "finite_circuit_resource_witness": {
      "threshold_count_capacity_rows": [
        {
          "fan_in": 8,
          "constant_b": 3,
          "constant_b_exact_count_capacity": 7,
          "log_b": 5,
          "log_b_exact_count_capacity": 31,
          "constant_b_can_retain_count": false,
          "log_b_can_retain_count": true
        },
        {
          "fan_in": 16,
          "constant_b": 3,
          "constant_b_exact_count_capacity": 7,
          "log_b": 6,
          "log_b_exact_count_capacity": 63,
          "constant_b_can_retain_count": false,
          "log_b_can_retain_count": true
        },
        {
          "fan_in": 32,
          "constant_b": 3,
          "constant_b_exact_count_capacity": 7,
          "log_b": 7,
          "log_b_exact_count_capacity": 127,
          "constant_b_can_retain_count": false,
          "log_b_can_retain_count": true
        },
        {
          "fan_in": 64,
          "constant_b": 3,
          "constant_b_exact_count_capacity": 7,
          "log_b": 8,
          "log_b_exact_count_capacity": 255,
          "constant_b_can_retain_count": false,
          "log_b_can_retain_count": true
        },
        {
          "fan_in": 128,
          "constant_b": 3,
          "constant_b_exact_count_capacity": 7,
          "log_b": 9,
          "log_b_exact_count_capacity": 511,
          "constant_b_can_retain_count": false,
          "log_b_can_retain_count": true
        }
      ]
    },
    "sufficient_volume_configurations": {
      "configurations": [
        {
          "N": 2,
          "D": 1,
          "b": 1,
          "volume": 1,
          "required_log2_N": 1,
          "injective_position_encoding": true
        },
        {
          "N": 2,
          "D": 1,
          "b": 1,
          "volume": 1,
          "required_log2_N": 1,
          "injective_position_encoding": true
        },
        {
          "N": 2,
          "D": 1,
          "b": 3,
          "volume": 3,
          "required_log2_N": 1,
          "injective_position_encoding": true
        },
        {
          "N": 2,
          "D": 1,
          "b": 1,
          "volume": 1,
          "required_log2_N": 1,
          "injective_position_encoding": true
        },
        {
          "N": 4,
          "D": 1,
          "b": 2,
          "volume": 2,
          "required_log2_N": 2,
          "injective_position_encoding": true
        },
        {
          "N": 4,
          "D": 2,
          "b": 1,
          "volume": 2,
          "required_log2_N": 2,
          "injective_position_encoding": true
        },
        {
          "N": 4,
          "D": 1,
          "b": 3,
          "volume": 3,
          "required_log2_N": 2,
          "injective_position_encoding": true
        },
        {
          "N": 4,
          "D": 1,
          "b": 1,
          "volume": 1,
          "required_log2_N": 2,
          "injective_position_encoding": false
        },
        {
          "N": 8,
          "D": 1,
          "b": 3,
          "volume": 3,
          "required_log2_N": 3,
          "injective_position_encoding": true
        },
        {
          "N": 8,
          "D": 3,
          "b": 1,
          "volume": 3,
          "required_log2_N": 3,
          "injective_position_encoding": true
        },
        {
          "N": 8,
          "D": 1,
          "b": 3,
          "volume": 3,
          "required_log2_N": 3,
          "injective_position_encoding": true
        },
        {
          "N": 8,
          "D": 1,
          "b": 2,
          "volume": 2,
          "required_log2_N": 3,
          "injective_position_encoding": false
        },
        {
          "N": 16,
          "D": 1,
          "b": 4,
          "volume": 4,
          "required_log2_N": 4,
          "injective_position_encoding": true
        },
        {
          "N": 16,
          "D": 4,
          "b": 1,
          "volume": 4,
          "required_log2_N": 4,
          "injective_position_encoding": true
        },
        {
          "N": 16,
          "D": 2,
          "b": 3,
          "volume": 6,
          "required_log2_N": 4,
          "injective_position_encoding": true
        },
        {
          "N": 16,
          "D": 1,
          "b": 3,
          "volume": 3,
          "required_log2_N": 4,
          "injective_position_encoding": false
        },
        {
          "N": 64,
          "D": 1,
          "b": 6,
          "volume": 6,
          "required_log2_N": 6,
          "injective_position_encoding": true
        },
        {
          "N": 64,
          "D": 6,
          "b": 1,
          "volume": 6,
          "required_log2_N": 6,
          "injective_position_encoding": true
        },
        {
          "N": 64,
          "D": 2,
          "b": 3,
          "volume": 6,
          "required_log2_N": 6,
          "injective_position_encoding": true
        },
        {
          "N": 64,
          "D": 1,
          "b": 5,
          "volume": 5,
          "required_log2_N": 6,
          "injective_position_encoding": false
        },
        {
          "N": 256,
          "D": 1,
          "b": 8,
          "volume": 8,
          "required_log2_N": 8,
          "injective_position_encoding": true
        },
        {
          "N": 256,
          "D": 8,
          "b": 1,
          "volume": 8,
          "required_log2_N": 8,
          "injective_position_encoding": true
        },
        {
          "N": 256,
          "D": 3,
          "b": 3,
          "volume": 9,
          "required_log2_N": 8,
          "injective_position_encoding": true
        },
        {
          "N": 256,
          "D": 1,
          "b": 7,
          "volume": 7,
          "required_log2_N": 8,
          "injective_position_encoding": false
        },
        {
          "N": 1024,
          "D": 1,
          "b": 10,
          "volume": 10,
          "required_log2_N": 10,
          "injective_position_encoding": true
        },
        {
          "N": 1024,
          "D": 10,
          "b": 1,
          "volume": 10,
          "required_log2_N": 10,
          "injective_position_encoding": true
        },
        {
          "N": 1024,
          "D": 4,
          "b": 3,
          "volume": 12,
          "required_log2_N": 10,
          "injective_position_encoding": true
        },
        {
          "N": 1024,
          "D": 1,
          "b": 9,
          "volume": 9,
          "required_log2_N": 10,
          "injective_position_encoding": false
        },
        {
          "N": 4096,
          "D": 1,
          "b": 12,
          "volume": 12,
          "required_log2_N": 12,
          "injective_position_encoding": true
        },
        {
          "N": 4096,
          "D": 12,
          "b": 1,
          "volume": 12,
          "required_log2_N": 12,
          "injective_position_encoding": true
        },
        {
          "N": 4096,
          "D": 4,
          "b": 3,
          "volume": 12,
          "required_log2_N": 12,
          "injective_position_encoding": true
        },
        {
          "N": 4096,
          "D": 1,
          "b": 11,
          "volume": 11,
          "required_log2_N": 12,
          "injective_position_encoding": false
        }
      ],
      "positions_checked": 16412
    },
    "scope": "Finite proof-instance checks support the constructions and resource boundary; the universal class equalities remain established by the cited paper proofs."
  },
  "claim_2_volume_is_D_times_b": {
    "configurations": [
      {
        "N": 2,
        "D": 1,
        "b": 1,
        "volume": 1,
        "required_log2_N": 1,
        "injective_position_encoding": true
      },
      {
        "N": 2,
        "D": 1,
        "b": 1,
        "volume": 1,
        "required_log2_N": 1,
        "injective_position_encoding": true
      },
      {
        "N": 2,
        "D": 1,
        "b": 3,
        "volume": 3,
        "required_log2_N": 1,
        "injective_position_encoding": true
      },
      {
        "N": 2,
        "D": 1,
        "b": 1,
        "volume": 1,
        "required_log2_N": 1,
        "injective_position_encoding": true
      },
      {
        "N": 4,
        "D": 1,
        "b": 2,
        "volume": 2,
        "required_log2_N": 2,
        "injective_position_encoding": true
      },
      {
        "N": 4,
        "D": 2,
        "b": 1,
        "volume": 2,
        "required_log2_N": 2,
        "injective_position_encoding": true
      },
      {
        "N": 4,
        "D": 1,
        "b": 3,
        "volume": 3,
        "required_log2_N": 2,
        "injective_position_encoding": true
      },
      {
        "N": 4,
        "D": 1,
        "b": 1,
        "volume": 1,
        "required_log2_N": 2,
        "injective_position_encoding": false
      },
      {
        "N": 8,
        "D": 1,
        "b": 3,
        "volume": 3,
        "required_log2_N": 3,
        "injective_position_encoding": true
      },
      {
        "N": 8,
        "D": 3,
        "b": 1,
        "volume": 3,
        "required_log2_N": 3,
        "injective_position_encoding": true
      },
      {
        "N": 8,
        "D": 1,
        "b": 3,
        "volume": 3,
        "required_log2_N": 3,
        "injective_position_encoding": true
      },
      {
        "N": 8,
        "D": 1,
        "b": 2,
        "volume": 2,
        "required_log2_N": 3,
        "injective_position_encoding": false
      },
      {
        "N": 16,
        "D": 1,
        "b": 4,
        "volume": 4,
        "required_log2_N": 4,
        "injective_position_encoding": true
      },
      {
        "N": 16,
        "D": 4,
        "b": 1,
        "volume": 4,
        "required_log2_N": 4,
        "injective_position_encoding": true
      },
      {
        "N": 16,
        "D": 2,
        "b": 3,
        "volume": 6,
        "required_log2_N": 4,
        "injective_position_encoding": true
      },
      {
        "N": 16,
        "D": 1,
        "b": 3,
        "volume": 3,
        "required_log2_N": 4,
        "injective_position_encoding": false
      },
      {
        "N": 64,
        "D": 1,
        "b": 6,
        "volume": 6,
        "required_log2_N": 6,
        "injective_position_encoding": true
      },
      {
        "N": 64,
        "D": 6,
        "b": 1,
        "volume": 6,
        "required_log2_N": 6,
        "injective_position_encoding": true
      },
      {
        "N": 64,
        "D": 2,
        "b": 3,
        "volume": 6,
        "required_log2_N": 6,
        "injective_position_encoding": true
      },
      {
        "N": 64,
        "D": 1,
        "b": 5,
        "volume": 5,
        "required_log2_N": 6,
        "injective_position_encoding": false
      },
      {
        "N": 256,
        "D": 1,
        "b": 8,
        "volume": 8,
        "required_log2_N": 8,
        "injective_position_encoding": true
      },
      {
        "N": 256,
        "D": 8,
        "b": 1,
        "volume": 8,
        "required_log2_N": 8,
        "injective_position_encoding": true
      },
      {
        "N": 256,
        "D": 3,
        "b": 3,
        "volume": 9,
        "required_log2_N": 8,
        "injective_position_encoding": true
      },
      {
        "N": 256,
        "D": 1,
        "b": 7,
        "volume": 7,
        "required_log2_N": 8,
        "injective_position_encoding": false
      },
      {
        "N": 1024,
        "D": 1,
        "b": 10,
        "volume": 10,
        "required_log2_N": 10,
        "injective_position_encoding": true
      },
      {
        "N": 1024,
        "D": 10,
        "b": 1,
        "volume": 10,
        "required_log2_N": 10,
        "injective_position_encoding": true
      },
      {
        "N": 1024,
        "D": 4,
        "b": 3,
        "volume": 12,
        "required_log2_N": 10,
        "injective_position_encoding": true
      },
      {
        "N": 1024,
        "D": 1,
        "b": 9,
        "volume": 9,
        "required_log2_N": 10,
        "injective_position_encoding": false
      },
      {
        "N": 4096,
        "D": 1,
        "b": 12,
        "volume": 12,
        "required_log2_N": 12,
        "injective_position_encoding": true
      },
      {
        "N": 4096,
        "D": 12,
        "b": 1,
        "volume": 12,
        "required_log2_N": 12,
        "injective_position_encoding": true
      },
      {
        "N": 4096,
        "D": 4,
        "b": 3,
        "volume": 12,
        "required_log2_N": 12,
        "injective_position_encoding": true
      },
      {
        "N": 4096,
        "D": 1,
        "b": 11,
        "volume": 11,
        "required_log2_N": 12,
        "injective_position_encoding": false
      }
    ],
    "positions_checked": 16412
  },
  "claim_3_looped_ACd_TCd_equivalence": {
    "AC_and_TC_maps": 54,
    "exhaustive_input_loop_checks": 3024,
    "maximum_composed_depth": 81
  },
  "claim_4_log_precision_SMAT_simulates_AHAT": {
    "fixed_point_cases": 800,
    "max_post_round_difference": 0.0,
    "negative_control_loose_temperature_difference": 0.28125
  },
  "claim_5_theory_only_scope": {
    "primary_pdf_sha256": "fbc31ec9024e20bef85e4e12a262991f098c093d171d6063d57bcf62419b562b",
    "source_sections": [
      "2. Preliminaries",
      "3. SMATs Can Simulate AHATs",
      "4. Padded Constant-depth Transformers Are Constant-depth Circuits",
      "5. Looped Padded Transformers Are Highly Uniform Growing-depth Circuits",
      "6. Discussion",
      "A--C formal definitions and proofs"
    ],
    "empirical_benchmark_or_training_protocol": false,
    "interpretation": "The paper is a theoretical characterization; its claims are theorem/proof claims rather than dataset, training, or benchmark results."
  }
}

````


---
<!-- trackio-cell
{"type": "code", "id": "cell_8a5fb342df87", "created_at": "2026-07-17T09:11:00+00:00", "title": "Seven regression tests", "command": ["env", "PYTHONPATH=repro", "python", "-m", "pytest", "-q", "repro/tests"], "exit_code": 0, "duration_s": 1.754}
-->
````bash
$ env PYTHONPATH=repro python -m pytest -q repro/tests
````

exit 0 · 1.8s


````output
.......                                                                  [100%]
7 passed in 1.14s

````
