# src/controllers/schema_controllers/schema_exceptions.py

class SchemaError(Exception):
    """Base exception for schema-related errors."""
    pass

class SchemaReadError(SchemaError):
    """Raised when there's an error reading the schema file."""
    pass

class SchemaValidationError(SchemaError):
    """Raised when schema validation fails."""
    pass

class SchemaApplicationError(SchemaError):
    """Raised when there's an error applying schema changes."""
    pass
