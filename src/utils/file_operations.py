# src/utils/file_operations.py

from utils.custom_logging import logger, error_handler
from configs.messages_config import SCHEMA_FILE_READ_ERROR

@error_handler
def read_schema_file(schema_path):
    try:
        with open(schema_path, 'r') as schema_file:
            return schema_file.read()
    except IOError as e:
        logger.error(f"Error reading schema file: {e}")
        raise IOError(SCHEMA_FILE_READ_ERROR.format(str(e))) from e