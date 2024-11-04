# Main Window Documentation

This document provides an overview of the main window implementation in the Simple Family Budget Tracking App.

## Overview

The main window serves as the primary interface for the application, managing the overall layout, tab structure, and menu bar. It coordinates with various controllers and services to handle database operations and user interactions.

## Components

### 1. MainWindow

- **Purpose**: Serves as the main application window.
- **Responsibilities**:
  - Initialize the user interface.
  - Manage tab structure.
  - Handle database validation on startup.

#### Methods:
- `__init__()`
  - Initializes the main window, sets up the UI controller, and checks the database.

- `check_and_validate_database()`
  - Validates the database on application startup.
  - Shows a warning if the database is invalid or missing.

- `init_ui()`
  - Sets up the main layout and tab structure.
  - Creates placeholder tabs for different sections of the app.

- `create_placeholder_tab()`
  - Creates a placeholder widget for each tab.

---

### 2. MainWindowManager

- **Purpose**: Manages the business logic for the main window.
- **Responsibilities**:
  - Coordinate database operations.
  - Handle menu actions.

#### Methods:
- `check_and_validate_database(parent)`
  - Delegates database validation to the CheckAndValidateDatabase service.

- `load_database()`, `new_database()`, `reset_database()`
  - Delegate respective database operations to the MenuBarService.

- `show_about(parent)`, `show_help()`
  - Handle "About" dialog and help functionality.

---

### 3. MenuBarBuilder

- **Purpose**: Constructs and manages the application's menu bar.
- **Responsibilities**:
  - Create menu structure.
  - Connect menu actions to corresponding functions.

#### Methods:
- `build()`
  - Constructs the entire menu bar.

- `create_file_menu()`, `create_tools_menu()`, `create_help_menu()`
  - Create respective menu sections.

- `connect_actions()`
  - Links menu items to their corresponding functions.

- `update_menu_state()`
  - Updates the enabled/disabled state of menu items based on database status.

---

### 4. CheckAndValidateDatabase

- **Purpose**: Handles database validation and user prompts for database operations.
- **Responsibilities**:
  - Check database existence and validity.
  - Prompt user for database creation or reset.

#### Key Methods:
- `check_and_validate(parent)`
  - Main method to check and validate the database.

- `handle_non_existent_database(parent)`, `handle_invalid_schema(parent)`
  - Handle cases of missing or invalid databases.

---

### 5. MenuBarService

- **Purpose**: Handles menu bar-related operations.
- **Responsibilities**:
  - Manage database loading, creation, and reset operations.

#### Key Methods:
- `load_database()`, `new_database()`, `reset_database()`
  - Handle respective database operations.

## Best Practices

1. Keep UI logic separate from business logic.
2. Use services for complex operations like database checks and menu actions.
3. Maintain a clear separation of concerns between different components.

## Conclusion

This documentation provides an overview of the main window implementation in the Simple Family Budget Tracking App. It outlines the key components and their responsibilities in managing the application's primary interface and core functionalities.
