# Conclusion


---
<!-- trackio-cell
{"type": "artifact", "id": "cell_bundle_nbul_v5", "created_at": "2026-07-19T12:36:08+00:00", "title": "Lean formalization reproduction bundle", "artifact": "reproduction-padded-transformer-expressivity/repro-bundle:v5", "artifact_type": "dataset"}
-->
**📦 Artifact** `reproduction-padded-transformer-expressivity/repro-bundle:v5` · dataset

https://huggingface.co/buckets/DineshAI/nBuL6HywFX-artifacts#reproduction-padded-transformer-expressivity/repro-bundle:v5


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_rerun_nbul", "created_at": "2026-07-19T09:55:07+00:00", "title": "Download and rerun"}
-->
Download the bundle and run from its root:

```bash
python -m pip install -r requirements.txt
elan toolchain install leanprover/lean4:v4.32.0
lean formal/PaddedTransformer.lean
python repro/run_lean_formal_check.py
PYTHONPATH=repro python repro/run_theorem42.py
PYTHONPATH=repro python repro/run_audit.py
PYTHONPATH=repro python -m pytest -q repro/tests
```

Expected: Lean 4.32; 11 kernel dependency reports; no forbidden proof escapes; no `sorryAx`; 16 tests passed. The bundle contains the formal source/toolchain pin, proof certificate, printed-routing rejection, constant-width repair, source mapping, and regression evidence. Formalization limits are disclosed in `docs/LEAN_FORMAL_AUDIT.md`.
