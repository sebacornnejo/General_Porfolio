# Import necessary libraries
import plotly.express as px
import plotly.graph_objects as go
import statsmodels

# Load the Iris dataset
df = px.data.iris()

# -----------------------------------------------------------------------------------------#
# Simple Scatterplot
fig1 = px.scatter(df, x="sepal_width", y="sepal_length", 
                  title='<b>Sepal Width vs Sepal Length<b>',
                  labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length'},
                  template='plotly_dark', color_discrete_sequence=['#6331C5'])

# Customize the layout
fig1.update_layout(font_family="Montserrat")

fig1.show()

# Save the interactive HTML chart
# fig1.write_html("scatterplot_sepal.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Color and Size
fig2 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="petal_length",
                  title='<b>Sepal Width vs Sepal Length with Species and Petal Length<b>',
                  labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length', 'petal_length': 'Petal Length'},
                  template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig2.update_layout(font_family="Montserrat")

fig2.show()

# Save the interactive HTML chart
# fig2.write_html("scatterplot_species.html")

# -----------------------------------------------------------------------------------------#
# 3D Scatterplot
fig3 = px.scatter_3d(df, x="sepal_length", y="petal_length", z="petal_width", color="species", size="sepal_width",
                     title='<b>3D Scatterplot of Sepal and Petal Dimensions<b>',
                     labels={'sepal_length': 'Sepal Length', 'petal_length': 'Petal Length', 'petal_width': 'Petal Width'},
                     template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig3.update_layout(font_family="Montserrat")

fig3.show()

# Save the interactive HTML chart
# fig3.write_html("scatterplot_3d.html")

# -----------------------------------------------------------------------------------------#
# Scatter Matrix
fig4 = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species",
                        title='<b>Scatter Matrix of Sepal and Petal Dimensions<b>',
                        template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig4.update_layout(font_family="Montserrat")

fig4.show()

# Save the interactive HTML chart
# fig4.write_html("scatter_matrix.html")

# -----------------------------------------------------------------------------------------#
# Boxplot
fig5 = px.box(df, y="sepal_width", 
              title='<b>Boxplot of Sepal Width<b>',
              labels={'sepal_width': 'Sepal Width'},
              template='plotly_dark', color_discrete_sequence=['#6331C5'])

# Customize the layout
fig5.update_layout(font_family="Montserrat")

fig5.show()

# Save the interactive HTML chart
# fig5.write_html("boxplot_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Boxplot Comparison
fig6 = px.box(df, x="species", y="sepal_width", color="species",
              title='<b>Boxplot Comparison of Sepal Width by Species<b>',
              labels={'sepal_width': 'Sepal Width'},
              template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig6.update_layout(font_family="Montserrat")

fig6.show()

# Save the interactive HTML chart
# fig6.write_html("boxplot_species_comparison.html")

# -----------------------------------------------------------------------------------------#
# Histogram
fig7 = px.histogram(df, x="sepal_width", 
                    title='<b>Histogram of Sepal Width<b>',
                    labels={'sepal_width': 'Sepal Width'},
                    template='plotly_dark', color_discrete_sequence=['#6331C5'])

# Customize the layout
fig7.update_layout(font_family="Montserrat")

fig7.show()

# Save the interactive HTML chart
# fig7.write_html("histogram_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Multiple Histograms
fig8 = px.histogram(df, x="sepal_width", color="species", 
                    title='<b>Overlayed Histograms of Sepal Width by Species<b>',
                    labels={'sepal_width': 'Sepal Width'},
                    template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig8.update_layout(font_family="Montserrat", barmode='overlay')
fig8.update_traces(opacity=0.75)

fig8.show()

# Save the interactive HTML chart
# fig8.write_html("histogram_species_overlay.html")

# -----------------------------------------------------------------------------------------#
# Histogram for General Counting
fig9 = px.histogram(df, x="species", color="sepal_width", histfunc="count", height=300, 
                    title='<b>Histogram Chart for General Counting<b>',
                    labels={'species': 'Species'},
                    template='plotly_dark')

# Customize the layout
fig9.update_layout(font_family="Montserrat")

fig9.show()

# Save the interactive HTML chart
# fig9.write_html("histogram_general_count.html")

# -----------------------------------------------------------------------------------------#
# Bar Chart
fig10 = px.bar(df, x="species", 
               title='<b>Bar Chart of Species<b>',
               labels={'species': 'Species'},
               template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig10.update_layout(font_family="Montserrat")

fig10.show()

# Save the interactive HTML chart
# fig10.write_html("bar_chart_species.html")

# -----------------------------------------------------------------------------------------#
# Bar Chart with Values
fig11 = px.bar(df, x="species", y="sepal_length", 
               title='<b>Bar Chart of Sepal Length by Species<b>',
               labels={'species': 'Species', 'sepal_length': 'Sepal Length'},
               template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig11.update_layout(font_family="Montserrat")

fig11.show()

# Save the interactive HTML chart
# fig11.write_html("bar_chart_sepal_length.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Regression Lines
fig12 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", trendline="ols", 
                   title='<b>Scatterplot with Regression Lines<b>',
                   labels={'sepal_width': 'Sepal Width', 'sepal_length': 'Sepal Length'},
                   template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig12.update_layout(font_family="Montserrat")

fig12.show()

# Save the interactive HTML chart
# fig12.write_html("scatterplot_regression.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Marginal Plots
fig13 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="box", marginal_x="box", 
                   trendline="ols", title='<b>Scatterplot with Marginal Plots<b>',
                   template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# Customize the layout
fig13.update_layout(font_family="Montserrat")

fig13.show()

# Save the interactive HTML chart
# fig13.write_html("scatterplot_marginal_plots.html")

# -----------------------------------------------------------------------------------------#
# Create a Dashboard with make_subplots
from plotly.subplots import make_subplots
import screeninfo


fig14 = make_subplots(rows=4, cols=4, subplot_titles=['Sepal Width vs Sepal Length', 'Sepal Width vs Sepal Length with Species and Petal Length',
                                                      '3D Scatterplot of Sepal and Petal Dimensions', 'Scatter Matrix of Sepal and Petal Dimensions',
                                                      'Boxplot of Sepal Width', 'Boxplot Comparison of Sepal Width by Species', 'Histogram of Sepal Width',
                                                      'Overlayed Histograms of Sepal Width by Species', 'Histogram Chart for General Counting',
                                                      'Bar Chart of Species', 'Bar Chart of Sepal Length by Species', 'Scatterplot with Regression Lines',
                                                      'Scatterplot with Marginal Plots'])

# Add traces to the subplots
fig14.add_trace(fig1['data'][0], row=1, col=1)
fig14.add_trace(fig2['data'][0], row=1, col=2)
fig14.add_trace(fig4['data'][0], row=1, col=3)
fig14.add_trace(fig5['data'][0], row=2, col=4)
fig14.add_trace(fig6['data'][0], row=2, col=1)
fig14.add_trace(fig7['data'][0], row=2, col=2)
fig14.add_trace(fig8['data'][0], row=2, col=3)
fig14.add_trace(fig9['data'][0], row=3, col=4)
fig14.add_trace(fig10['data'][0], row=3, col=1)
fig14.add_trace(fig11['data'][0], row=3, col=2)
fig14.add_trace(fig12['data'][0], row=3, col=3)
fig14.add_trace(fig13['data'][0], row=4, col=4)

# Get screen resolution
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Update layout
fig14.update_layout(height=screen_height, width=screen_width, showlegend=False, title_text='<b style="font-size:24px">Iris Dataset Dashboard</b>',
                    font_family="Montserrat", template='plotly_dark')

# Save the interactive HTML dashboard
fig14.write_html("iris_dataset_dashboard.html")

# Display the dashboard
fig14.show()
