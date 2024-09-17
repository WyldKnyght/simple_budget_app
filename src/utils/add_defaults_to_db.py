# src/utils/add_defaults_to_db.py
import os
import sqlite3
from dotenv import load_dotenv
from pathlib import Path
import sys

# Load environment variables from .env file
load_dotenv()

# Get the current file's directory
current_file_path = Path(__file__).resolve()

# Define a function to find the root directory
def find_root_directory(start_path, marker):
    path = start_path
    while path != path.parent:  # Loop until we reach the root
        if (path / marker).exists():  # Check if the marker exists
            return path
        path = path.parent  # Move up one level
    return None  # Return None if the marker is not found

# Find the root directory using a marker (e.g., '.env' file)
root_dir = find_root_directory(current_file_path, '.env')

if root_dir is None:
    raise FileNotFoundError("Root directory not found. Ensure the marker file exists.")

# Add the root directory to the Python path
sys.path.insert(0, str(root_dir))

# Import the settings configuration
from src.configs.settings_config import DEFAULT_ACCOUNT_TYPES, DEFAULT_CATEGORIES, DEFAULT_EXPENSE_FREQUENCIES  # noqa: E402

# Resolve the full database path from .env
db_path = root_dir / os.getenv("DATABASE_PATH")

# Debugging output to verify paths
print(f"Resolved database path: {db_path}")

# Ensure the directory for the database exists
db_path.parent.mkdir(parents=True, exist_ok=True)

# Function to add default account types
def add_default_account_types(cursor):
    cursor.executemany("INSERT OR IGNORE INTO AccountTypes (type_name) VALUES (?);", 
                       [(account_type,) for account_type in DEFAULT_ACCOUNT_TYPES])
    print("Default account types added.")

# Function to add default categories and subcategories
def add_default_categories(cursor):
    def insert_subcategories(parent_id, subcategories):
        subcategory_data = []
        for subcategory in subcategories:
            if isinstance(subcategory, dict):  # Ensure subcategory is a dictionary
                subcategory_data.append((subcategory["name"], parent_id))
                if isinstance(subcategory.get("subcategories"), list):  # Ensure subcategories is a list
                    subcategory_data.extend(insert_subcategories(cursor.lastrowid, subcategory["subcategories"]))
        return subcategory_data

    category_data = [(category["name"],) for category in DEFAULT_CATEGORIES]
    cursor.executemany("INSERT OR IGNORE INTO Categories (category_name) VALUES (?);", category_data)
    
    for category in DEFAULT_CATEGORIES:
        cursor.execute("SELECT id FROM Categories WHERE category_name = ?", (category["name"],))
        category_id = cursor.fetchone()[0]
        subcategory_data = insert_subcategories(category_id, category.get("subcategories", []))
        cursor.executemany("INSERT OR IGNORE INTO Categories (category_name, parent_id) VALUES (?, ?);", subcategory_data)
    
    print("Default categories and subcategories added.")

# Function to add default expense frequencies
def add_default_expense_frequencies(cursor):
    cursor.executemany("INSERT OR IGNORE INTO ExpenseFrequencies (frequency_name) VALUES (?);", 
                       [(frequency,) for frequency in DEFAULT_EXPENSE_FREQUENCIES])
    print("Default expense frequencies added.")

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Add default values
add_default_account_types(cursor)
add_default_categories(cursor)
add_default_expense_frequencies(cursor)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Default values added to the database.")
