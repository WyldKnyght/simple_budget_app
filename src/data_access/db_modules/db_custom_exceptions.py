# src/data_access/db_custom_exceptions.py

class DatabaseError(Exception):
    """Base class for database-related exceptions."""
    pass

class ConnectionError(DatabaseError):
    """Raised when there's an issue connecting to the database."""
    pass

class InitializationError(DatabaseError):
    """Raised when there's an issue initializing the database."""
    pass

class QueryExecutionError(DatabaseError):
    """Raised when there's an issue executing a database query."""
    pass