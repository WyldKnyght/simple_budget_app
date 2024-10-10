# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_model.py
from PyQt6.QtCore import Qt, QAbstractTableModel

class AccountsModel(QAbstractTableModel):
    """A model for the accounts table."""
    def __init__(self, accounts, columns):
        """Initialize the model."""
        super().__init__()
        self._accounts_list = accounts
        self._column_definitions = columns
        self._column_indices = {col['name']: i for i, col in enumerate(columns)}
        self._header_names = [col['name'] for col in columns if col['name'].lower() != 'id']

    def data(self, index, role):
        """Get data for the given index and role."""
        if role == Qt.ItemDataRole.DisplayRole:
            column_name = self._header_names[index.column()]
            return self._accounts_list[index.row()][self._column_indices[column_name]]
    
    def row_count(self, parent):
        """Get the number of rows in the model."""
        return len(self._accounts_list)

    def column_count(self, parent):
        """Get the number of columns in the model."""
        return len(self._header_names)

    def header_data(self, section, orientation, role):
        """Get header data for the given section, orientation, and role."""
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._header_names[section]

