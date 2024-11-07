# src/controllers/menu_bar_manager.py

from .services.menu_bar_service import MenuBarService

class MenuBarManager:
    def __init__(self, db_manager, message_manager):
        self.menu_bar_service = MenuBarService(db_manager, message_manager)

    def reset_database(self):
        return self.menu_bar_service.reset_database()

    def show_about(self, parent):
        return self.menu_bar_service.show_about(parent)
