import numpy as np
from backend.core.models.canonical import CanonicalBodyInput
from backend.core.models.engine import EngineBodyParams


# Mapping version (internal)
MAPPING_VERSION = "1.0"

# Engine assumptions (POC-safe)
ENGINE_SHAPE_VECTOR_SIZE = 10

# Height mapping (meters, abstracted)
MIN_HEIGHT = 1.5
MAX_HEIGHT = 1.9

def map_to_engine_params(body: CanonicalBodyInput) -> EngineBodyParams:
    engine_gender = _map_gender(body.gender)
    engine_scale = _map_height(body.height)
    shape_vector = _map_shape(body)

    return EngineBodyParams(
        engine_gender=engine_gender,
        engine_scale=engine_scale,
        engine_shape_vector=shape_vector,
    )

def _map_gender(gender: str) -> str:
    # Direct mapping in v1
    return gender

def _map_height(height_norm: float) -> float:
    # Linear scaling
    return MIN_HEIGHT + height_norm * (MAX_HEIGHT - MIN_HEIGHT)

def _map_shape(body: CanonicalBodyInput) -> np.ndarray:
    shape = np.zeros(ENGINE_SHAPE_VECTOR_SIZE, dtype=np.float32)

    # Index convention (POC)
    # 0–1 : chest
    # 2–3 : waist
    # 4–5 : hips
    # 6–7 : body fat
    # 8–9 : age influence

    shape[0:2] += body.chest
    shape[2:4] += body.waist
    shape[4:6] += body.hips
    shape[6:8] += body.body_fat
    shape[8:10] += _map_age(body.age)

    return shape

def _map_age(age: int) -> float:
    # Normalize age to 0–1 range
    return age / 70.0
