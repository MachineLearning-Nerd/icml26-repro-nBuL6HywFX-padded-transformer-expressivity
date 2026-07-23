#!/usr/bin/env python3
"""Write the universal Theorem 4.2 proof-obligation certificate."""

from __future__ import annotations

import json
from pathlib import Path

from src.theorem42 import theorem42_audit


if __name__ == "__main__":
    report = theorem42_audit()
    root = Path(__file__).resolve().parents[1]
    target = root / "outputs" / "theorem42_proof_certificate.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
