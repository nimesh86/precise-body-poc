# backend/core/rendering/mesh_renderer.py

from email.mime import image
import os
import numpy as np
import trimesh
import pyrender
from PIL import Image


from backend.core.models.artifacts import MeshArtifact
from backend.core.rendering.base_renderer import BaseRenderer


class MeshRenderer(BaseRenderer):
    """
    Real geometry renderer for POC v3-A.
    No textures, no face, no realism.
    Geometry truth only.
    """

    def __init__(
        self,
        image_size=(512, 512),
        background_color=(255, 255, 255, 255)
    ):
        self.image_size = image_size
        self.background_color = background_color

    def render(
        self,
        mesh_artifact: MeshArtifact,
        output_path: str
    ) -> str:
        """
        Render a mesh artifact to a PNG image.
        """

        # -----------------------------
        # 1. Load mesh from disk (CORRECT)
        # -----------------------------
        mesh = trimesh.load(
            mesh_artifact.mesh_path,
            process=False
        )

        if not isinstance(mesh, trimesh.Trimesh):
            raise ValueError("Loaded mesh is not a Trimesh object")

        # -----------------------------
        # 2. Convert to pyrender mesh
        # -----------------------------
        render_mesh = pyrender.Mesh.from_trimesh(
            mesh,
            smooth=False
        )

        # -----------------------------
        # 3. Scene setup
        # -----------------------------
        scene = pyrender.Scene(
            bg_color=self.background_color,
            ambient_light=(0.4, 0.4, 0.4)
        )
        scene.add(render_mesh)

        # -----------------------------
        # 4. Camera auto-framing
        # -----------------------------
        camera = pyrender.PerspectiveCamera(
            yfov=np.pi / 3.0
        )

        camera_pose = self._compute_camera_pose(mesh)
        scene.add(camera, pose=camera_pose)

        # -----------------------------
        # 5. Light (simple, neutral)
        # -----------------------------
        light = pyrender.DirectionalLight(
            color=np.ones(3),
            intensity=2.5
        )
        scene.add(light, pose=camera_pose)

        # -----------------------------
        # 6. Offscreen render
        # -----------------------------
        renderer = pyrender.OffscreenRenderer(
            viewport_width=self.image_size[0],
            viewport_height=self.image_size[1]
        )

        color, _ = renderer.render(scene)
        renderer.delete()

        # -----------------------------
        # 7. Save output
        # -----------------------------
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        image = Image.fromarray(color)
        image.save(output_path)

        return output_path

    def _compute_camera_pose(self, mesh: trimesh.Trimesh) -> np.ndarray:
        bounds = mesh.bounds
        center = bounds.mean(axis=0)
        size = np.linalg.norm(bounds[1] - bounds[0])

        camera_distance = size * 2.5
        camera_position = center + np.array([0.0, 0.0, camera_distance])

        pose = np.eye(4)
        pose[:3, 3] = camera_position
        return pose
