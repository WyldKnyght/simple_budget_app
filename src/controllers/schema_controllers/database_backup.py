# src/controllers/schema_controllers/database_backup.py
import sqlite3
from typing import Tuple
from utils.custom_logging import logger

class DatabaseBackup:
    @staticmethod
    def backup_database(db_ops, backup_path: str) -> Tuple[bool, str]:
        try:
            with db_ops.get_connection() as conn:
                with sqlite3.connect(backup_path) as backup_conn:
                    conn.backup(backup_conn)
            logger.info(f"Database backed up to {backup_path}")
            return True, f"Database backed up successfully to {backup_path}"
        except Exception as e:
            logger.error(f"Error backing up database: {e}")
            return False, f"Failed to backup database: {str(e)}"