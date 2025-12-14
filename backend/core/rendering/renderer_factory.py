
from backend.core.rendering.renderer import PlaceholderRenderer
from backend.core.rendering.mesh_renderer import MeshRenderer


def get_renderer(renderer_type: str = "placeholder"):
    """
    Renderer selector for POC v3.
    Explicit is better than implicit.
    """

    if renderer_type == "mesh":
        return MeshRenderer()

    # default (existing behavior)
    return PlaceholderRenderer()
