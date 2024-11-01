# Schema Management Documentation

This document provides an overview of the schema management system implemented in the Simple Family Budget Tracking App.

## Overview

The schema management layer is responsible for handling interactions with the database schema. It includes components for loading the schema, retrieving table names, and getting column definitions.

## Source of Truth

The database schema file serves as the single source of truth for the database structure. This means:

- All database structural changes should be made in the schema file only.
- The application relies on this schema file to understand the database structure.
- When making changes to the database structure, only the schema file needs to be updated.
- This approach ensures consistency across the application and simplifies database management.

## Components

### 1. SchemaManager

- **Purpose**: Serves as the main interface for schema-related operations.
- **Responsibilities**:
  - Load the database schema from the source-of-truth file.
  - Retrieve the names of tables defined in the schema.
  - Get the columns for a specific table.

#### Methods:
- `load_schema()`
  - Loads the database schema from the predefined schema file (source of truth).
  - Raises an error if there is an issue reading the schema file.

- `get_table_names()`
  - Returns a list of table names defined in the loaded schema.
  - Raises an error if there is an issue processing the schema.

- `get_table_columns(table_name)`
  - Returns a list of column names for a specified table.
  - Raises an error if there is an issue processing the schema or if the table does not exist.

---

### 2. Schema Operations

The following functions are defined to handle specific operations related to the database schema:

- **get_schema()**
  - Reads and returns the entire database schema from the source-of-truth schema file.
  - Raises an error if there is an issue reading the file.

- **get_table_names(schema)**
  - Extracts and returns a list of table names from a given schema string.

- **get_table_columns(schema, table_name)**
  - Extracts and returns a list of column names for a specified table from a given schema string.
  - Returns `None` if the specified table does not exist in the schema.

## Best Practices

1. **Schema Updates**: When the database structure needs to change, update only the schema file. The SchemaManager will then reflect these changes throughout the application.

2. **Consistency**: Always use the SchemaManager to retrieve information about the database structure. This ensures that all parts of the application are working with the same, up-to-date structural information.

3. **Version Control**: Keep the schema file under version control to track changes over time.

4. **Migration Management**: Consider implementing a migration system for managing schema changes in a production environment.

## Conclusion

This documentation provides an overview of how to manage and interact with the database schema within the Simple Family Budget Tracking App. By maintaining the schema file as the single source of truth, we ensure consistency and simplify database structure management across the application. For further details on usage or specific implementation questions, please refer to the source code or reach out to the development team.