# src/configs/error_config.py

DB_CONNECTION_ERROR = "Failed to connect to the database: {}"
DB_INITIALIZATION_ERROR = "Failed to initialize the database: {}"
DB_QUERY_ERROR = "Error executing database query: {}"
DB_SCHEMA_ERROR = "Database schema validation failed: {}"
DB_RESET_ERROR = "Error resetting the database: {}"
SCHEMA_FILE_READ_ERROR = "Failed to read schema file: {}"
DB_CLOSE_ERROR = "Error closing database connection: {}"
DB_LOAD_ERROR = "Error loading database: {}"

# File operation error messages
FILE_NOT_FOUND_ERROR = "File not found: {}"
FILE_READ_ERROR = "Error reading file: {}"
FILE_WRITE_ERROR = "Error writing to file: {}"

# User interface error messages
UI_INITIALIZATION_ERROR = "Error initializing user interface: {}"

# Data validation error messages
INVALID_INPUT_ERROR = "Invalid input: {}"
MISSING_REQUIRED_FIELD_ERROR = "Missing required field: {}"

# Application-specific error messages
ACCOUNT_NOT_FOUND_ERROR = "Account not found with ID: {}"
CATEGORY_NOT_FOUND_ERROR = "Category not found with ID: {}"
TRANSACTION_NOT_FOUND_ERROR = "Transaction not found with ID: {}"
EXPENSE_NOT_FOUND_ERROR = "Expense not found with ID: {}"

# General error messages
UNEXPECTED_ERROR = "An unexpected error occurred: {}"