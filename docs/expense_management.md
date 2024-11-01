# Expense Management Documentation

This document provides an overview of the expense management system implemented in the Simple Family Budget Tracking App.

## Overview

The expense management system is responsible for handling all operations related to recurring expenses or bills. It allows for creating, retrieving, updating, and deleting expense records, which are crucial for budgeting and financial planning.

## Components

### 1. ExpenseManager

- **Location**: `src/controllers/expense_manager.py`
- **Purpose**: Serves as the main coordinator for expense-related operations.
- **Responsibilities**:
  - Coordinate expense creation, retrieval, updating, and deletion.
  - Act as an interface between the UI layer and the business logic layer.

#### Methods:
- `create_expense(expense_name, category_id, due_date, frequency, amount)`
  - Coordinates the creation of a new expense.

- `get_expense_by_id(expense_id)`
  - Coordinates retrieving an expense by its ID.

- `get_all_expenses()`
  - Coordinates retrieving all expenses.

- `update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)`
  - Coordinates updating an existing expense.

- `delete_expense(expense_id)`
  - Coordinates deleting an expense by its ID.

### 2. ExpenseService

- **Location**: `src/controllers/services/expense_service.py`
- **Purpose**: Implements the business logic for expense operations.
- **Responsibilities**:
  - Validate expense data.
  - Interact with the data access layer to perform CRUD operations.
  - Handle any business rules related to expenses.

#### Key Methods:
- `create_expense(expense_name, category_id, due_date, frequency, amount)`
- `get_expense_by_id(expense_id)`
- `get_all_expenses()`
- `update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)`
- `delete_expense(expense_id)`
- `_validate_expense_data(expense_name, amount)`

### 3. ExpenseOperations

- **Location**: `src/data_access/db_expense_operations.py`
- **Purpose**: Handles direct database interactions for expense-related operations.
- **Responsibilities**:
  - Execute SQL queries for CRUD operations on expenses.
  - Interact with the DatabaseManager to perform database operations.

#### Key Methods:
- `create_expense(expense_name, category_id, due_date, frequency, amount)`
- `get_expense_by_id(expense_id)`
- `get_all_expenses()`
- `update_expense(expense_id, expense_name, category_id, due_date, frequency, amount)`
- `delete_expense(expense_id)`

## Data Flow

1. User Interface (UI) interacts with `ExpenseManager`.
2. `ExpenseManager` delegates tasks to `ExpenseService`.
3. `ExpenseService` performs business logic and data validation.
4. `ExpenseService` uses `ExpenseOperations` for database interactions.
5. `ExpenseOperations` executes SQL queries using `DatabaseManager`.

## Error Handling

- The `error_handler` decorator is used in `ExpenseService` to ensure consistent error logging and handling across all expense operations.
- Custom exceptions may be raised for specific error scenarios.

## Constants

Expense-related constants (table names, field names, SQL queries) are centralized in `src/configs/constants.py` to maintain consistency and ease of modification.

## Expense Fields

- `expense_name`: The name of the expense (e.g., "Rent", "Electricity Bill").
- `category_id`: The ID of the category associated with the expense.
- `due_date`: The date when the expense is due.
- `frequency`: How often the expense occurs (e.g., "Monthly", "Annually").
- `amount`: The amount of the expense.

## Data Validation

The `_validate_expense_data` method in `ExpenseService` performs the following checks:
- Ensures that the expense name is not empty.
- Verifies that the amount is a non-negative number.

Additional validation can be implemented as needed.

## Best Practices

1. Always use `ExpenseManager` for expense-related operations in the UI or other high-level components.
2. Implement new business rules or validations in `ExpenseService`.
3. Consider implementing additional methods for filtering expenses (e.g., by category, due date, or frequency).
4. When creating or updating expenses, ensure that the associated category exists.
5. Implement proper data validation to ensure the integrity of expense data.
6. Consider adding functionality to generate recurring transactions based on expense records.

## Future Enhancements

1. Implement a notification system for upcoming expenses.
2. Add support for variable expenses (where the amount may change each occurrence).
3. Develop reporting features to analyze expense patterns over time.
4. Integrate with a budgeting feature to compare actual expenses against planned expenses.

## Conclusion

This expense management system provides a robust and flexible structure for handling all expense-related operations in the Simple Family Budget Tracking App. Its layered architecture ensures separation of concerns, making it easy to maintain and extend the functionality as the application grows. By tracking recurring expenses, users can better plan their finances and maintain a comprehensive view of their financial obligations.