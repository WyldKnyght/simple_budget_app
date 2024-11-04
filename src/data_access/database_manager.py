# src\data_access\database_manager.py
from configs.path_config import DB_PATH, SCHEMA_PATH
from .db_connections import DatabaseConnections
from .db_initializer import DatabaseInitializer
from .db_loader import DatabaseLoader
from .db_query_executor import QueryExecutor
from .db_schema_validator import SchemaValidator
from .schema_manager import SchemaManager

class DatabaseManager:
    ''' Database Manager Cordinates all data access codes. No defined functions, imports only. '''
    def __init__(self):
        self.db_path = DB_PATH
        self.schema_path = SCHEMA_PATH
        self.connections = DatabaseConnections()
        self.schema_manager = SchemaManager()
        self.schema_validator = SchemaValidator(self)
        self.initializer = DatabaseInitializer(self.connections, self.schema_validator)
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
        return self.schema_validator.validate_schema()

    def refresh_schema_validator(self):
        self.schema_validator.refresh()
        
    def close_all_connections(self):
        self.connections.close_all_connections()