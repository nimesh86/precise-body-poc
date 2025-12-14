from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class EngineBodyParams:
    engine_gender: str
    engine_scale: float
    engine_shape_vector: np.ndarray
    engine_pose: str
