# Import necessary libraries
import plotly.express as px
import plotly.graph_objects as go
import statsmodels

# Load the Iris dataset
df = px.data.iris()

# Map species names to the desired format
species_mapping = {
    "setosa": "Setosa",
    "versicolor": "Versicolor",
    "virginica": "Virginica",
}
df["species"] = df["species"].map(species_mapping)

# -----------------------------------------------------------------------------------------#
# Simple Scatterplot
# fig1 = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     title='<b style="font-size:24px>A Simple Scatterplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={"sepal_width": "Sepal Width", "sepal_length": "Sepal Length"},
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5"],
# )

# # Customize the layout
# fig1.update_layout(
#     xaxis_title="Sepal Width", yaxis_title="Sepal Length", font_family="Montserrat"
# )

# # Adjust point size fixedly
# fig1.update_traces(marker=dict(size=12, line=dict(color="#F2F2F2", width=2)))

# fig1.show()

# Save the interactive HTML chart
# fig1.write_html(".\HTMLs\scatterplot_sepal.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Color and Size
# fig2 = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     size="petal_length",
#     title='<b style="font-size:24px>A Simple Scatterplot with Color and Size</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={
#         "sepal_width": "Sepal Width",
#         "sepal_length": "Sepal Length",
#         "petal_length": "Petal Length",
#         "species": "Species",
#     },
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# fig2.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# # Customize the layout
# fig2.update_layout(
#     # xaxis_title="Sepal Width",
#     # yaxis_title="Sepal Length",
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig2.show()

# Save the interactive HTML chart
# fig2.write_html(".\HTMLs\scatterplot_species.html")

# -----------------------------------------------------------------------------------------#
# 3D Scatterplot
# fig3 = px.scatter_3d(
#     df,
#     x="sepal_length",
#     y="petal_length",
#     z="petal_width",
#     color="species",
#     size="sepal_width",
#     title='<b style="font-size:24px>A Simple 3D Scatterplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={
#         "sepal_length": "Sepal Length",
#         "petal_length": "Petal Length",
#         "petal_width": "Petal Width",
#         "species": "Species",
#         "sepal_width": "Sepal Width",
#     },
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# fig3.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# # Customize the layout
# fig3.update_layout(
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig3.show()

# Save the interactive HTML chart
# fig3.write_html(".\HTMLs\scatterplot_3d.html")

# -----------------------------------------------------------------------------------------#
# Scatter Matrix
# fig4 = px.scatter_matrix(
#     df,
#     dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
#     color="species",
#     title='<b style="font-size:24px>A Simple Scatter Matrix</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={
#         "sepal_length": "Sepal Length",
#         "petal_length": "Petal Length",
#         "petal_width": "Petal Width",
#         "species": "Species",
#         "sepal_width": "Sepal Width",
#     },
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# # Customize the layout
# fig4.update_layout(
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=1.07, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig4.show()

# # Save the interactive HTML chart
# fig4.write_html(".\HTMLs\scatter_matrix.html")

# -----------------------------------------------------------------------------------------#
# Boxplot
# fig5 = px.box(
#     df,
#     y="sepal_width",
#     title='<b style="font-size:24px>A Simple Boxplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={"sepal_width": "Sepal Width"},
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5"],
# )

# # Customize the layout
# fig5.update_layout(font_family="Montserrat")

# fig5.show()

# Save the interactive HTML chart
# fig5.write_html(".\HTMLs\boxplot_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Boxplot Comparison
# fig6 = px.box(
#     df,
#     x="species",
#     y="sepal_width",
#     color="species",
#     title='<b style="font-size:24px>A Simple Boxplot Comparison</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={"sepal_width": "Sepal Width", "species": "Species"},
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# # Customize the layout
# fig6.update_layout(
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.96, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig6.show()

# Save the interactive HTML chart
# fig6.write_html(".\HTMLs\boxplot_species_comparison.html")

# -----------------------------------------------------------------------------------------#
# Histogram
# import numpy as np

# # Calculate percentage bins from histogram using numpy
# # This is because Plotly does not have the ability to display "count" and "percent" at the same time in "hover"
# bin = 13;
# hist, _ = np.histogram(df["sepal_width"], bins=bin, density=False)
# hist_percent = (hist / len(df)) * 100

# fig7 = px.histogram(
#     df,
#     x="sepal_width",
#     nbins=bin,
#     title='<b style="font-size:24px>A Simple Histogram</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={"sepal_width": "Sepal Width"},
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5"],
# )

