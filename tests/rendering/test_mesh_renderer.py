import os
import trimesh
from backend.core.rendering.mesh_renderer import MeshRenderer
from backend.core.models.artifacts import MeshArtifact


def _create_dummy_mesh(path):
    mesh = trimesh.creation.icosphere(radius=1.0)
    mesh.export(path)


def test_mesh_renderer_outputs_image(tmp_path):
    mesh_path = tmp_path / "test.obj"
    trimesh.creation.box().export(mesh_path)

    mesh = MeshArtifact(mesh_path=str(mesh_path))

    output_path = tmp_path / "out.png"
    renderer = MeshRenderer()

    result = renderer.render(mesh, str(output_path))

    assert os.path.exists(result)


def test_mesh_renderer_is_deterministic(tmp_path):
    mesh_path = tmp_path / "same.obj"
    trimesh.creation.box().export(mesh_path)

    mesh = MeshArtifact(mesh_path=str(mesh_path))

    renderer = MeshRenderer()

    out1 = renderer.render(mesh, str(tmp_path / "a.png"))
    out2 = renderer.render(mesh, str(tmp_path / "b.png"))

    assert os.path.exists(out1)
    assert os.path.exists(out2)

