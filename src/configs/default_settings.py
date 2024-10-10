# src/configs/default_settings.py
DEFAULT_ACCOUNT_TYPES = [
    "Checking",
    "Savings",
    "Credit Card",
    "Investment",
    "Line of Credit"
]

DEFAULT_CATEGORIES = [
    {"name": "Housing", "subcategories": [
        {"name": "Rent/Mortgage", "subcategories": ["Rent", "Mortgage Payments"]},
        {"name": "Utilities", "subcategories": ["Electricity", "Water", "Gas", "Trash Collection", "Internet & Cable"]},
        {"name": "Maintenance", "subcategories": ["Repairs", "Lawn Care", "HOA Fees", "Home Improvement"]},
        {"name": "Property Insurance/Taxes", "subcategories": ["Property Insurance", "Property Taxes"]}
    ]},
    {"name": "Transportation", "subcategories": [
        {"name": "Vehicle", "subcategories": ["Car Payments", "Fuel", "Maintenance & Repairs", "Insurance", "Registration/License"]},
        {"name": "Public Transportation", "subcategories": ["Bus Passes", "Train/Subway Tickets"]},
        {"name": "Ride-Sharing", "subcategories": ["Uber/Lyft", "Taxis"]},
        {"name": "Parking & Tolls", "subcategories": []}
    ]},
    {"name": "Food", "subcategories": [
        {"name": "Groceries", "subcategories": ["Supermarket", "Farmer's Market", "Wholesale Clubs"]},
        {"name": "Dining Out", "subcategories": ["Restaurants", "Takeout/Delivery", "Coffee Shops"]}
    ]},
    {"name": "Health and Medical", "subcategories": [
        {"name": "Health Insurance", "subcategories": ["Premiums"]},
        {"name": "Medical Expenses", "subcategories": ["Doctor Visits", "Medications", "Dental Care", "Eye Care", "Hospital Fees"]},
        {"name": "Fitness", "subcategories": ["Gym Membership", "Exercise Equipment", "Fitness Classes"]}
    ]},
    {"name": "Personal Care", "subcategories": [
        {"name": "Hygiene", "subcategories": ["Toiletries", "Haircuts"]},
        {"name": "Beauty", "subcategories": ["Salon Services", "Cosmetics", "Skincare"]}
    ]},
    {"name": "Childcare and Education", "subcategories": [
        {"name": "Childcare", "subcategories": ["Daycare", "Babysitting"]},
        {"name": "Education", "subcategories": ["School Supplies", "Tuition", "Textbooks", "Extracurricular Activities"]}
    ]},
    {"name": "Entertainment and Recreation", "subcategories": [
        {"name": "Subscriptions", "subcategories": ["Streaming Services", "Magazine/News Subscriptions"]},
        {"name": "Hobbies", "subcategories": ["Books", "Video Games", "Sports Equipment", "Music"]},
        {"name": "Vacations", "subcategories": ["Travel Expenses", "Hotel Accommodations", "Activities"]}
    ]},
    {"name": "Clothing", "subcategories": [
        {"name": "Adults", "subcategories": ["Work Clothing", "Casual Wear", "Accessories"]},
        {"name": "Children", "subcategories": ["School Uniforms", "Play Clothes", "Shoes"]}
    ]},
    {"name": "Insurance", "subcategories": [
        {"name": "Health Insurance", "subcategories": []},
        {"name": "Life Insurance", "subcategories": []},
        {"name": "Home Insurance", "subcategories": []},
        {"name": "Auto Insurance", "subcategories": []},
        {"name": "Disability Insurance", "subcategories": []}
    ]},
    {"name": "Debt Repayment", "subcategories": [
        {"name": "Credit Cards", "subcategories": ["Interest Payments", "Principal Payments"]},
        {"name": "Loans", "subcategories": ["Student Loans", "Personal Loans", "Auto Loans", "Mortgage"]}
    ]},
    {"name": "Savings and Investments", "subcategories": [
        {"name": "Emergency Fund", "subcategories": []},
        {"name": "Retirement Savings", "subcategories": ["401(k)", "IRA", "Pension"]},
        {"name": "Investment Accounts", "subcategories": ["Stocks", "Bonds", "Mutual Funds"]}
    ]},
    {"name": "Gifts and Donations", "subcategories": [
        {"name": "Gifts", "subcategories": ["Birthday Presents", "Holiday Gifts", "Wedding Gifts"]},
        {"name": "Charity", "subcategories": ["Donations", "Volunteering Expenses"]}
    ]},
    {"name": "Taxes", "subcategories": [
        {"name": "Income Tax", "subcategories": []},
        {"name": "Property Tax", "subcategories": []},
        {"name": "Sales Tax", "subcategories": []}
    ]},
    {"name": "Business Expenses", "subcategories": [
        {"name": "Office Supplies", "subcategories": []},
        {"name": "Professional Services", "subcategories": ["Accounting", "Legal"]},
        {"name": "Marketing", "subcategories": ["Advertising", "Promotions"]}
    ]},
    {"name": "Miscellaneous", "subcategories": [
        {"name": "Pet Expenses", "subcategories": ["Food", "Vet Bills", "Supplies"]},
        {"name": "Bank Fees", "subcategories": []},
        {"name": "Postage", "subcategories": []}
    ]}
]

DEFAULT_EXPENSE_FREQUENCIES = [
    "Daily",
    "Weekly",
    "Bi-weekly",
    "Monthly",
    "Bi-monthly",
    "Quarterly",
    "Annually"
    "One-time"
]
