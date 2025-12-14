import os
import torch
import numpy as np
import trimesh
from typing import Dict, Any

import smplx

from backend.core.body_engine.base_engine import BaseBodyEngine
from backend.core.body_engine.base_smpl_engine import BaseSMPLFamilyEngine


class SMPLEngine(BaseBodyEngine, BaseSMPLFamilyEngine):
    """
    Real SMPL-based body generation engine (deterministic, CPU-first).
    """

    MODEL_DIR = "assets/body_models/smpl"

    def generate_mesh(self, engine_params: Dict[str, Any]) -> Dict[str, Any]:
        if engine_params.get("dry_run", False):
            return {
                        "mesh_path": engine_params.get(
                            "output_mesh_path", "outputs/meshes/smpl_dummy.obj"
                        ),
                        "engine": "smpl",
                        "metadata": {
                            "gender": engine_params.get("gender"),
                            "scale": engine_params.get("scale"),
                            "betas": engine_params.get("betas"),
                        }
                    }

        gender = engine_params.get("gender", "neutral")
        betas = engine_params.get("betas")
        scale = engine_params.get("scale", 1.7)
        output_mesh_path = engine_params.get("output_mesh_path")

        if betas is None or len(betas) != 10:
            raise ValueError("SMPL requires exactly 10 beta values")

        model_path = self._resolve_model_path(gender)

        # Deterministic setup
        torch.manual_seed(0)
        torch.set_grad_enabled(False)

        model = smplx.create(
            model_path=model_path,
            model_type="smpl",
            gender=gender,
            use_pca=False,
            batch_size=1
        )

        betas_tensor = torch.tensor(betas, dtype=torch.float32).unsqueeze(0)

        pose_name = engine_params.get("pose", "neutral")
        body_pose = self._load_pose(pose_name)

        output = model(
            betas=betas_tensor,
            return_verts=True
        )

        vertices = output.vertices[0].cpu().numpy()
        vertices *= scale

        faces = model.faces

        mesh = trimesh.Trimesh(vertices=vertices, faces=faces, process=False)

        os.makedirs(os.path.dirname(output_mesh_path), exist_ok=True)
        mesh.export(output_mesh_path)

        return {
            "mesh_path": output_mesh_path,
            "engine": "smpl",
            "metadata": {
                "gender": gender,
                "scale": scale,
                "betas": betas,
                "vertex_count": int(vertices.shape[0])
            }
        }

    def _resolve_model_path(self, gender: str) -> str:
        gender = gender.lower()

        if gender == "male":
            filename = "SMPL_MALE.pkl"
        elif gender == "female":
            filename = "SMPL_FEMALE.pkl"
        else:
            filename = "SMPL_NEUTRAL.pkl"

        path = os.path.join(self.MODEL_DIR, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"SMPL model not found: {path}")

        return path

    