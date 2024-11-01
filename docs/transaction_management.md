# Transaction Management Documentation

This document provides an overview of the transaction management system implemented in the Simple Family Budget Tracking App.

## Overview

The transaction management system is responsible for handling all operations related to financial transactions. It allows for creating, retrieving, updating, and deleting transaction records, which are central to tracking the flow of money in the budget app.

## Components

### 1. TransactionManager

- **Location**: `src/controllers/transaction_manager.py`
- **Purpose**: Serves as the main coordinator for transaction-related operations.
- **Responsibilities**:
  - Coordinate transaction creation, retrieval, updating, and deletion.
  - Act as an interface between the UI layer and the business logic layer.

#### Methods:
- `create_transaction(account_id, date, payee=None, memo=None, category_id=None, payment=None, deposit=None, account_balance=None, note=None)`
  - Coordinates the creation of a new transaction.

- `get_transaction_by_id(transaction_id)`
  - Coordinates retrieving a transaction by its ID.

- `get_all_transactions()`
  - Coordinates retrieving all transactions.

- `update_transaction(transaction_id, account_id, date, payee=None, memo=None, category_id=None, payment=None, deposit=None, account_balance=None, note=None)`
  - Coordinates updating an existing transaction.

- `delete_transaction(transaction_id)`
  - Coordinates deleting a transaction by its ID.

### 2. TransactionService

- **Location**: `src/controllers/services/transaction_service.py`
- **Purpose**: Implements the business logic for transaction operations.
- **Responsibilities**:
  - Validate transaction data.
  - Interact with the data access layer to perform CRUD operations.
  - Handle any business rules related to transactions.

#### Key Methods:
- `create_transaction(account_id, date, payee=None, memo=None, category_id=None, payment=None, deposit=None, account_balance=None, note=None)`
- `get_transaction_by_id(transaction_id)`
- `get_all_transactions()`
- `update_transaction(transaction_id, account_id, date, payee=None, memo=None, category_id=None, payment=None, deposit=None, account_balance=None, note=None)`
- `delete_transaction(transaction_id)`
- `_validate_transaction_data(account_id)`

### 3. TransactionOperations

- **Location**: `src/data_access/db_transaction_operations.py`
- **Purpose**: Handles direct database interactions for transaction-related operations.
- **Responsibilities**:
  - Execute SQL queries for CRUD operations on transactions.
  - Interact with the DatabaseManager to perform database operations.

#### Key Methods:
- `create_transaction(account_id, date, payee, memo, category_id, payment, deposit, account_balance, note)`
- `get_transaction_by_id(transaction_id)`
- `get_all_transactions()`
- `update_transaction(transaction_id, account_id, date, payee, memo, category_id, payment, deposit, account_balance, note)`
- `delete_transaction(transaction_id)`

## Data Flow

1. User Interface (UI) interacts with `TransactionManager`.
2. `TransactionManager` delegates tasks to `TransactionService`.
3. `TransactionService` performs business logic and data validation.
4. `TransactionService` uses `TransactionOperations` for database interactions.
5. `TransactionOperations` executes SQL queries using `DatabaseManager`.

## Error Handling

- The `error_handler` decorator is used in `TransactionService` to ensure consistent error logging and handling across all transaction operations.
- Custom exceptions may be raised for specific error scenarios.

## Constants

Transaction-related constants (table names, field names, SQL queries) are centralized in `src/configs/constants.py` to maintain consistency and ease of modification.

## Transaction Fields

- `account_id`: The ID of the account associated with the transaction.
- `date`: The date of the transaction.
- `payee`: The entity to whom the payment was made or from whom the deposit was received.
- `memo`: A brief description of the transaction.
- `category_id`: The ID of the category associated with the transaction.
- `payment`: The amount paid (for outgoing transactions).
- `deposit`: The amount received (for incoming transactions).
- `account_balance`: The balance of the account after the transaction.
- `note`: Additional notes or details about the transaction.

## Best Practices

1. Always use `TransactionManager` for transaction-related operations in the UI or other high-level components.
2. Implement new business rules or validations in `TransactionService`.
3. Ensure that account balances are updated correctly when creating or modifying transactions.
4. Consider implementing additional methods for filtering transactions (e.g., by date range, category, or account).
5. When deleting a transaction, make