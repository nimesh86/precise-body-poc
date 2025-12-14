import os
import numpy as np
import pytest
from backend.core.body_engine.smpl_engine import SMPLEngine

MODEL_PATH = "assets/body_models/smpl/SMPL_NEUTRAL.pkl"

@pytest.mark.skipif(
    not os.path.exists(MODEL_PATH),
    reason="Real SMPL model files not present"
)
def test_pose_changes_geometry(tmp_path):
    engine = SMPLEngine()

    base_params = {
        "gender": "neutral",
        "betas": [0.0] * 10,
        "scale": 1.7,
        "output_mesh_path": str(tmp_path / "neutral.obj"),
        "pose": "neutral",
    }

    a_pose_params = dict(base_params)
    a_pose_params["output_mesh_path"] = str(tmp_path / "a_pose.obj")
    a_pose_params["pose"] = "a_pose"

    neutral = engine.generate_mesh(base_params)
    a_pose = engine.generate_mesh(a_pose_params)

    assert os.path.exists(neutral["mesh_path"])
    assert os.path.exists(a_pose["mesh_path"])
    assert neutral["mesh_path"] != a_pose["mesh_path"]
