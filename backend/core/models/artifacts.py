from dataclasses import dataclass

@dataclass(frozen=True)
class MeshArtifact:
    mesh_path: str

@dataclass(frozen=True)
class RenderArtifact:
    image_path: str

@dataclass(frozen=True)
class ResponsePayload:
    status: str
    preview_image: str
    mesh: str | None = None
