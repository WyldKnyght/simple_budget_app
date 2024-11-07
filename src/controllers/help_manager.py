# src/controllers/help_manager.py

from .services.help_service import HelpService
from utils.custom_logging import logger

class HelpManager:
    def __init__(self, message_manager):
        self.help_service = HelpService()
        self.message_manager = message_manager

    def show_help(self, topic='main_window_ui'):
        logger.info(f"Showing help for topic: {topic}")
        if self.help_service.open_help_topic(topic):
            self.message_manager.show_info_message(None, "Help", f"Opened help for: {topic}")
        else:
            self.message_manager.show_error_message(None, "Help Error", f"Help documentation not found for: {topic}")

    def get_available_help_topics(self):
        return self.help_service.get_available_topics()