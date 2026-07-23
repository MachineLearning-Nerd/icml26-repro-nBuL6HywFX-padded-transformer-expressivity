#!/usr/bin/env python3
"""Run and persist the fail-closed Theorem 4.2 obligation audit."""

from __future__ import annotations

import json
from pathlib import Path

from src.theorem42_obligations import run_obligation_audit


if __name__ == "__main__":
    report = run_obligation_audit()
    root = Path(__file__).resolve().parents[1]
    target = root / "outputs" / "theorem42_obligations.json"
    target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    summary = report["summary"]
    print("Theorem 4.2 fail-closed obligation audit")
    print(f"sources pinned: {len(report['source_pins'])}")
    print(f"obligations closed: {summary['closed']} / {summary['total_obligations']}")
    print(f"derived checks executed: {summary['derived_and_checked']}")
    print(f"Claim 1 equality closed: {summary['claim_1_equality_closed']}")
    print(f"Claim 2 equality closed with repair: {summary['claim_2_equality_closed_with_repair']}")
    print(f"printed Lemma 4.1 route rejected: {summary['printed_lemma_4_1_route_rejected']}")
    print(f"unresolved obligations: {summary['unresolved_obligations']}")
    print(f"wrote {target.relative_to(root)}")
