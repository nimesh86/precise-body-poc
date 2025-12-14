from backend.core.mapping.canonical_to_smpl import canonical_to_smpl


def test_canonical_to_smpl_basic_mapping():
    canonical = {
        "gender": "female",
        "height": 0.6,
        "waist": 0.3,
        "hips": 0.7,
        "chest": 0.6,
        "body_fat": 0.4,
        "pose": "neutral"
    }

    result = canonical_to_smpl(canonical)

    assert result["engine"] == "smpl"
    assert result["gender"] == "female"
    assert len(result["betas"]) == 10
    assert isinstance(result["scale"], float)
    assert 1.5 <= result["scale"] <= 1.9
