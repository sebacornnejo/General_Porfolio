# -----------------------------------------------------------------------------------------#
# This script essentially connects to the Northwind database, performs SQL queries to retrieve specific information, and then visualizes the results using Pandas and Plotly.
# -----------------------------------------------------------------------------------------#

# Import necessary libraries
import sqlite3
import pandas as pd
import plotly.express as px  # Import Plotly for better styling

# -----------------------------------------------------------------------------------------#
# The colors #6331C5, #3F7AD8 and #12BF80 are used for the bar chart, and the dark template plotly_dark is chosen for a professional look.
# The font family is set to Montserrat for consistency.
# Each chart is saved as an interactive HTML file using Plotly for easy sharing and embedding into dashboards.
# -----------------------------------------------------------------------------------------#

# Add custom styles and links to the head of the HTML file
styles = '''
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
        }
    </style>
'''

# Connect to the Northwind database using SQLite
conn = sqlite3.connect("Northwind.db")

# Query to get the top 10 most profitable products
query = """
    SELECT ProductName, SUM(Price * Quantity) AS Revenue 
    FROM OrderDetails od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10;
"""

# Execute the query and store the results in a Pandas DataFrame
top_products = pd.read_sql_query(query, conn)

# Plot the results using Plotly
fig1 = px.bar(top_products, x='ProductName', y='Revenue',
              title='Top 10 Products by Revenue',
              labels={'ProductName': 'Product','Revenue': 'Revenue'},
              color_discrete_sequence=['#6331C5'],
              template='plotly_dark')

# Customize the layout
fig1.update_layout(xaxis_title='Product Name', yaxis_title='Revenue',
                   font_family="Montserrat")

# Save the interactive HTML chart
fig1.write_html("top_products_chart.html")

# Add Montserrat font style to the generated HTML
# Read the content of the generated HTML file with UTF-8 encoding
with open("top_products_chart.html", "r", encoding="utf-8") as file:
    content = file.read()
    
# Insert the styles in the head of the HTML file
content = content.replace('</head>', styles + '</head>')

# Escribir el contenido modificado de nuevo al archivo HTML
with open("top_products_chart.html", "w", encoding="utf-8") as file:
    file.write(content)

# Display the chart
# fig1.show()

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code establishes a connection to the SQLite database file "Northwind.db" using the sqlite3 library.
# It then runs a SQL query to retrieve the top 10 most profitable products from the Northwind database. The results are stored in a Pandas DataFrame named top_products.
# The script then creates a bar chart using Plotly for more interactive and visually appealing charts to visualize the revenue of the top 10 products. The chart is displayed with appropriate titles and labels.
# -----------------------------------------------------------------------------------------#

# Query to get the top 3 employees with the fewest total orders
query2 = """
    SELECT FirstName || " " || LastName, COUNT(*) as Total
    FROM Orders o
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Total ASC
    LIMIT 3;
"""

# Execute the query and store the results in a Pandas DataFrame
top_employees = pd.read_sql_query(query2, conn)

# Plot the results using Plotly
fig2 = px.bar(top_employees, x='FirstName || " " || LastName', y='Total',
              title='Top 3 Employees by Total Orders',
              labels={'FirstName || " " || LastName':'Name','Total': 'Total Orders'},
              color_discrete_sequence=['#3F7AD8'],
              template='plotly_dark')

# Customize the layout
fig2.update_layout(xaxis_title='Employee Name', yaxis_title='Total Orders',
                   font_family="Montserrat")

# Save the interactive HTML chart
fig2.write_html("top_employees_chart.html")

# Add Montserrat font style to the generated HTML
# Read the content of the generated HTML file with UTF-8 encoding
with open("top_employees_chart.html", "r", encoding="utf-8") as file:
    content = file.read()
    
# Insert the styles in the head of the HTML file
content = content.replace('</head>', styles + '</head>')

# Escribir el contenido modificado de nuevo al archivo HTML
with open("top_employees_chart.html", "w", encoding="utf-8") as file:
    file.write(content)

# Display the chart
# fig2.show()

# -----------------------------------------------------------------------------------------#
# Explanation:

# This section of the code retrieves the top 3 employees with the fewest total orders.
# The results are stored in a Pandas DataFrame named top_employees.
# A bar chart is created to visualize the total orders for the top 3 employees.
# -----------------------------------------------------------------------------------------#

# Query to get the top 10 employees with the highest revenue
query3 = """
    SELECT FirstName || " " || LastName, SUM(od.Quantity * p.Price) as Revenue
    FROM Orders o
    JOIN OrderDetails od ON od.OrderID = o.OrderID
    JOIN Products p ON p.ProductID = od.ProductID
    JOIN Employees e ON e.EmployeeID = o.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY Revenue DESC
    LIMIT 10;
    """

