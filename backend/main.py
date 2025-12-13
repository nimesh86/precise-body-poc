from backend.core.validation.validator import validate_input
from backend.core.mapping.canonical_to_engine import map_to_engine_params
from backend.core.body_engine.body_generator import generate_body_mesh
from backend.core.rendering.renderer import render_preview
from backend.core.output.response_builder import prepare_response


def generate_character(payload: dict) -> dict:
    """
    Orchestrates full backend pipeline.

    Flow:
    Payload
      → Validation
      → Mapping
      → Body Engine
      → Renderer
      → Response
    """

    canonical_body = validate_input(payload)
    engine_params = map_to_engine_params(canonical_body)
    mesh_artifact = generate_body_mesh(engine_params)
    render_artifact = render_preview(mesh_artifact)
    response = prepare_response(mesh_artifact, render_artifact)

    return response.__dict__
