# Validation Management Documentation

This document provides an overview of the validation management system implemented in the Simple Family Budget Tracking App.

## Overview

The validation management system is responsible for handling all validation operations across the application. It follows a layered architecture to ensure separation of concerns and maintainability.

## Components

### 1. ValidationManager

- **Location**: `src/controllers/validation_manager.py`
- **Purpose**: Serves as the main coordinator for validation-related operations.
- **Responsibilities**:
  - Coordinate validation operations across different parts of the application.
  - Act as an interface between the UI layer and the validation logic layer.

#### Methods:
- `validate_database_schema()`
  - Coordinates the validation of the database schema.
- `check_and_validate_database(parent)`
  - Coordinates checking and validating the database, including UI interactions.
- `validate_account_data(account_name, account_number, account_type)`
  - Coordinates validation of account data.
- `validate_category_data(category_name)`
  - Coordinates validation of category data.
- `validate_expense_data(expense_name, amount)`
  - Coordinates validation of expense data.
- `validate_transaction_data(transaction_data)`
  - Coordinates validation of transaction data.

### 2. ValidationService

- **Location**: `src/controllers/services/validation_service.py`
- **Purpose**: Implements the business logic for validation operations.
- **Responsibilities**:
  - Perform specific validation checks.
  - Handle user interactions related to validation (e.g., prompts for database creation/reset).

#### Key Methods:
- `check_and_validate_database(validation_operations, parent)`
- `handle_non_existent_database(validation_operations, parent)`
- `handle_invalid_schema(validation_operations, parent)`
- `show_warning_message(parent, custom_message=None)`
- `prompt_create_database(parent)`
- `prompt_reset_database(parent)`

### 3. ValidationOperations

- **Location**: `src/data_access/db_validation_operations.py`
- **Purpose**: Handles direct database interactions for validation-related operations.
- **Responsibilities**:
  - Execute validation checks that require database access.
  - Interact with the DatabaseManager to perform validation operations.

#### Key Methods:
- `validate_schema()`
- `database_exists()`
- `get_current_schema()`
- `initialize_database()`
- `reset_database()`
- `refresh_schema_cache()`

## Data Flow

1. User Interface (UI) or other components interact with `ValidationManager`.
2. `ValidationManager` delegates tasks to `ValidationService`.
3. `ValidationService` performs validation logic and user interactions.
4. `ValidationService` uses `ValidationOperations` for database-related validations.
5. `ValidationOperations` executes validation checks using `DatabaseManager`.

## Error Handling

- The `error_handler` decorator is used in `ValidationOperations` to ensure consistent error logging and handling across all validation operations.
- Custom exceptions may be raised for specific validation error scenarios.

## Constants

Validation-related constants (error messages, prompts) are centralized in `src/configs/error_config.py` to maintain consistency and ease of modification.

## Best Practices

1. Always use `ValidationManager` for validation-related operations in the UI or other high-level components.
2. Implement new validation rules or checks in `ValidationService`.
3. For any changes to the database schema validation, update both the schema file and the relevant validation methods.
4. Maintain separation of concerns: keep UI logic, validation logic, and data access logic in their respective layers.

## Conclusion

This validation management system provides a robust and maintainable structure for handling all validation-related operations in the Simple Family Budget Tracking App. Its layered architecture allows for easy testing, modification, and extension of functionality as the application grows.