# Execute the query and store the results in a Pandas DataFrame
top_employeessales = pd.read_sql_query(query3, conn)

# Plot the results using Plotly
fig3 = px.bar(top_employeessales, x='FirstName || " " || LastName', y='Revenue',
              title='Top 10 Employees by Revenue',
              labels={'FirstName || " " || LastName':'Name','Revenue': 'Revenue'},
              color_discrete_sequence=['#12BF80'],
              template='plotly_dark')

# Customize the layout
fig3.update_layout(xaxis_title='Employee Name', yaxis_title='Revenue',
                   font_family="Montserrat")

# Save the interactive HTML chart
fig3.write_html("top_employeessales_chart.html")

# Add Montserrat font style to the generated HTML
# Read the content of the generated HTML file with UTF-8 encoding
with open("top_employeessales_chart.html", "r", encoding="utf-8") as file:
    content = file.read()
    
# Insert the styles in the head of the HTML file
content = content.replace('</head>', styles + '</head>')

# Escribir el contenido modificado de nuevo al archivo HTML
with open("top_employeessales_chart.html", "w", encoding="utf-8") as file:
    file.write(content)

# Display the chart
# fig3.show()

# -----------------------------------------------------------------------------------------#
# Explanation:

# This part of the code retrieves the top 10 employees with the highest revenue.
# The results are stored in a Pandas DataFrame named top_employeessales.
# A bar chart is created to visualize the revenue of the top 10 employees. The chart is displayed with appropriate titles and labels.
# -----------------------------------------------------------------------------------------#



# -----------------------------------------------------------------------------------------#
# Below is a basic example of how you can integrate the three charts into a dashboard:
# -----------------------------------------------------------------------------------------#

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import screeninfo

# Add the 'name' attribute to DataFrames
top_products['name'] = 'Products'
top_employees['name'] = 'Employees'
top_employeessales['name'] = 'Employee Sales'

# Create subplots
fig = make_subplots(rows=1, cols=3, subplot_titles=['Top 10 Products by Revenue',
                                                    'Top 3 Employees by Total Orders',
                                                    'Top 10 Employees by Revenue'])

# Add traces to the subplots
fig.add_trace(go.Bar(x=top_products['ProductName'], y=top_products['Revenue'], 
                     marker_color='#6331C5',
                     hovertemplate='<b>Product</b><br>Name: %{x}<br>Revenue: %{y}', name='Top Products'), row=1, col=1)
fig.add_trace(go.Bar(x=top_employees['FirstName || " " || LastName'], y=top_employees['Total'], 
                     marker_color='#3F7AD8',
                     hovertemplate='<b>Employee</b><br>Name: %{x}<br>Total Orders: %{y}',name='Top Employees'), row=1, col=2)
fig.add_trace(go.Bar(x=top_employeessales['FirstName || " " || LastName'], y=top_employeessales['Revenue'], 
                     marker_color='#12BF80',
                     hovertemplate='<b>Employee</b><br>Name: %{x}<br>Revenue: %{y}',name='Top Employees Revenue'), row=1, col=3)

# Get screen resolution
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Update layout
# Configure layout with automatic size
fig.update_layout(height=screen_height * 0.6, width=screen_width * 0.8,
                  showlegend=False,
                  title_text='<b style="font-size:24px">Northwind Dashboard</b>',
                  font_family="Montserrat",
                  template='plotly_dark')

# Update x-axis and y-axis labels
fig.update_xaxes(title_text='Product Name', row=1, col=1)
fig.update_xaxes(title_text='Employee Name', row=1, col=2)
fig.update_xaxes(title_text='Employee Name', row=1, col=3)

fig.update_yaxes(title_text='Revenue', row=1, col=1)
fig.update_yaxes(title_text='Total Orders', row=1, col=2)
fig.update_yaxes(title_text='Revenue', row=1, col=3)

# Save the interactive HTML dashboard
fig.write_html("northwind_dashboard.html")

# Add Montserrat font style to the generated HTML
# Read the content of the generated HTML file with UTF-8 encoding
with open("northwind_dashboard.html", "r", encoding="utf-8") as file:
    content = file.read()
    
# Insert the styles in the head of the HTML file
content = content.replace('</head>', styles + '</head>')

# Escribir el contenido modificado de nuevo al archivo HTML
with open("northwind_dashboard.html", "w", encoding="utf-8") as file:
    file.write(content)

# Display the dashboard
fig.show()

# -----------------------------------------------------------------------------------------#
# Explanation:

# The make_subplots function is used to create a 1x3 grid for the subplots.
# Each subplot is a bar chart created using Plotly's go.Bar.
# The layout is updated to include a title, set the font family, and use the dark template.
# X-axis and Y-axis labels are customized for each subplot.
# The interactive dashboard is saved as an HTML file named "northwind_dashboard.html".
# -----------------------------------------------------------------------------------------#