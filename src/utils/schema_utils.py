# src/utils/schema_utils.py
import re
from configs.path_config import SCHEMA_PATH

def get_table_names_from_schema():
    with open(SCHEMA_PATH, 'r') as schema_file:
        schema = schema_file.read()
    table_pattern = r'CREATE TABLE (\w+)'
    return re.findall(table_pattern, schema)

def get_table_name_by_prefix(prefix):
    table_names = get_table_names_from_schema()
    return next((name for name in table_names if name.lower().startswith(prefix.lower())), None)