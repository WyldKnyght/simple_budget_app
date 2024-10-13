# src/user_interface/settings_tab_modules/accounts_tab_modules/accounts_model.py
from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex

class AccountsModel(QAbstractTableModel):
    CHUNK_SIZE = 100  # Number of rows to load at a time

    def __init__(self, accounts_controller, columns):
        super().__init__()
        self._accounts_controller = accounts_controller
        self._column_definitions = columns
        self._column_indices = {col['name']: i for i, col in enumerate(columns)}
        self._header_names = [col['name'] for col in columns if col['name'].lower() != 'id']
        self._loaded_data = []
        self._total_rows = self._accounts_controller.get_total_count()

    def canFetchMore(self, index):
        return len(self._loaded_data) < self._total_rows

    def fetchMore(self, index):
        remainder = self._total_rows - len(self._loaded_data)
        items_to_fetch = min(remainder, self.CHUNK_SIZE)
        self.beginInsertRows(QModelIndex(), len(self._loaded_data), len(self._loaded_data) + items_to_fetch - 1)
        self._loaded_data.extend(self._accounts_controller.get_entities(offset=len(self._loaded_data), limit=items_to_fetch))
        self.endInsertRows()

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            column_name = self._header_names[index.column()]
            return self._loaded_data[index.row()][self._column_indices[column_name]]
    
    def rowCount(self, parent):
        return len(self._loaded_data)

    def columnCount(self, parent):
        return len(self._header_names)

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._header_names[section]