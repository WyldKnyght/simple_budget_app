# src/controllers/tab_operations/settings_tab_controller.py
from utils.custom_logging import logger
from typing import List, Dict, Any

class SettingsTabController:
    def __init__(self, db_manager):
        self.db_manager = db_manager
        self.entities = {
            'accounts': [],
            'categories': [],
            'expenses': []
        }

    def refresh(self):
        """Refresh all data in the settings tab."""
        logger.info("Refreshing settings tab data")
        for entity_type in self.entities:
            self.refresh_entity(entity_type)

    def refresh_entity(self, entity_type: str):
        """Refresh data for a specific entity type."""
        logger.info(f"Refreshing {entity_type} data")
        controller = self.db_manager.get_operation(entity_type)
        self.entities[entity_type] = controller.get_entities()
        logger.info(f"Retrieved {len(self.entities[entity_type])} {entity_type}")

    def get_category_tree(self):
        return self.db_manager.get_operation('categories').get_category_tree()

    def format_account_display(self, account):
        return f"{account['account_name']} ({account['account_number']})"

    def format_expense_display(self, expense):
        return f"{expense['expense_name']} - {expense['amount']} (Due: {expense['due_date']})"

    def get_entities(self, entity_type: str) -> List[Dict[str, Any]]:
        return self.entities[entity_type]

    def perform_entity_operation(self, operation: str, entity_type: str, entity_id: int = None, entity_data: Dict[str, Any] = None):
        controller = self.db_manager.get_operation(entity_type)
        if operation == 'add':
            return controller.add_entity(entity_data)
        elif operation == 'update':
            return controller.update_entity(entity_id, entity_data)
        elif operation == 'delete':
            return controller.remove_entity(entity_id)
        else:
            raise ValueError(f"Unknown operation: {operation}")

    def add_entity(self, entity_type: str, entity_data: Dict[str, Any]):
        return self.perform_entity_operation('add', entity_type, entity_data=entity_data)

    def update_entity(self, entity_type: str, entity_id: int, entity_data: Dict[str, Any]):
        return self.perform_entity_operation('update', entity_type, entity_id, entity_data)

    def delete_entity(self, entity_type: str, entity_id: int):
        return self.perform_entity_operation('delete', entity_type, entity_id)

    def get_table_info(self, table_name: str) -> Dict[str, Any]:
        return self.db_manager.schema_controller.get_table_info(table_name)

logger.info("SettingsTabController initialized")