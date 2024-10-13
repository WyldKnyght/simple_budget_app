# src/controllers/db_operations/database_manager.py

from .database_connection import DatabaseConnection
from .query_executor import QueryExecutor
from .operation_registry import OperationRegistry
from ..schema_controllers.schema_manager import SchemaManager
from configs.path_config import DB_PATH, SCHEMA_PATH
from utils.custom_logging import logger
from typing import Any, Tuple, List, Optional, Dict

class DatabaseManager:
    def __init__(self):
        self.connection = DatabaseConnection(DB_PATH)
        self.query_executor = QueryExecutor(self.connection)
        self.operation_registry = OperationRegistry()
        self.connect()
        self.schema_controller = SchemaManager(self)
        self.schema_path = SCHEMA_PATH
        self._initialize_schema()

    def connect(self):
        self.connection.connect()

    def close(self):
        self.connection.close()

    def _initialize_schema(self):
        with self.get_connection():  # Ensure connection is open
            success, message = self.schema_controller.apply_schema_changes()
            if not success:
                logger.error(f"Failed to initialize schema: {message}")

    def initialize_operations(self):
        from .database_initializer import DatabaseInitializer
        DatabaseInitializer.initialize_database(self)

    def register_operation(self, name: str, operation: callable):
        self.operation_registry.register(name, operation)
        
    def get_operation(self, name: str) -> Optional[callable]:
        return self.operation_registry.get(name)

    def execute_query(self, query: str, params: Tuple[Any, ...] = ()) -> Any:
        try:
            return self.connection.execute_query(query, params)
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            raise

    def fetch_one(self, query: str, params: Tuple[Any, ...] = ()) -> Optional[Tuple[Any, ...]]:
        try:
            return self.query_executor.fetch_one(query, params)
        except Exception as e:
            logger.error(f"Error fetching one row: {e}")
            raise

    def fetch_all(self, query: str, params: Tuple[Any, ...] = ()) -> List[Tuple[Any, ...]]:
        try:
            return self.query_executor.fetch_all(query, params)
        except Exception as e:
            logger.error(f"Error fetching all rows: {e}")
            raise

    def table_exists(self, table_name: str) -> bool:
        return self.schema_controller.table_exists(table_name)

    def get_columns(self, table_name: str) -> List[Dict[str, Any]]:
        return self.schema_controller.get_columns(table_name)

    def get_foreign_keys(self, table_name: str) -> List[Dict[str, str]]:
        return self.schema_controller.get_foreign_keys(table_name)

    def get_table_names(self) -> List[str]:
        return self.connection.get_table_names()
    
    def get_connection(self):
        return self.connection.get_connection()