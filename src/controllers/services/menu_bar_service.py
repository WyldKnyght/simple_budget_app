# src/controllers/services/menu_bar_service.py

class MenuBarService:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def load_database(self):
        success, message = self.db_manager.load_database()
        if success:
            print("Database loaded successfully")
        else:
            print(f"Failed to load database: {message}")
        return success

    def new_database(self):
        if not self.db_manager.schema_validator.database_exists():
            success = self.db_manager.initialize_database()
            if success:
                print("New database created successfully")
            else:
                print("Failed to create new database")
            return success
        else:
            print("Database already exists. Use reset_database to create a new one.")
            return False

    def reset_database(self):
        success, message = self.menu_bar_service.reset_database()
        if success:
            # Refresh the UI or perform any necessary updates
            self.refresh_ui()
        else:
            # Show error message to the user
            self.show_error_message(message)
        return success