# src/configs/app_config.py

import os
from dotenv import load_dotenv
from utils.custom_logging import logger

load_dotenv()

def get_env_path(env_var):
    if path := os.getenv(env_var):
        return os.path.abspath(os.path.join(DATABASE_DIR, path))
    else:
        raise ValueError(f"{env_var} not set in .env file")

DATABASE_DIR = os.getenv('DATABASE_DIR')
DATABASE_NAME = get_env_path('DATABASE_NAME')
DATABASE_PATH = get_env_path('DATABASE_PATH')
SCHEMA_FILE_PATH = get_env_path('SCHEMA_FILE_PATH')

logger.debug(f"DATABASE_DIR: {DATABASE_DIR}")
logger.debug(f"DATABASE_NAME: {DATABASE_NAME}")
logger.debug(f"DATABASE_PATH: {DATABASE_PATH}")
logger.debug(f"SCHEMA_FILE_PATH: {SCHEMA_FILE_PATH}")