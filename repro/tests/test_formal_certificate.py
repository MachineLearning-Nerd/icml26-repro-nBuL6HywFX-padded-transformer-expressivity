from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_lean_certificate_matches_source() -> None:
    source = ROOT / "formal" / "PaddedTransformer.lean"
    certificate = json.loads(
        (ROOT / "outputs" / "lean_formal_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    assert certificate["verdict"] == "lean_kernel_verified"
    assert certificate["source_sha256"] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert certificate["toolchain"] == "leanprover/lean4:v4.32.0"
    assert certificate["forbidden_escape_tokens"] == []
    assert certificate["sorry_ax_dependency"] is False
    assert certificate["kernel_checked_theorems"] == 11
    assert len(certificate["axiom_reports"]) == 11


def test_new_universal_routing_theorems_are_axiom_free() -> None:
    certificate = json.loads(
        (ROOT / "outputs" / "lean_formal_certificate.json").read_text(
            encoding="utf-8"
        )
    )
    reports = "\n".join(certificate["axiom_reports"])
    for theorem in (
        "repaired_layer1_routes_exactly_source",
        "repaired_layer2_collects_exactly_destination",
        "printed_route_rejected_when_source_ne_gate",
        "theorem42_from_source_inclusions",
        "all_levels_correct",
    ):
        assert f"'{theorem}'" not in reports
        qualified = f"'PaddedTransformer.{theorem}' does not depend on any axioms"
        assert qualified in reports
