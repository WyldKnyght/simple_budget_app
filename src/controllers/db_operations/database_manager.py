# src/controllers/db_operations/database_manager.py
from .database_connection import DatabaseConnection
from .query_executor import QueryExecutor
from .operation_registry import OperationRegistry
from configs.path_config import DB_PATH, SCHEMA_PATH

class DatabaseManager:
    def __init__(self):
        self.connection = DatabaseConnection(DB_PATH)
        self.query_executor = QueryExecutor(self.connection)
        self.operation_registry = OperationRegistry()
        self.schema_path = SCHEMA_PATH

    def connect(self):
        self.connection.connect()

    def close(self):
        self.connection.close()

    def register_operation(self, name: str, operation: callable):
        self.operation_registry.register(name, operation)
        
    def get_operation(self, name: str) -> callable:
        return self.operation_registry.get(name)

    def execute_query(self, query: str, params: tuple = ()):
        return self.query_executor.execute(query, params)

    def fetch_one(self, query: str, params: tuple = ()):
        return self.query_executor.fetch_one(query, params)

    def fetch_all(self, query: str, params: tuple = ()):
        return self.query_executor.fetch_all(query, params)