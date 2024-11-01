# Category Management Documentation

This document provides an overview of the category management system implemented in the Simple Family Budget Tracking App.

## Overview

The category management system is responsible for handling all operations related to budget categories. It supports a hierarchical structure, allowing for main categories and subcategories.

## Components

### 1. CategoryManager

- **Location**: `src/controllers/category_manager.py`
- **Purpose**: Serves as the main coordinator for category-related operations.
- **Responsibilities**:
  - Coordinate category creation, retrieval, updating, and deletion.
  - Act as an interface between the UI layer and the business logic layer.

#### Methods:
- `create_category(category_name, parent_id=None)`
  - Coordinates the creation of a new category or subcategory.

- `get_category_by_id(category_id)`
  - Coordinates retrieving a category by its ID.

- `get_all_categories()`
  - Coordinates retrieving all categories.

- `update_category(category_id, category_name, parent_id=None)`
  - Coordinates updating an existing category.

- `delete_category(category_id)`
  - Coordinates deleting a category by its ID.

- `get_subcategories(parent_id)`
  - Coordinates retrieving subcategories for a given parent category.

### 2. CategoryService

- **Location**: `src/controllers/services/category_service.py`
- **Purpose**: Implements the business logic for category operations.
- **Responsibilities**:
  - Validate category data.
  - Interact with the data access layer to perform CRUD operations.
  - Handle any business rules related to categories.

#### Key Methods:
- `create_category(category_name, parent_id=None)`
- `get_category_by_id(category_id)`
- `get_all_categories()`
- `update_category(category_id, category_name, parent_id=None)`
- `delete_category(category_id)`
- `get_subcategories(parent_id)`
- `_validate_category_data(category_name)`

### 3. CategoryOperations

- **Location**: `src/data_access/db_category_operations.py`
- **Purpose**: Handles direct database interactions for category-related operations.
- **Responsibilities**:
  - Execute SQL queries for CRUD operations on categories.
  - Interact with the DatabaseManager to perform database operations.

#### Key Methods:
- `create_category(category_name, parent_id=None)`
- `get_category_by_id(category_id)`
- `get_all_categories()`
- `update_category(category_id, category_name, parent_id=None)`
- `delete_category(category_id)`
- `get_subcategories(parent_id)`

## Data Flow

1. User Interface (UI) interacts with `CategoryManager`.
2. `CategoryManager` delegates tasks to `CategoryService`.
3. `CategoryService` performs business logic and data validation.
4. `CategoryService` uses `CategoryOperations` for database interactions.
5. `CategoryOperations` executes SQL queries using `DatabaseManager`.

## Error Handling

- The `error_handler` decorator is used in `CategoryService` to ensure consistent error logging and handling across all category operations.
- Custom exceptions may be raised for specific error scenarios.

## Constants

Category-related constants (table names, field names, SQL queries) are centralized in `src/configs/constants.py` to maintain consistency and ease of modification.

## Hierarchical Structure

- Categories can have a parent-child relationship.
- The `parent_id` field in the Categories table allows for creating subcategories.
- The `get_subcategories` method facilitates retrieving child categories for a given parent.

## Best Practices

1. Always use `CategoryManager` for category-related operations in the UI or other high-level components.
2. Implement new business rules or validations in `CategoryService`.
3. Be cautious when deleting categories, as it may affect related data (e.g., transactions or expenses linked to the category).
4. Consider implementing additional checks to prevent circular references in the category hierarchy.
5. When displaying categories, consider implementing a method to retrieve the full hierarchy for better user experience.

## Conclusion

This category management system provides a flexible and maintainable structure for handling all category-related operations in the Simple Family Budget Tracking App. Its support for hierarchical categories allows for detailed budget organization, while the layered architecture ensures ease of maintenance and extensibility.