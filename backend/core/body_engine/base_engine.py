from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseBodyEngine(ABC):
    """
    Abstract base class for all body engines.
    Every engine MUST implement this interface.
    """

    @abstractmethod
    def generate_mesh(self, engine_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a 3D body mesh.

        Args:
            engine_params (dict):
                Engine-specific parameters produced by canonical mapping.
                Example:
                {
                    "gender": "male",
                    "betas": [...],
                    "height": 1.75,
                    "pose": "neutral"
                }

        Returns:
            dict:
                {
                    "mesh_path": str,      # absolute or relative path to OBJ
                    "engine": str,         # engine name (simple / smpl / smplx)
                    "metadata": dict       # optional debug or stats
                }
        """
        pass
