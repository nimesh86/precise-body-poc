from backend.core.models.canonical import CanonicalBodyInput
from backend.core.errors.validation_errors import (
    SchemaValidationError,
    UnsupportedSchemaVersionError,
    ValueRangeError,
    EnumValidationError,
)


SUPPORTED_SCHEMA_VERSION = "1.0"


def validate_input(payload: dict) -> CanonicalBodyInput:
    if not isinstance(payload, dict):
        raise SchemaValidationError("Payload must be a JSON object")

    _validate_meta(payload)
    body = _validate_body(payload)

    return CanonicalBodyInput(
        gender=body["gender"],
        age=body["age"],
        height=body["height"],
        chest=body["chest"],
        waist=body["waist"],
        hips=body["hips"],
        body_fat=body["body_fat"],
    )


def _validate_meta(payload: dict) -> None:
    if "meta" not in payload:
        raise SchemaValidationError("Missing 'meta' section")

    meta = payload["meta"]

    if not isinstance(meta, dict):
        raise SchemaValidationError("'meta' must be an object")

    if "schema_version" not in meta:
        raise UnsupportedSchemaVersionError("Missing schema_version")

    if meta["schema_version"] != SUPPORTED_SCHEMA_VERSION:
        raise UnsupportedSchemaVersionError(
            f"Unsupported schema_version: {meta['schema_version']}"
        )


def _validate_body(payload: dict) -> dict:
    if "body" not in payload:
        raise SchemaValidationError("Missing 'body' section")

    body = payload["body"]

    if not isinstance(body, dict):
        raise SchemaValidationError("'body' must be an object")

    required_fields = {
        "gender",
        "age",
        "height",
        "chest",
        "waist",
        "hips",
        "body_fat",
    }

    extra_fields = set(body.keys()) - required_fields
    missing_fields = required_fields - set(body.keys())

    if missing_fields:
        raise SchemaValidationError(f"Missing fields: {missing_fields}")

    if extra_fields:
        raise SchemaValidationError(f"Unknown fields: {extra_fields}")

    _validate_gender(body["gender"])
    _validate_age(body["age"])
    _validate_unit_range("height", body["height"])
    _validate_unit_range("chest", body["chest"])
    _validate_unit_range("waist", body["waist"])
    _validate_unit_range("hips", body["hips"])
    _validate_unit_range("body_fat", body["body_fat"])

    return body


def _validate_gender(value: str) -> None:
    if not isinstance(value, str):
        raise EnumValidationError("gender must be a string")

    if value not in {"male", "female"}:
        raise EnumValidationError(f"Invalid gender: {value}")


def _validate_age(value: int) -> None:
    if not isinstance(value, int):
        raise ValueRangeError("age must be an integer")

    if value < 0 or value > 70:
        raise ValueRangeError("age must be between 0 and 70")


def _validate_unit_range(name: str, value: float) -> None:
    if not isinstance(value, (int, float)):
        raise ValueRangeError(f"{name} must be a number")

    if value < 0.0 or value > 1.0:
        raise ValueRangeError(f"{name} must be between 0.0 and 1.0")
