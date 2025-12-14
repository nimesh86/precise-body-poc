from backend.core.rendering.renderer_factory import get_renderer
from backend.core.rendering.mesh_renderer import MeshRenderer
from backend.core.rendering.renderer import PlaceholderRenderer


def test_renderer_factory_mesh():
    renderer = get_renderer("mesh")
    assert isinstance(renderer, MeshRenderer)


def test_renderer_factory_placeholder():
    renderer = get_renderer()
    assert isinstance(renderer, PlaceholderRenderer)
