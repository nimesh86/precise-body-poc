# tests/body_engine/test_simple_engine.py

import os
from backend.core.body_engine.simple_engine import SimpleEngine


def test_simple_engine_generate_mesh(tmp_path):
    """
    Sanity test for POC v1 SimpleEngine.
    Ensures engine contract is respected.
    """

    engine = SimpleEngine()

    # Fake minimal engine params
    engine_params = {
        "output_mesh_path": str(tmp_path / "test_mesh.obj"),
        # add any other params your POC v1 logic requires
    }

    result = engine.generate_mesh(engine_params)

    # Contract checks
    assert isinstance(result, dict)
    assert "mesh_path" in result
    assert "engine" in result
    assert "metadata" in result

    assert result["engine"] == "simple"
    assert result["mesh_path"].endswith(".obj")

    # Optional: check file exists (only if POC v1 creates it)
    if os.path.exists(result["mesh_path"]):
        assert os.path.isfile(result["mesh_path"])
