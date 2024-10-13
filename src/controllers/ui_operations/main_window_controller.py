# src/controllers/ui_operations/main_window_controller.py
from PyQt6.QtWidgets import QMessageBox, QMainWindow, QApplication
from services.database_reset_service import DatabaseResetService
from utils.custom_logging import logger
from configs.settings_manager import SettingsManager
from controllers.db_operations.database_manager import DatabaseManager

class MainWindowController:
    def __init__(self, window: QMainWindow, db_manager: DatabaseManager, settings_tab_controller):
        self.window = window
        self.db_manager = db_manager
        self.settings_tab_controller = settings_tab_controller
        self.settings_manager = SettingsManager()
        self.reset_service = DatabaseResetService(db_manager)

    def load_settings(self):
        try:
            self.settings_manager.load_window_settings(self.window)
            logger.info("Main window settings loaded successfully")
        except Exception as e:
            logger.error(f"Error loading main window settings: {e}")

    def save_settings(self):
        try:
            self.settings_manager.save_window_settings(self.window)
            logger.info("Main window settings saved successfully")
        except Exception as e:
            logger.error(f"Error saving main window settings: {e}")

    def reset_database(self, progress_dialog):
        try:
            for progress, total_steps in self.reset_service.reset_database():
                if progress == 0:
                    progress_dialog.setMaximum(total_steps)
                progress_dialog.setValue(progress)
                QApplication.processEvents()
                if progress_dialog.wasCanceled():
                    break
            self.settings_tab_controller.refresh()
            logger.info("Database reset successfully")
        except Exception as e:
            logger.error(f"Error resetting database: {e}")
            QMessageBox.critical(self.window, "Error", f"Failed to reset database: {str(e)}")
        finally:
            progress_dialog.close()

    def validate_schema(self):
        try:
            if _is_valid := self.db_manager.schema_controller.validate_schema():
                QMessageBox.information(self.window, "Schema Validation", "Database schema is valid.")
            else:
                QMessageBox.warning(self.window, "Schema Validation", "Database schema is invalid. Would you like to apply changes?")
                self.apply_schema_changes()
        except Exception as e:
            logger.error(f"Error validating schema: {e}")
            QMessageBox.critical(self.window, "Error", f"Failed to validate schema: {str(e)}")

    def apply_schema_changes(self):
        try:
            success, message = self.db_manager.schema_controller.apply_schema_changes()
            if success:
                QMessageBox.information(self.window, "Schema Update", "Schema changes applied successfully.")
                self.settings_tab_controller.refresh()
            else:
                QMessageBox.critical(self.window, "Error", f"Failed to apply schema changes: {message}")
        except Exception as e:
            logger.error(f"Error applying schema changes: {e}")
            QMessageBox.critical(self.window, "Error", f"Failed to apply schema changes: {str(e)}")

    def backup_database(self):
        try:
            backup_path = self.settings_manager.get_backup_path()
            success, message = self.db_manager.schema_controller.backup_database(backup_path)
            if success:
                QMessageBox.information(self.window, "Backup", f"Database backed up successfully to {backup_path}")
            else:
                QMessageBox.critical(self.window, "Error", f"Failed to backup database: {message}")
        except Exception as e:
            logger.error(f"Error backing up database: {e}")
            QMessageBox.critical(self.window, "Error", f"Failed to backup database: {str(e)}")
    def show_about_dialog(self):
        QMessageBox.about(self.window, "About", "Family Expense and Income Tracker\nVersion 1.0")

    def exit_application(self):
        self.save_settings()
        self.window.close()