# src/data_access/schema_modules/schema_operations.py
import re
from utils.custom_logging import logger, error_handler
from configs.path_config import SCHEMA_PATH

class SchemaOperations:
    def __init__(self):
        self.schema = None

    @error_handler
    def get_schema(self):
        if self.schema is None:
            self.schema = self.read_schema_file()
        return self.schema

    @error_handler
    def read_schema_file(self):
        logger.info(f"Reading schema file from {SCHEMA_PATH}")
        try:
            with open(SCHEMA_PATH, 'r') as file:
                content = file.read()
            logger.info("Schema file read successfully")
            return content
        except Exception as e:
            logger.error(f"Error reading schema file: {str(e)}")
            return None

    @error_handler
    def get_table_definitions(self):
        """Parse the schema and return a structured format of table definitions."""
        schema = self.get_schema()
        if not schema:
            return None

        table_definitions = {}
        table_pattern = re.compile(r'CREATE TABLE (\w+) \((.*?)\);', re.DOTALL)
        column_pattern = re.compile(r'(\w+)\s+([^,\n]+)')

        for match in table_pattern.finditer(schema):
            table_name = match.group(1)
            table_content = match.group(2)
            columns = []

            for col_match in column_pattern.finditer(table_content):
                col_name = col_match.group(1)
                col_type = col_match.group(2).split()[0]  # Get only the type, not constraints
                if col_name.upper() != 'FOREIGN':  # Ignore FOREIGN KEY definitions
                    columns.append({'name': col_name, 'type': col_type})

            table_definitions[table_name] = columns

        return table_definitions

    
    @error_handler
    def get_table_names(self):
        schema = self.get_schema()
        if not schema:
            return []
        table_names = []
        for line in schema.split('\n'):
            if line.strip().startswith('CREATE TABLE'):
                table_name = line.split('(')[0].split()[-1]
                table_names.append(table_name)
        return table_names

    @error_handler
    def get_table_columns(self, table_name):
        schema = self.get_schema()
        if not schema:
            return None
        start_index = schema.find(f"CREATE TABLE {table_name}")
        if start_index == -1:
            return None
        end_index = schema.find(');', start_index)
        table_schema = schema[start_index:end_index]
        return [
            line.strip().split()[0]
            for line in table_schema.split('\n')[1:]
            if line.strip() and not line.strip().startswith('FOREIGN KEY')
        ]