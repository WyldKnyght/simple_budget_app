# src/data_access/schema_manager.py

from .schema_modules.schema_operations import SchemaOperations

class SchemaManager:
    def __init__(self):
        self.schema_operations = SchemaOperations()

    def load_schema(self):
        return self.schema_operations.get_schema()

    def get_table_names(self):
        return self.schema_operations.get_table_names()

    def get_table_columns(self, table_name):
        return self.schema_operations.get_table_columns(table_name)

    def get_table_definitions(self):
        return self.schema_operations.get_table_definitions()