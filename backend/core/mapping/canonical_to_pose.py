def canonical_to_pose(canonical: dict) -> str:
    return canonical.get("pose", "neutral")
