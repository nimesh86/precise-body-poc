class ValidationError(Exception):
    pass


class SchemaValidationError(ValidationError):
    pass


class UnsupportedSchemaVersionError(ValidationError):
    pass


class ValueRangeError(ValidationError):
    pass


class EnumValidationError(ValidationError):
    pass
