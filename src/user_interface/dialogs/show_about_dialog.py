# src/user_interface/dialogs/show_about_dialog.py
from PyQt6.QtWidgets import QMessageBox
from configs.app_constants import APP_TITLE, APP_VERSION

def show_about_dialog(parent):
    QMessageBox.about(parent, "About", f"{APP_TITLE}\nVersion {APP_VERSION}")