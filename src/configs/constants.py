# src/configs/constants.py

# Database tables
TABLE_ACCOUNTS = "Accounts"

# Account fields
FIELD_ACCOUNT_ID = "id"
FIELD_ACCOUNT_NAME = "account_name"
FIELD_ACCOUNT_NUMBER = "account_number"
FIELD_ACCOUNT_TYPE = "account_type"

# SQL query templates
SQL_INSERT_ACCOUNT = """
INSERT INTO {table} ({name}, {number}, {type})
VALUES (?, ?, ?)
"""

SQL_SELECT_ACCOUNT_BY_ID = "SELECT * FROM {table} WHERE {id} = ?"

SQL_SELECT_ALL_ACCOUNTS = "SELECT * FROM {table}"

SQL_UPDATE_ACCOUNT = """
UPDATE {table}
SET {name} = ?, {number} = ?, {type} = ?
WHERE {id} = ?
"""

SQL_DELETE_ACCOUNT = "DELETE FROM {table} WHERE {id} = ?"


# Category table and fields
TABLE_CATEGORIES = "Categories"
FIELD_CATEGORY_ID = "id"
FIELD_CATEGORY_NAME = "category_name"
FIELD_PARENT_ID = "parent_id"

# SQL query templates for Categories
SQL_INSERT_CATEGORY = """
INSERT INTO {table} ({name}, {parent})
VALUES (?, ?)
"""

SQL_SELECT_CATEGORY_BY_ID = "SELECT * FROM {table} WHERE {id} = ?"

SQL_SELECT_ALL_CATEGORIES = "SELECT * FROM {table}"

SQL_UPDATE_CATEGORY = """
UPDATE {table}
SET {name} = ?, {parent} = ?
WHERE {id} = ?
"""

SQL_DELETE_CATEGORY = "DELETE FROM {table} WHERE {id} = ?"

SQL_SELECT_SUBCATEGORIES = "SELECT * FROM {table} WHERE {parent} = ?"

# Transactions table and fields
TABLE_TRANSACTIONS = "Transactions"
FIELD_TRANSACTION_ID = "id"
FIELD_ACCOUNT_ID = "account_id"
FIELD_DATE = "date"
FIELD_PAYEE = "payee"
FIELD_MEMO = "memo"
FIELD_CATEGORY_ID = "category_id"
FIELD_PAYMENT = "payment"
FIELD_DEPOSIT = "deposit"
FIELD_ACCOUNT_BALANCE = "account_balance"
FIELD_NOTE = "note"

# SQL query templates for Transactions
SQL_INSERT_TRANSACTION = """
INSERT INTO {table} ({account_id}, {date}, {payee}, {memo}, {category_id}, {payment}, {deposit}, {account_balance}, {note})
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_SELECT_TRANSACTION_BY_ID = "SELECT * FROM {table} WHERE {id} = ?"

SQL_SELECT_ALL_TRANSACTIONS = "SELECT * FROM {table}"

SQL_UPDATE_TRANSACTION = """
UPDATE {table}
SET {account_id} = ?, {date} = ?, {payee} = ?, {memo} = ?, {category_id} = ?, 
    {payment} = ?, {deposit} = ?, {account_balance} = ?, {note} = ?
WHERE {id} = ?
"""

SQL_DELETE_TRANSACTION = "DELETE FROM {table} WHERE {id} = ?"

# Add these to your existing constants.py file

# Expenses table and fields
TABLE_EXPENSES = "Expenses"
FIELD_EXPENSE_ID = "id"
FIELD_EXPENSE_NAME = "expense_name"
FIELD_CATEGORY_ID = "category_id"
FIELD_DUE_DATE = "due_date"
FIELD_FREQUENCY = "frequency"
FIELD_AMOUNT = "amount"

# SQL query templates for Expenses
SQL_INSERT_EXPENSE = """
INSERT INTO {table} ({name}, {category}, {due_date}, {frequency}, {amount})
VALUES (?, ?, ?, ?, ?)
"""

SQL_SELECT_EXPENSE_BY_ID = "SELECT * FROM {table} WHERE {id} = ?"

SQL_SELECT_ALL_EXPENSES = "SELECT * FROM {table}"

SQL_UPDATE_EXPENSE = """
UPDATE {table}
SET {name} = ?, {category} = ?, {due_date} = ?, {frequency} = ?, {amount} = ?
WHERE {id} = ?
"""

SQL_DELETE_EXPENSE = "DELETE FROM {table} WHERE {id} = ?"