from backend.core.body_engine.smpl_engine import SMPLEngine
from backend.core.models.artifacts import MeshArtifact
from backend.core.rendering.renderer import render_preview

import os

OUTPUT_DIR = "outputs/validation"
os.makedirs(OUTPUT_DIR, exist_ok=True)

engine = SMPLEngine()

base_params = {
    "gender": "neutral",
    "betas": [0.0] * 10,
    "scale": 1.7,
}

poses = ["neutral", "a_pose", "t_pose"]

for pose in poses:
    mesh_path = os.path.join(OUTPUT_DIR, f"body_{pose}.obj")

    params = {
        **base_params,
        "pose": pose,
        "output_mesh_path": mesh_path,
    }

    result = engine.generate_mesh(params)

    mesh_artifact = MeshArtifact(
        mesh_path=result["mesh_path"]
    )

    render_artifact = render_preview(mesh_artifact)

    print(f"Rendered preview for {pose}: {render_artifact.image_path}")
