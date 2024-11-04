# src/data_access/database_manager.py
from .db_connections import DatabaseConnections
from .db_initializer import DatabaseInitializer
from .db_loader import DatabaseLoader
from .db_query_executor import QueryExecutor
from .db_validation_operations import ValidationOperations
from .schema_manager import SchemaManager

class DatabaseManager:
    def __init__(self):
        self.connections = DatabaseConnections()
        self.schema_manager = SchemaManager()
        self.validation_operations = ValidationOperations(self)
        self.initializer = DatabaseInitializer(self.connections, self.validation_operations)
        self.executor = QueryExecutor(self.connections)
        self.loader = DatabaseLoader(self)

    def get_connection(self):
        return self.connections.get_connection()

    def initialize_database(self):
        self.initializer.initialize_database()

    def load_database(self):
        return self.loader.load_database()

    def new_database(self):
        return self.initializer.new_database()

    def reset_database(self):
        return self.initializer.reset_database()

    def execute_query(self, query, params=None):
        return self.executor.execute_query(query, params)
    
    def validate_schema(self):
        return self.validation_operations.validate_schema()

    def refresh_schema_validator(self):
        self.validation_operations.refresh()
        
    def close_all_connections(self):
        self.connections.close_all_connections()