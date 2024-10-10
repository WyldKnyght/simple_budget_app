# src/configs/path_config.py
import os
from dotenv import load_dotenv

load_dotenv()

class EnvSettings:
    SETTINGS = {
        'PROJECT_ROOT': 'PROJECT_ROOT',
        'ENTRY_POINT': 'ENTRY_POINT',
        'DB_PATH': 'DB_PATH',
        'SCHEMA_PATH': 'SCHEMA_PATH',
        'DEFAULT_SETTINGS_PATH': 'DEFAULT_SETTINGS_PATH',
        'UI_INI_PATH': 'UI_INI_PATH'
    }

    def __init__(self):
        for attr, env_var in self.SETTINGS.items():
            setattr(self, attr, os.getenv(env_var))

env_settings = EnvSettings()

# Expose the settings at the module level
for attr in EnvSettings.SETTINGS:
    globals()[attr] = getattr(env_settings, attr)