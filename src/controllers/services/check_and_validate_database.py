# src/controllers/services/check_and_validate_database.py
from data_access.database_manager import DatabaseManager
from PyQt6.QtWidgets import QMessageBox

class CheckAndValidateDatabase:
    ''' Check And Validate Database Service, coordinates validation and database business logic, data access and UI for the main window manager. '''
    def __init__(self):
        self.db_manager = DatabaseManager()

    def check_and_validate(self, parent):
        try:
            if not self.db_manager.schema_validator.database_exists():
                return self.handle_non_existent_database(parent)
            elif not self.db_manager.validate_schema():
                return self.handle_invalid_schema(parent)
            return True
        finally:
            self.db_manager.close_all_connections()

    def handle_non_existent_database(self, parent):
        if self.prompt_create_database(parent):
            self.db_manager.initialize_database()
            print("New database created")
            return True
        self.show_warning_message(parent)
        return False

    def handle_invalid_schema(self, parent):
        if self.prompt_reset_database(parent):
            success, message = self.db_manager.reset_database()
            if success:
                print("Database reset")
                return True
            else:
                self.show_warning_message(parent)
                return False
        self.show_warning_message(parent)
        return False

    def show_warning_message(self, parent, custom_message=None):
        message = custom_message or 'The application may not function correctly without a valid database. You can manually reset the database or make other changes as needed.'
        QMessageBox.warning(parent, 'Database Issue', message)

    def prompt_create_database(self, parent):
        return QMessageBox.question(parent, 'Create Database', 
                                    'No database found. Would you like to create a new one?',
                                    QMessageBox.StandardButton.Yes | 
                                    QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.Yes) == QMessageBox.StandardButton.Yes

    def prompt_reset_database(self, parent):
        return QMessageBox.warning(parent, 'Outdated Database', 
                                   'The database schema is outdated. Some features may not work. '
                                   'Would you like to reset the database? '
                                   'Warning: This will delete all existing data.',
                                   QMessageBox.StandardButton.Yes | 
                                   QMessageBox.StandardButton.No,
                                   QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes