# src/user_interface/common/table_widget.py
from PyQt6.QtWidgets import QTableView, QPushButton, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel

class TableWidget(QTableView):
    def __init__(self):
        super().__init__()
        self.setEditTriggers(QTableView.EditTrigger.NoEditTriggers)

class ButtonLayout(QHBoxLayout):
    def __init__(self, add_label, edit_label, delete_label):
        super().__init__()
        self.add_button = QPushButton(add_label)
        self.edit_button = QPushButton(edit_label)
        self.delete_button = QPushButton(delete_label)
        self.addWidget(self.add_button)
        self.addWidget(self.edit_button)
        self.addWidget(self.delete_button)

class TableModel(QStandardItemModel):
    def __init__(self):
        super().__init__()
    
    def hide_column(self, index):
        view = self.parent()
        if isinstance(view, QTableView):
            view.hideColumn(index)