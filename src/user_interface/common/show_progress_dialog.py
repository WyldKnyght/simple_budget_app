# src/user_interface/common/show_progress_dialog

from PyQt6.QtWidgets import QProgressDialog
from PyQt6.QtCore import Qt

def show_progress_dialog(parent, title, message, max_value):
    progress = QProgressDialog(message, "Cancel", 0, max_value, parent)
    progress.setWindowTitle(title)
    progress.setWindowModality(Qt.WindowModality.WindowModal)
    progress.setMinimumDuration(0)
    progress.setValue(0)
    progress.show()
    return progress