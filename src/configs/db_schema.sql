-- Accounts table
CREATE TABLE Accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT NOT NULL,
    account_number TEXT NOT NULL,
    account_type TEXT NOT NULL
);

-- Categories table
CREATE TABLE Categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES Categories(id)
);

-- Transactions table
CREATE TABLE Transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER,
    date TEXT NOT NULL,
    payee TEXT,
    memo TEXT,
    category_id INTEGER,
    payment REAL,
    deposit REAL,
    account_balance REAL,
    FOREIGN KEY (account_id) REFERENCES Accounts(id),
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

-- Expenses table
CREATE TABLE Expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    expense_name TEXT NOT NULL,
    category_id INTEGER,
    due_date TEXT,
    frequency TEXT,
    amount REAL,
    FOREIGN KEY (category_id) REFERENCES Categories(id)
);

CREATE TABLE AccountTypes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_name TEXT NOT NULL UNIQUE
);

CREATE TABLE ExpenseFrequencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    frequency_name TEXT NOT NULL UNIQUE
);