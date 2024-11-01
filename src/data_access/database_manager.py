# src\data_access\database_manager.py
from configs.path_config import DB_PATH, SCHEMA_PATH
from .db_connections import DatabaseConnections
from .db_initializer import DatabaseInitializer
from .db_query_executor import QueryExecutor
from utils.custom_logging import error_handler

class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = DatabaseConnections()
        self.initializer = DatabaseInitializer()
        self.executor = QueryExecutor()

    @error_handler
    def get_connection(self):
        return self.connections.get_connection()

    @error_handler
    def initialize_database(self):
        self.initializer.initialize_database()

    @error_handler
    def execute_query(self, query, params=None):
        return self.executor.execute_query(query, params)