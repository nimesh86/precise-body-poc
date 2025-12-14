import os
import trimesh
from backend.core.rendering.renderer import PlaceholderRenderer
from backend.core.models.artifacts import MeshArtifact


def test_placeholder_renderer_creates_image(tmp_path):
    mesh_path = tmp_path / "dummy.obj"
    trimesh.creation.box().export(mesh_path)

    mesh = MeshArtifact(mesh_path=str(mesh_path))

    renderer = PlaceholderRenderer()
    result = renderer.render(mesh)

    assert os.path.exists(result.image_path)
