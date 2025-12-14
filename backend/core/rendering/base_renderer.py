
from abc import ABC, abstractmethod
from backend.core.models.artifacts import MeshArtifact, RenderArtifact


class BaseRenderer(ABC):

    @abstractmethod
    def render(self, mesh: MeshArtifact) -> RenderArtifact:
        pass
