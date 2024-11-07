# src/controllers/services/message_service.py
from PyQt6.QtWidgets import QMessageBox
from utils.custom_logging import logger

class MessageService:
    def show_warning_message(self, parent, title, message):
        logger.info(f"Displaying Warning: {title} - {message}")
        return QMessageBox.warning(parent, title, message)

    def show_question_message(self, parent, title, message):
        logger.info(f"Displaying Question: {title} - {message}") 
        return QMessageBox.question(parent, title, message,
                                    QMessageBox.StandardButton.Yes | 
                                    QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.No)

    def show_info_message(self, parent, title, message):
        logger.info(f"Displaying Info: {title} - {message}")
        return QMessageBox.information(parent, title, message)

    def show_error_message(self, parent, title, message):
        logger.error(f"Displaying Error: {title} - {message}")
        return QMessageBox.critical(parent, title, message)