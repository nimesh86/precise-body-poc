from dataclasses import dataclass


@dataclass(frozen=True)
class CanonicalBodyInput:
    gender: str
    age: int
    height: float
    chest: float
    waist: float
    hips: float
    body_fat: float
