# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_dialog.py
from utils.custom_logging import logger, error_handler
from ...common.base_dialog import BaseDialog

class AccountDialog(BaseDialog):
    def __init__(self, parent=None, columns=None, account_data=None):
        super().__init__(parent, columns)
        self.setWindowTitle("Add/Edit Account")
        self.account_data = account_data
        self.init_ui()
        if self.account_data:
            self.populate_fields()

    def init_ui(self):
        super().init_ui()  # Call the parent's init_ui method
        self.setWindowTitle("Add/Edit Account")

    def populate_fields(self):
        for name, input_field in self.inputs.items():
            if name in self.account_data:
                input_field.setText(str(self.account_data[name]))

    @error_handler
    def get_data(self):
        logger.info("Getting account data")
        return super().get_data()  # Use the parent's get_data method