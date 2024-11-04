# src/configs/error_config.py

# Database error messages
DB_CONNECTION_ERROR = "Failed to connect to the database: {}"
DB_INITIALIZATION_ERROR = "Failed to initialize the database: {}"
DB_QUERY_ERROR = "Error executing database query: {}"
DB_SCHEMA_ERROR = "Database schema validation failed: {}"
DB_RESET_ERROR = "Error resetting the database: {}"
DB_CLOSE_ERROR = "Error closing database connection: {}"
DB_LOAD_ERROR = "Error loading database: {}"

# File operation error messages
FILE_NOT_FOUND_ERROR = "File not found: {}"
FILE_READ_ERROR = "Error reading file: {}"
FILE_WRITE_ERROR = "Error writing to file: {}"

# Schema-related error messages
SCHEMA_FILE_READ_ERROR = "Failed to read schema file: {}"
SCHEMA_VALIDATION_ERROR = "Schema validation failed: {}"

# Database state error messages
DB_ALREADY_EXISTS_ERROR = "Database already exists"
DB_DOES_NOT_EXIST_ERROR = "Database does not exist"

# Success messages
DB_INIT_SUCCESS = "Database initialized successfully"
DB_RESET_SUCCESS = "Database reset successfully"
DB_REMOVED_SUCCESS = "Existing database removed"
NEW_DB_CREATED_SUCCESS = "New database created successfully"
DB_CONNECTION_SUCCESS = "Successfully connected to the database"
DB_CLOSE_SUCCESS = "Successfully closed database connection"

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

# Warning messages
DB_VALIDATION_WARNING = 'The application may not function correctly without a valid database. You can manually reset the database or make other changes as needed.'
DB_CREATE_PROMPT = 'No database found. Would you like to create a new one?'
DB_RESET_PROMPT = 'The database schema is outdated. Some features may not work. Would you like to reset the database? Warning: This will delete all existing data.'