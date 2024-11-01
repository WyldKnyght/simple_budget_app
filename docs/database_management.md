# Database Documentation

This document provides an overview of the database management system implemented in the Simple Family Budget Tracking App.

## Overview

The database layer is responsible for managing all interactions with the SQLite database. It includes components for establishing connections, initializing the database schema, executing queries, and handling errors.

## Important Note on Schema Changes

The database schema serves as the single source of truth for the database structure. Any changes to the database structure should be made in the schema file only. For details on managing and interacting with the schema, please refer to the [Schema Management Documentation](./schema_management.md).

## Components

### 1. DatabaseManager

- **Purpose**: Serves as the main interface for all database operations.
- **Responsibilities**:
  - Manage connections to the database.
  - Initialize the database using a predefined schema.
  - Execute SQL queries.

#### Methods:
- `get_connection()`
  - Returns a connection to the SQLite database.
  - Raises `ConnectionError` if unable to establish a connection.

- `initialize_database()`
  - Initializes the database using the schema defined in a separate file.
  - Raises `InitializationError` if there's an issue during initialization.

- `execute_query(query, params=None)`
  - Executes a SQL query on the database.
  - Returns a cursor object containing the query results.
  - Raises `QueryExecutionError` if there's an issue executing the query.

---

### 2. DatabaseConnections

- **Purpose**: Manages connections to the SQLite database.

#### Methods:
- `get_connection()`
  - Establishes and returns a connection to the SQLite database.
  - Raises `ConnectionError` if unable to connect.

---

### 3. DatabaseInitializer

- **Purpose**: Handles initialization of the database schema.

#### Methods:
- `initialize_database()`
  - Reads the schema from the source-of-truth file and initializes the database.
  - Raises `InitializationError` if there's an issue reading the schema or executing SQL commands.

---

### 4. QueryExecutor

- **Purpose**: Executes SQL queries against the database.

#### Methods:
- `execute_query(query, params=None)`
  - Executes a given SQL query and returns results via a cursor.
  - Raises `QueryExecutionError` if there's an issue executing the query.

---

### 5. Custom Exceptions

The following custom exceptions are defined for handling specific error scenarios:

- **DatabaseError**: Base class for all database-related exceptions.
- **ConnectionError**: Raised when there's an issue connecting to the database.
- **InitializationError**: Raised when there's an issue initializing the database.
- **QueryExecutionError**: Raised when there's an issue executing a SQL query.

## Best Practices

1. Always use the DatabaseManager for database operations to ensure consistent error handling and connection management.
2. Refer to the [Schema Management Documentation](./schema_management.md) when making changes to the database structure.
3. Use parameterized queries to prevent SQL injection vulnerabilities.

## Conclusion

This documentation provides an overview of how to interact with and manage the SQLite database within the Simple Family Budget Tracking App. For details on schema management and changes, please refer to the Schema Management Documentation. For further details on usage or specific implementation questions, please refer to the source code or reach out to the development team.