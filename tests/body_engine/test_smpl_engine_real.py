import os
import pytest
from backend.core.body_engine.smpl_engine import SMPLEngine

MODEL_PATH = "assets/body_models/smpl/SMPL_NEUTRAL.pkl"

@pytest.mark.skipif(
    not os.path.exists(MODEL_PATH),
    reason="Real SMPL model files not present"
)
def test_real_smpl_engine_generates_mesh(tmp_path):
    engine = SMPLEngine()

    output_path = tmp_path / "real_smpl.obj"

    params = {
        "gender": "neutral",
        "betas": [0.0] * 10,
        "scale": 1.7,
        "output_mesh_path": str(output_path),
    }

    result = engine.generate_mesh(params)

    assert os.path.exists(result["mesh_path"])
    assert result["engine"] == "smpl"
    assert result["metadata"]["vertex_count"] > 6000
