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

