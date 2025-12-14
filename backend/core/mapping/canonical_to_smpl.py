from typing import Dict, Any, List


def canonical_to_smpl(canonical: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert canonical body parameters into SMPL-compatible parameters.
    """

    gender = canonical.get("gender", "neutral")

    # Normalize betas (SMPL expects ~10 shape coefficients)
    betas: List[float] = [
        canonical.get("body_fat", 0.5),
        canonical.get("waist", 0.5),
        canonical.get("hips", 0.5),
        canonical.get("chest", 0.5),
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    ]

    # Height scaling (SMPL neutral ~1.7m baseline)
    height_norm = canonical.get("height", 0.5)
    scale = 1.5 + height_norm * 0.4  # ~1.5m → ~1.9m

    return {
        "engine": "smpl",
        "gender": gender,
        "betas": betas,
        "scale": scale,
        "pose": canonical.get("pose", "neutral")
    }
