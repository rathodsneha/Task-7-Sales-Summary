import sqlite3
import pandas as pd

# Step 1: Connect to existing database
conn = sqlite3.connect("sales_data.db")

# Step 2: Write SQL query
query = '''
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
'''

# Step 3: Run query and load into DataFrame
df = pd.read_sql_query(query, conn)

# Step 4: Print the result
print("Sales Summary:")
print(df)

# Close the database connection
conn.close()


import matplotlib.pyplot as plt

# Plot bar chart for revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")  # Saves the image
plt.show()  # Displays the chart
