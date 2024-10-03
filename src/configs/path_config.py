# src/configs/path_config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class EnvSettings:
    # Root Folder
    PROJECT_ROOT = os.getenv('PROJECT_ROOT')

    # Application Entrypoint
    ENTRY_POINT = os.getenv('ENTRY_POINT')

    # Database
    DB_PATH = os.getenv('DB_PATH')
    SCHEMA_PATH = os.getenv('SCHEMA_PATH')

    # Default Settings
    DEFAULT_SETTINGS_PATH = os.getenv('DEFAULT_SETTINGS_PATH')

# Expose the settings at the module level
PROJECT_ROOT = EnvSettings.PROJECT_ROOT
ENTRY_POINT = EnvSettings.ENTRY_POINT
DB_PATH = EnvSettings.DB_PATH
SCHEMA_PATH = EnvSettings.SCHEMA_PATH
DEFAULT_SETTINGS_PATH = EnvSettings.DEFAULT_SETTINGS_PATH