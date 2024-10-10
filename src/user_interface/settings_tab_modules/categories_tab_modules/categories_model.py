# src/user_interface/settings_tab_modules/categories_tab_modules/categories_model.py

from PyQt6.QtCore import Qt, QAbstractItemModel, QModelIndex
from typing import List, Dict, Any, Optional

class CategoryItem:
    def __init__(self, data: Dict[str, Any], columns: List[Dict[str, Any]], parent: Optional['CategoryItem'] = None):
        self.parent_item = parent
        self.item_data = data
        self.columns = columns
        self.child_items: List[CategoryItem] = []

    def appendChild(self, item: 'CategoryItem'):
        self.child_items.append(item)

    def child(self, row: int) -> Optional['CategoryItem']:
        return self.child_items[row] if 0 <= row < len(self.child_items) else None

    def childCount(self) -> int:
        return len(self.child_items)

    def columnCount(self) -> int:
        return len(self.columns)

    def data(self, column: int) -> Any:
        if 0 <= column < len(self.columns):
            return self.item_data.get(self.columns[column]['name'], '')
        return None

    def row(self) -> int:
        return self.parent_item.child_items.index(self) if self.parent_item else 0

    def parent(self) -> Optional['CategoryItem']:
        return self.parent_item

    def getId(self) -> int:
        return self.item_data.get('id', -1)

class CategoriesModel(QAbstractItemModel):
    def __init__(self, categories: List[Dict[str, Any]], columns: List[Dict[str, Any]], parent=None):
        super().__init__(parent)
        self.columns = columns
        self.root_item = CategoryItem({"name": "Root", "id": None}, self.columns)
        self.setupModelData(categories, self.root_item)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self.columns)

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.columns[section]['name'].capitalize()
        return None

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole) -> Any:
        if not index.isValid() or role != Qt.ItemDataRole.DisplayRole:
            return None

        item: CategoryItem = index.internalPointer()
        return item.data(index.column())

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable if index.isValid() else Qt.ItemFlag.NoItemFlags

    def index(self, row: int, column: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        parent_item = parent.internalPointer() if parent.isValid() else self.root_item
        if child_item := parent_item.child(row):
            return self.createIndex(row, column, child_item)
        return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()

        child_item: CategoryItem = index.internalPointer()
        parent_item = child_item.parent()

        if parent_item == self.root_item:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        parent_item = parent.internalPointer() if parent.isValid() else self.root_item
        return parent_item.childCount()

    def setupModelData(self, categories: List[Dict[str, Any]], parent: CategoryItem):
        for category in categories:
            category_item = CategoryItem(category, self.columns, parent)
            parent.appendChild(category_item)
            if 'subcategories' in category:
                self.setupModelData(category['subcategories'], category_item)

    def getCategoryId(self, index: QModelIndex) -> int:
        if not index.isValid():
            return -1

        item: CategoryItem = index.internalPointer()
        return item.getId()

    def updateData(self, categories: List[Dict[str, Any]]):
        self.beginResetModel()
        self.root_item = CategoryItem({"name": "Root", "id": None}, self.columns)
        self.setupModelData(categories, self.root_item)
        self.endResetModel()

    def index_from_string(self, index_str):
        path = [int(i) for i in index_str.split('.')]
        index = QModelIndex()
        for row in path:
            index = self.index(row, 0, index)
            if not index.isValid():
                return QModelIndex()
        return index

    def string_from_index(self, index):
        path = []
        while index.isValid():
            path.insert(0, str(index.row()))
            index = index.parent()
        return '.'.join(path)