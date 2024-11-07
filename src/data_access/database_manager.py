# src/data_access/database_manager.py
from configs.path_config import DB_PATH, SCHEMA_PATH
from .db_modules.db_connections import DatabaseConnections
from .db_modules.db_initializer import DatabaseInitializer
from .db_modules.db_reset_database import ResetDatabase
from .db_modules.db_query_executor import QueryExecutor
from .db_modules.db_validation_operations import ValidationOperations
from .schema_manager import SchemaManager
from utils.custom_logging import logger

class DatabaseManager:
    def __init__(self):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = DatabaseConnections()
        self.schema_manager = SchemaManager()
        self.validation_operations = ValidationOperations(self)
        self.initializer = DatabaseInitializer(self.connections, self.validation_operations)
        self.reset_db = ResetDatabase(self.connections)
        self.executor = QueryExecutor(self.connections)

    def database_exists(self):
        return self.validation_operations.database_exists()

    def validate_schema(self):
        return self.validation_operations.validate_schema()

    def initialize_database(self):
        return self.initializer.initialize_database()

    def reset_database(self):
        logger.info("DatabaseManager: Attempting to reset database")
        return self.reset_db.reset_database()

    def get_connection(self):
        return self.connections.get_connection()
    
    def new_database(self):
        return self.initializer.new_database()

    def execute_query(self, query, params=None):
        return self.executor.execute_query(query, params)

    def refresh_schema_validator(self):
        self.validation_operations.refresh_schema_cache()
        
    def close_all_connections(self):
        self.connections.close_all_connections()