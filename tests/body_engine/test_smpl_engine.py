from backend.core.body_engine.smpl_engine import SMPLEngine


def test_smpl_engine_generate_mesh_contract(tmp_path):
    engine = SMPLEngine()

    engine_params = {
        "gender": "male",
        "betas": [0.5] * 10,
        "scale": 1.75,
        "output_mesh_path": str(tmp_path / "smpl_test.obj"),
        "dry_run": True,
    }


    result = engine.generate_mesh(engine_params)

    assert isinstance(result, dict)
    assert result["engine"] == "smpl"
    assert "mesh_path" in result
    assert result["mesh_path"].endswith(".obj")
    assert "metadata" in result
    assert result["metadata"]["gender"] == "male"

def test_smpl_engine_generate_mesh_contract(tmp_path):
    engine = SMPLEngine()

    engine_params = {
        "gender": "male",
        "betas": [0.5] * 10,
        "scale": 1.75,
        "output_mesh_path": str(tmp_path / "smpl_test.obj"),
        "dry_run": True,
        "pose": "t_pose",
    }

    result = engine.generate_mesh(engine_params)

    assert result["engine"] == "smpl"
    assert result["metadata"]["gender"] == "male"
