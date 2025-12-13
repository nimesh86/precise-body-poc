from backend.core.models.artifacts import (
    MeshArtifact,
    RenderArtifact,
    ResponsePayload,
)


def prepare_response(
    mesh: MeshArtifact,
    render: RenderArtifact,
) -> ResponsePayload:
    """
    Assembles final response payload.
    No logic, no transformation.
    """

    return ResponsePayload(
        status="success",
        preview_image=render.image_path,
        mesh=mesh.mesh_path,
    )
