# src/controllers/db_operations/database_operations.py
from typing import Any
from utils.custom_logging import logger
from ..settings_tab_controllers.accounts_controller import AccountsController
from ..settings_tab_controllers.categories_controller import CategoriesController
from ..settings_tab_controllers.expenses_controller import ExpensesController
from services.database_reset_service import DatabaseResetService

class DatabaseOperations:
    @staticmethod
    def initialize_database(db_manager: Any) -> None:
        """Initialize the database by registering necessary operations."""
        try:
            db_manager.register_operation('accounts', AccountsController(db_manager))
            db_manager.register_operation('categories', CategoriesController(db_manager))
            db_manager.register_operation('expenses', ExpensesController(db_manager))
            logger.info("Database operations initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database operations: {e}")
            raise

    @staticmethod
    def reset_database(db_manager: Any) -> None:
        """Reset the database to its initial state."""
        try:
            reset_service = DatabaseResetService(db_manager)
            reset_service.reset_database()
            logger.info("Database reset successfully")
        except Exception as e:
            logger.error(f"Error resetting database: {e}")
            raise

    @staticmethod
    def validate_database_structure(db_manager: Any) -> bool:
        """Validate the database structure against the schema."""
        try:
            schema_controller = db_manager.schema_controller
            return schema_controller.validate_schema()
        except Exception as e:
            logger.error(f"Error validating database structure: {e}")
            return False