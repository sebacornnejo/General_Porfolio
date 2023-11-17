# A Simple Northwind Data Analysis Example

## Overview

This example showcases a data analysis project focused on the (extract) Northwind database. The example involves querying and analyzing data related to product revenue, employee performance, and overall sales. The results are visualized using Python with Pandas for data manipulation and Plotly for interactive and visually appealing charts.

## Code Structure

### 1. Top 10 Products by Revenue

- **Code File:** `simple_revenue_withplotly.py`
- **Objective:** Identify the top 10 most profitable products.
- **Data Source:** Northwind database
- **Technologies Used:** SQLite, Pandas, Plotly
- **Visual Output:** Bar chart displaying the revenue of the top 10 products.
- **Interactive Chart:** [Top Products Chart](https://sebacornnejo.github.io/top_products_chart.html)

### 2. Top 3 Employees by Total Orders

- **Code File:** `simple_revenue_withplotly.py`
- **Objective:** Identify the top 3 employees with the fewest total orders.
- **Data Source:** Northwind database
- **Technologies Used:** SQLite, Pandas, Plotly
- **Visual Output:** Bar chart displaying the total orders for the top 3 employees.
- **Interactive Chart:** [Top Employees Chart](https://sebacornnejo.github.io/top_employees_chart.html)

### 3. Top 10 Employees by Revenue

- **Code File:** `simple_revenue_withplotly.py`
- **Objective:** Identify the top 10 employees with the highest revenue.
- **Data Source:** Northwind database
- **Technologies Used:** SQLite, Pandas, Plotly
- **Visual Output:** Bar chart displaying the revenue of the top 10 employees.
- **Interactive Chart:** [Top Employees Revenue Chart](https://sebacornnejo.github.io/top_employeessales_chart.html)

### 4. Northwind Dashboard

- **Code File:** `simple_revenue_withplotly.py`
- **Objective:** Integrate the three charts into an interactive dashboard.
- **Technologies Used:** Plotly
- **Visual Output:** Combined dashboard showcasing the top products, top employees, and top employees by revenue.
- **Interactive Dashboard:** [Northwind Dashboard](https://sebacornnejo.github.io/northwind_dashboard.html)

## How to Use

1. Clone the repository: `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/PythonSQL_Northwind`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the individual analysis scripts or the full dashboard script.
4. Explore the generated charts and dashboard HTML files.

## Explanation

Each analysis script connects to the Northwind database, performs SQL queries to extract relevant information, and uses Pandas and Plotly for data manipulation and visualization. The generated charts are saved as interactive HTML files for easy sharing and embedding into dashboards.

Feel free to explore, modify, or extend the project to suit your needs. Happy coding!

**Note:** Uncomment the `fig.show()` lines in the individual analysis scripts if you want to display the charts interactively in your development environment.
