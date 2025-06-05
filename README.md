# Task 7: Basic Sales Summary using SQLite & Python

## 🎯 Objective:
Extract and visualize sales summary data using SQL inside Python.

## 🛠️ Tools Used:
- Python 3.13
- SQLite3
- Pandas
- Matplotlib

## 📂 Summary of Steps:
1. Created a SQLite database (`sales_data.db`) with a `sales` table.
2. Inserted sample sales data.
3. Ran SQL query inside Python using `sqlite3` and `pandas` to calculate:
   - Total quantity sold per product
   - Total revenue per product
4. Printed results in terminal
5. Plotted bar chart using `matplotlib`

## 📊 Output (Example):

| Product  | Total Qty | Revenue |
|----------|-----------|---------|
| Pen      | 18        | 90.0    |
| Notebook | 8         | 160.0   |
| Pencil   | 15        | 30.0    |
| Eraser   | 7         | 21.0    |

## 📈 Visualization:
The chart is saved as: `sales_chart.png`

## 📁 Files Included:
- `sales_data.db`: SQLite database
- `task7_summary.py`: Python script
- `sales_chart.png`: Bar chart image
- `README.md`: This file

