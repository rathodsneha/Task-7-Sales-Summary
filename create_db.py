import sqlite3

# Connect to database (will create new if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert sample sales data
sales_data = [
    ("Pen", 10, 5.0),
    ("Notebook", 5, 20.0),
    ("Pencil", 15, 2.0),
    ("Eraser", 7, 3.0),
    ("Pen", 8, 5.0),
    ("Notebook", 3, 20.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

conn.commit()
conn.close()
print("✅ sales_data.db created with the sales table and sample data!")
