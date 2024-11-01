# src/data_access/schema_manager.py
from utils.custom_logging import error_handler
from .schema_operations import get_schema, get_table_names, get_table_columns

class SchemaManager:
    def __init__(self):
        self.schema = None

    @error_handler
    def load_schema(self):
        self.schema = get_schema()

    @error_handler
    def get_table_names(self):
        if self.schema is None:
            self.load_schema()
        return get_table_names(self.schema)

    @error_handler
    def get_table_columns(self, table_name):
        if self.schema is None:
            self.load_schema()
        return get_table_columns(self.schema, table_name)