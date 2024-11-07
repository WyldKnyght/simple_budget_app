# src/controllers/message_manager.py
from controllers.services.message_service import MessageService
from data_access.message_modules.message_operations import MessageOperations

class MessageManager:
    def __init__(self):
        self.message_service = MessageService()
        self.message_operations = MessageOperations()

    def show_warning_message(self, parent, title, message):
        return self.message_service.show_warning_message(parent, title, message)

    def show_question_message(self, parent, title, message):
        return self.message_service.show_question_message(parent, title, message)

    def show_info_message(self, parent, title, message):
        return self.message_service.show_info_message(parent, title, message)

    def show_error_message(self, parent, title, message):
        return self.message_service.show_error_message(parent, title, message)

    def get_message(self, message_key):
        return self.message_operations.get_message(message_key)