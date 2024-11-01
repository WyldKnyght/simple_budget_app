# src/data_access/schema_operations.py
from utils.custom_logging import logger
from configs.path_config import SCHEMA_PATH

def get_schema():
    try:
        with open(SCHEMA_PATH, 'r') as schema_file:
            return schema_file.read()
    except IOError as e:
        logger.error(f"Error reading schema file: {e}")
        raise

def get_table_names(schema):
    table_names = []
    for line in schema.split('\n'):
        if line.strip().startswith('CREATE TABLE'):
            table_name = line.split('(')[0].split()[-1]
            table_names.append(table_name)
    return table_names

def get_table_columns(schema, table_name):
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