# fig7.update_traces(
#     marker=dict(line=dict(color="#F2F2F2", width=0.5)),
#     hovertemplate="Bin: %{x}<br>Count: %{y}<br>Percent: %{customdata:.2f}%",
#     customdata=hist_percent,
# )

# # Customize the layout
# fig7.update_layout(font_family="Montserrat")

# fig7.show()

# Save the interactive HTML chart
# fig7.write_html(".\HTMLs\histogram_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Multiple Histograms
# fig8 = px.histogram(
#     df,
#     x="sepal_width",
#     color="species",
#     nbins=10,
#     title='<b style="font-size:24px>A Simple Multiple Histogram</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={"sepal_width": "Sepal Width", "species": "Species"},
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# fig8.update_traces(marker=dict(line=dict(color="#F2F2F2", width=0.5)),hovertemplate='Bin: %{x}<br>Count: %{y}')

# # Customize the layout
# fig8.update_layout(
#     font_family="Montserrat",
#     barmode="group",
#     yaxis_title=" ",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.98, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig8.show()

# Save the interactive HTML chart
# fig8.write_html(".\HTMLs\histogram_species_overlay.html")

# -----------------------------------------------------------------------------------------#
# Histogram for General Counting
# color_palette_cpt = [
#     "#EAF759","#F1E44F","#F7D246","#FABF3F","#FCAE3C","#FB9C3E","#F78C45","#F07F50","#E5745E","#D76C6B","#C76676","#B7617F","#A65C86","#96578A","#87518E","#784B91","#694496","#593D9B","#4736A0","#303399","#1A347F","#0C3062","#062B49","#042333"
# ]

# df_sorted = df.sort_values(by='sepal_width', ascending=False)

# fig9 = px.histogram(df_sorted, x="species", color="sepal_width", histnorm="percent", height=400,
#                     title='<b style="font-size:24px>A Simple Histogram Chart for General Percentage</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#                     labels={'species': 'Species',"sepal_width": "Sepal Width"},
#                     template='plotly_dark',color_discrete_sequence=color_palette_cpt,
#                    )

# # Customize the layout
# fig9.update_layout(height=600, width=1080,font_family="Montserrat",showlegend=True,
#     yaxis_title=" ",
#     legend_title="<b>Sepal Width:<b>",
#     legend=dict(bgcolor="rgba(255, 255, 255, 0.5)", traceorder='reversed'),
#     legend_font_color="#262626",)

# fig9.update_traces(hovertemplate='<b>Percent</b>: %{y:.2f}%')

# fig9.show()

# Save the interactive HTML chart
# fig9.write_html(".\HTMLs\histogram_general_count.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Regression Lines
# fig10 = px.scatter(
#     df,
#     x="sepal_width",
#     y="sepal_length",
#     color="species",
#     trendline="ols",
#     title='<b style="font-size:24px>A Simple Scatterplot with Regression Lines</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#     labels={
#         "sepal_width": "Sepal Width",
#         "sepal_length": "Sepal Length",
#         "species": "Species",
#     },
#     template="plotly_dark",
#     color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
# )

# fig10.update_traces(marker=dict(size=10, line=dict(color="#F2F2F2", width=0.5)))
# # Customize the layout
# fig10.update_layout(
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig10.show()

# # Save the interactive HTML chart
# fig10.write_html(".\HTMLs\scatterplot_regression.html")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Marginal Plots
# fig13 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="box", marginal_x="box", 
#                    trendline="ols", title='<b style="font-size:24px>A Simple Scatterplot with Margin Plots</b><br><span style="font-size:14px;">from Iris Dataset</span>',
#                    labels={"sepal_width": "Sepal Width", "sepal_length": "Sepal Length", "species": "Species"},
#                    template='plotly_dark', color_discrete_sequence=['#6331C5', '#3F7AD8', '#12BF80'])

# # Customize the layout
# fig13.update_traces(marker=dict(size=10, line=dict(color="#F2F2F2", width=0.5)))
# # Customize the layout
# fig13.update_layout(
#     font_family="Montserrat",
#     showlegend=True,
#     legend_title="<b>Species:<b>",
#     legend=dict(x=0.74, y=0.98, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
#     legend_font_color="#262626",
# )

# fig13.show()

# Save the interactive HTML chart
# fig13.write_html(".\HTMLs\scatterplot_marginal_plots.html")

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
