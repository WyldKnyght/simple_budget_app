from PyQt6.QtWidgets import QMessageBox

class MessageService:
    def show_warning_message(self, parent, title, message):
        return QMessageBox.warning(parent, title, message)

    def show_question_message(self, parent, title, message):
        return QMessageBox.question(parent, title, message,
                                    QMessageBox.StandardButton.Yes | 
                                    QMessageBox.StandardButton.No,
                                    QMessageBox.StandardButton.No)

    def show_info_message(self, parent, title, message):
        return QMessageBox.information(parent, title, message)