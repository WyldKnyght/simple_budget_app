# Account Management Documentation

This document provides an overview of the account management system implemented in the Simple Family Budget Tracking App.

## Overview

The account management system is responsible for handling all operations related to user accounts. It follows a layered architecture to ensure separation of concerns and maintainability.

## Components

### 1. AccountManager

- **Location**: `src/controllers/account_manager.py`
- **Purpose**: Serves as the main coordinator for account-related operations.
- **Responsibilities**:
  - Coordinate account creation, retrieval, updating, and deletion.
  - Act as an interface between the UI layer and the business logic layer.

#### Methods:
- `create_account(account_name, account_number, account_type)`
  - Coordinates the creation of a new account.

- `get_account_by_id(account_id)`
  - Coordinates retrieving an account by its ID.

- `get_all_accounts()`
  - Coordinates retrieving all accounts.

- `update_account(account_id, account_name, account_number, account_type)`
  - Coordinates updating an existing account.

- `delete_account(account_id)`
  - Coordinates deleting an account by its ID.

### 2. AccountService

- **Location**: `src/controllers/services/account_service.py`
- **Purpose**: Implements the business logic for account operations.
- **Responsibilities**:
  - Validate account data.
  - Interact with the data access layer to perform CRUD operations.
  - Handle any business rules related to accounts.

#### Key Methods:
- `create_account(account_name, account_number, account_type)`
- `get_account_by_id(account_id)`
- `get_all_accounts()`
- `update_account(account_id, account_name, account_number, account_type)`
- `delete_account(account_id)`
- `_validate_account_data(account_name, account_number, account_type)`

### 3. AccountOperations

- **Location**: `src/data_access/db_account_operations.py`
- **Purpose**: Handles direct database interactions for account-related operations.
- **Responsibilities**:
  - Execute SQL queries for CRUD operations on accounts.
  - Interact with the DatabaseManager to perform database operations.

#### Key Methods:
- `create_account(account_name, account_number, account_type)`
- `get_account_by_id(account_id)`
- `get_all_accounts()`
- `update_account(account_id, account_name, account_number, account_type)`
- `delete_account(account_id)`

## Data Flow

1. User Interface (UI) interacts with `AccountManager`.
2. `AccountManager` delegates tasks to `AccountService`.
3. `AccountService` performs business logic and data validation.
4. `AccountService` uses `AccountOperations` for database interactions.
5. `AccountOperations` executes SQL queries using `DatabaseManager`.

## Error Handling

- The `error_handler` decorator is used in `AccountService` to ensure consistent error logging and handling across all account operations.
- Custom exceptions may be raised for specific error scenarios.

## Constants

Account-related constants (table names, field names, SQL queries) are centralized in `src/configs/constants.py` to maintain consistency and ease of modification.

## Best Practices

1. Always use `AccountManager` for account-related operations in the UI or other high-level components.
2. Implement new business rules or validations in `AccountService`.
3. For any changes to the database schema related to accounts, update both the schema file and the relevant constants.
4. Maintain separation of concerns: keep UI logic, business logic, and data access logic in their respective layers.

## Conclusion

This account management system provides a robust and maintainable structure for handling all account-related operations in the Simple Family Budget Tracking App. Its layered architecture allows for easy testing, modification, and extension of functionality as the application grows.