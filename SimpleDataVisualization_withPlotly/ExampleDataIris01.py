# -----------------------------------------------------------------------------------------#
# This script essentially develops simple visualizations from the Iris dataset using Plotly Express.
# -----------------------------------------------------------------------------------------#

# Import necessary libraries
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------------------#
# The dark template plotly_dark is chosen for a professional look.
# Colors #6331C5, #3F7AD8 and #12BF80 are used main for the charts.
# The font family is set to Montserrat for consistency.
# Each chart is saved as an interactive HTML file using Plotly for easy sharing and embedding into dashboards.
# -----------------------------------------------------------------------------------------#

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
fig1 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    title='<b style="font-size:24px>A Simple Scatterplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width", "sepal_length": "Sepal Length"},
    template="plotly_dark",
    color_discrete_sequence=["#6331C5"],
)

# Customize the layout
fig1.update_layout(
    xaxis_title="Sepal Width", yaxis_title="Sepal Length", font_family="Montserrat"
)

# Adjust point size fixedly
fig1.update_traces(marker=dict(size=12, line=dict(color="#F2F2F2", width=2)))

# Uncomment the following line to display the interactive HTML chart:
# fig1.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig1.write_html("./HTMLs/scatterplot_sepal.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code generates a simple scatterplot from the Iris dataset, visualizing sepal width against sepal length.
# The chart is styled with the Plotly dark template and displayed interactively.
# -----------------------------------------------------------------------------------------#

# Scatterplot with Color and Size
fig2 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    size="petal_length",
    title='<b style="font-size:24px>A Simple Scatterplot with Color and Size</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_length": "Petal Length",
        "species": "Species",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

fig2.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# Customize the layout
fig2.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig2.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig2.write_html("./HTMLs/scatterplot_species.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# This section creates a scatterplot with color-coded points representing different species.
# The size of the points is determined by petal length.
# The chart is styled and displayed interactively.
# -----------------------------------------------------------------------------------------#

# 3D Scatterplot
fig3 = px.scatter_3d(
    df,
    x="sepal_length",
    y="petal_length",
    z="petal_width",
    color="species",
    size="sepal_width",
    title='<b style="font-size:24px>A Simple 3D Scatterplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_length": "Sepal Length",
        "petal_length": "Petal Length",
        "petal_width": "Petal Width",
        "species": "Species",
        "sepal_width": "Sepal Width",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

# Add borders to markers
fig3.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# Customize the layout
fig3.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig3.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig3.write_html("./HTMLs/scatterplot_3d.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code utilizes Plotly Express to create a 3D scatterplot from the Iris dataset.
# The scatterplot visualizes the relationships between sepal length, petal length, petal width, and sepal width, with points colored by species and sized by sepal width.
# The title of the plot is set with specified font sizes.
# Axes are labeled with descriptive names, and the color sequence is customized.
# Markers have borders added for better visibility.
# The layout is customized with the Montserrat font, legend settings, and a light background for the legend.
# The final 3D scatterplot is displayed.
# -----------------------------------------------------------------------------------------#

# Scatter Matrix
fig4 = px.scatter_matrix(
    df,
    dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
    color="species",
    title='<b style="font-size:24px>A Simple Scatter Matrix</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_length": "Sepal Length",
        "petal_length": "Petal Length",
        "petal_width": "Petal Width",
        "species": "Species",
        "sepal_width": "Sepal Width",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

# Customize the layout
fig4.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=1.07, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig4.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig4.write_html("./HTMLs/scatter_matrix.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The scatter matrix displays pairwise relationships between sepal width, sepal length, petal width, and petal length, with points colored by species.
# The title of the plot is set with specified font sizes.
# Axes are labeled with descriptive names, and the color sequence is customized.
# The layout is customized with the Montserrat font, legend settings, and a light background for the legend.
# The final Scatter Matrix is displayed.
# -----------------------------------------------------------------------------------------#

# Boxplot
fig5 = px.box(
    df,
    y="sepal_width",
    title='<b style="font-size:24px>A Simple Boxplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width"},
    template="plotly_dark",
    color_discrete_sequence=["#3F7AD8"],
)

# Update boxplot traces with customization
fig5.update_traces(
    marker=dict(
        outliercolor="#3F7AD8",
        size=9,
        line=dict(outliercolor="#3F7AD8"),
    ),
    boxmean="sd",
    line=dict(color="#F2F2F2"),
    fillcolor="#6331C5",
)

# Customize the layout
fig5.update_layout(
    font_family="Montserrat",
)

# Add a scatter plot to show individual data points
scatter_trace = go.Scatter(
    y=df["sepal_width"],
    mode="markers",
    marker=dict(color="#12BF80", size=8),
    hovertemplate="Width: %{y}",
    name="",
    showlegend=False,
)

fig5.add_trace(scatter_trace)

# Adjust x positions of scatter plot points and boxplot
fig5.update_traces(xaxis="x", x0=0, dx=0.2, selector=dict(type="box"))
fig5.update_traces(xaxis="x", x0=-0.35, dx=0.0004, selector=dict(type="scatter"))

# Hide x-axis tick labels
fig5.update_xaxes(showticklabels=False)

# Uncomment the following line to display the interactive HTML chart:
# fig5.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig5.write_html("./HTMLs/boxplot_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The title of the plot is set with specified font sizes.
# Boxplot customization includes marker settings, line colors, and fill colors.
# A scatter plot is added to show individual data points.
# The x positions of scatter plot points and boxplot are adjusted for better visual alignment.
# X-axis tick labels are hidden for cleaner presentation.
# The final Boxplot with Scatter Plot is displayed.
# -----------------------------------------------------------------------------------------#

# Boxplot Comparison
# Lista de colores de relleno para los boxplots
fill_colors = ["#6331C5", "#3F7AD8", "#12BF80"]

# Create a list of Box traces with custom colors
box_traces = []
for i in range(len(fill_colors)):
    box_trace = go.Box(
        x=df[df["species"] == df["species"].unique()[i]]["species"],
        y=df[df["species"] == df["species"].unique()[i]]["sepal_width"],
        name=df["species"].unique()[i],
        marker=dict(
            color=fill_colors[i],
            line=dict(color=fill_colors[i]),
        ),
        line=dict(color="#F2F2F2"),
        fillcolor=fill_colors[i],
        boxpoints="all",
    )
    box_traces.append(box_trace)

# Create the figure and add the custom boxplots
fig6 = go.Figure(box_traces)

# Additional configurations
fig6.update_layout(
    title='<b style="font-size:24px>A Simple Boxplot Comparison</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    xaxis=dict(title="Species"),
    yaxis=dict(title="Sepal Width"),
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.96, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
    template="plotly_dark",
)

# Uncomment the following line to display the interactive HTML chart:
# fig6.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig6.write_html("./HTMLs/boxplot_species_comparison.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code creates a Boxplot Comparison using Plotly with multiple boxplots for sepal width categorized by species from the Iris dataset.
# A list of fill colors is defined for each boxplot.
# Custom Box traces are created for each species with specified colors and other visual settings.
# The figure is generated by combining the custom boxplots.
# -----------------------------------------------------------------------------------------#

# Histogram
# The numpy library is additionally imported
import numpy as np

# Calculate percentage bins from histogram using numpy
# This is because Plotly does not have the ability to display "count" and "percent" at the same time in "hover"
bin = 13
hist, bin_edges = np.histogram(df["sepal_width"], bins=bin, density=False)
hist_percent = (hist / len(df)) * 100

# Create a Histogram using Plotly Express
fig7 = px.histogram(
    df,
    x="sepal_width",
    nbins=bin,
    title='<b style="font-size:24px>A Simple Histogram</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width"},
    template="plotly_dark",
    color_discrete_sequence=["#6331C5"],
)

# Update histogram traces with customization
fig7.update_traces(
    marker=dict(line=dict(color="#F2F2F2", width=0.5)),
    hovertemplate="Bin: %{x}<br>Count: %{y}<br>Percent: %{customdata:.2f}%",
    customdata=hist_percent,
)

# Customize the layout
fig7.update_layout(font_family="Montserrat")

# Add lines for mean, median, and standard deviation via go.Scatter
fig7.add_trace(
    go.Scatter(
        x=[
            min(df["sepal_width"]),
            max(df["sepal_width"]) + (bin_edges[1] - bin_edges[0]),
        ],
        y=[np.mean(hist), np.mean(hist)],
        mode="lines",
        line=dict(color="#12BF80", width=2, dash="longdashdot"),
        name="Mean",
        showlegend=False,
        hoverinfo="name",
    )
)

fig7.add_trace(
    go.Scatter(
        x=[
            min(df["sepal_width"]),
            max(df["sepal_width"]) + (bin_edges[1] - bin_edges[0]),
        ],
        y=[np.median(hist), np.median(hist)],
        mode="lines",
        line=dict(color="#B715B7", width=2, dash="longdashdot"),
        name="Median",
        showlegend=False,
        hoverinfo="name",
    )
)

fig7.add_trace(
    go.Scatter(
        x=[
            min(df["sepal_width"]),
            max(df["sepal_width"]) + (bin_edges[1] - bin_edges[0]),
        ],
        y=[np.mean(hist) - np.std(hist), np.mean(hist) - np.std(hist)],
        mode="lines",
        line=dict(color="#3F7AD8", width=1.5, dash="dash"),
        name="Std Dev",
        showlegend=False,
        hoverinfo="name",
    )
)

fig7.add_trace(
    go.Scatter(
        x=[
            min(df["sepal_width"]),
            max(df["sepal_width"]) + (bin_edges[1] - bin_edges[0]),
        ],
        y=[np.mean(hist) + np.std(hist), np.mean(hist) + np.std(hist)],
        mode="lines",
        line=dict(color="#3F7AD8", width=1.5, dash="dash"),
        name="Std Dev",
        showlegend=False,
        hoverinfo="name",
    )
)

# Remove y-axis title for better presentation
fig7.update_yaxes(title_text="")

# Uncomment the following line to display the interactive HTML chart:
# fig7.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig7.write_html("./HTMLs/histogram_sepal_width.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code calculates a histogram with percentage bins from the "sepal_width" column of the Iris dataset using NumPy.
# A Histogram is created using Plotly Express with specified parameters, including title, labels, and template.
# Histogram traces are customized for better visualization, and hover information includes bin, count, and percentage.
# Additional traces are added for mean, median, and standard deviation lines.
# The final Histogram with Mean, Median, and Standard Deviation lines is displayed.
# -----------------------------------------------------------------------------------------#

# Multiple Histograms
fig8 = px.histogram(
    df,
    x="sepal_width",
    color="species",
    nbins=10,
    title='<b style="font-size:24px>A Simple Multiple Histogram</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width", "species": "Species"},
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

# Update histogram traces with customization
fig8.update_traces(
    marker=dict(line=dict(color="#F2F2F2", width=0.5)),
    hovertemplate="Bin: %{x}<br>Count: %{y}",
)

# Customize the layout
fig8.update_layout(
    font_family="Montserrat",
    barmode="group",
    yaxis_title=" ",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.98, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig8.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig8.write_html("./HTMLs/histogram_species_overlay.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code creates a Multiple Histogram using Plotly Express with different colors for each species.
# The x-axis represents sepal width, and the data is grouped by the "species" column.
# Customizations include title, labels, template, color sequence, and hover information.
# The final Multiple Histograms are displayed, showing the distribution of sepal width for each species.
# -----------------------------------------------------------------------------------------#

# Histogram for General Counting
# The screeninfo library is additionally imported
import screeninfo

# Define a color palette for the histogram, these are extracted from thermal.cpt (http://soliton.vm.bytemark.co.uk/pub/cpt-city/cmocean/tn/thermal.png.index.html) and transformed to hex format with matlab,
# - colormap_cpt.m: http://soliton.vm.bytemark.co.uk/pub/cpt-city/notes/colormap_cpt.m
# - rgb2hex.m: https://www.mathworks.com/matlabcentral/fileexchange/46289-rgb2hex-and-hex2rgb
color_palette_cpt = [
    "#EAF759",
    "#F1E44F",
    "#F7D246",
    "#FABF3F",
    "#FCAE3C",
    "#FB9C3E",
    "#F78C45",
    "#F07F50",
    "#E5745E",
    "#D76C6B",
    "#C76676",
    "#B7617F",
    "#A65C86",
    "#96578A",
    "#87518E",
    "#784B91",
    "#694496",
    "#593D9B",
    "#4736A0",
    "#303399",
    "#1A347F",
    "#0C3062",
    "#062B49",
    "#042333",
]

# Sort the DataFrame by sepal width in descending order
df_sorted = df.sort_values(by="sepal_width", ascending=False)

# Create a Histogram for General Counting using Plotly Express
fig9 = px.histogram(
    df_sorted,
    x="species",
    color="sepal_width",
    histnorm="percent",
    height=400,
    title='<b style="font-size:24px>A Simple Histogram Chart for General Percentage</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"species": "Species", "sepal_width": "Sepal Width"},
    template="plotly_dark",
    color_discrete_sequence=color_palette_cpt,
)
# Get screen resolution
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Customize the layout
fig9.update_layout(
    height=screen_height * 0.7,
    width=screen_width * 0.8,
    font_family="Montserrat",
    showlegend=True,
    yaxis_title=" ",
    legend_title="<b>Sepal Width:<b>",
    legend=dict(bgcolor="rgba(255, 255, 255, 0.5)", traceorder="reversed"),
    legend_font_color="#262626",
)

# Update hover template
fig9.update_traces(hovertemplate="<b>Percent</b>: %{y:.2f}%")

# Uncomment the following line to display the interactive HTML chart:
# fig9.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig9.write_html("./HTMLs/histogram_general_count.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code creates a Histogram for General Counting using Plotly Express with sepal width colored by species.
# The DataFrame is sorted by sepal width in descending order.
# Customizations include title, labels, template, color palette, and histogram normalization to percent.
# The layout is customized with screen dimensions.
# The final Histogram for General Counting is displayed, showing the distribution of sepal width across species.
# -----------------------------------------------------------------------------------------#

# Scatterplot with Regression Lines
fig10 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    trendline="ols",  # Adding Ordinary Least Squares (OLS) regression lines
    title='<b style="font-size:24px>A Simple Scatterplot with Regression Lines</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "species": "Species",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

# Update scatterplot traces with customization
fig10.update_traces(marker=dict(size=10, line=dict(color="#F2F2F2", width=0.5)))

# Customize the layout
fig10.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig10.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig10.write_html("./HTMLs/scatterplot_regression.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code creates a Scatterplot with Regression Lines using Plotly Express with sepal width on the x-axis, sepal length on the y-axis, and color-coded by species.
# Regression lines are added using Ordinary Least Squares (OLS) method.
# The final Scatterplot with Regression Lines is displayed, showing the relationship between sepal width and sepal length with regression lines for each species.
# -----------------------------------------------------------------------------------------#

# Scatterplot with Marginal Plots
fig11 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    marginal_y="box",  # Add marginal boxplots on the y-axis
    marginal_x="box",  # Add marginal boxplots on the x-axis
    trendline="ols",  # Adding Ordinary Least Squares (OLS) regression lines
    title='<b style="font-size:24px>A Simple Scatterplot with Margin Plots</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "species": "Species",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

# Update scatterplot traces with customization
fig11.update_traces(marker=dict(size=10, line=dict(color="#F2F2F2", width=0.5)))

# Customize the layout
fig11.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.98, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Customize the color of the fill for the marginal boxplots
fill_colors = ["#6331C5", "#3F7AD8", "#12BF80"]
for i, species in enumerate(df["species"].unique()):
    fig11.update_traces(
        marker=dict(color=fill_colors[i], line=dict(color="#F2F2F2")),
        line=dict(color="#F2F2F2"),
        fillcolor=fill_colors[i],
        selector=dict(type="box", name=species),
    )

# Uncomment the following line to display the interactive HTML chart:
# fig11.show()

# Save the interactive HTML chart
# Uncomment the following line to save the interactive HTML chart:
# fig11.write_html("./HTMLs/scatterplot_marginal_plots.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code creates a Scatterplot with Marginal Boxplots using Plotly Express.
# The main scatterplot is created with sepal width on the x-axis, sepal length on the y-axis, and color-coded by species.
# Marginal boxplots are added on both the x-axis and y-axis to show the distribution of individual variables.
# Regression lines are added using Ordinary Least Squares (OLS) method.
# Contour lines of marginal boxplots are change and filled with custom colors corresponding to each species.
# The final Scatterplot with Marginal Plots is displayed, providing a comprehensive view of the data distribution.
# -----------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------#
# Below is a basic example of how you can integrate the charts into a dashboard:
# (Alternative graphics included for fig2 and fig6)
# -----------------------------------------------------------------------------------------#


# -----------------------------------------------------------------------------------------#
# Alternative to Scatterplot with Color and Size of Fig2
fig2a = px.scatter(
    df,
    x="petal_length",
    y="petal_width",
    color="species",
    size="sepal_width",
    title='<b style="font-size:24px>A Simple Scatterplot with Color and Size</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_width": "Sepal Width",
        "petal_width": "Petal Width",
        "petal_length": "Petal Length",
        "species": "Species",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

fig2a.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# Customize the layout
fig2a.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig2a.show()

# -----------------------------------------------------------------------------------------#
# Alternative to Boxplot Comparison of Fig6
fig6a = px.box(
    df,
    x="species",
    y="sepal_width",
    color="species",
    points="all",
    title='<b style="font-size:24px>A Simple Boxplot Comparison</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width", "species": "Species"},
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

fig6a.update_traces(
    marker=dict(color="#12BF80"),  # Color de relleno
    line=dict(color="#F2F2F2"),  # Color de línea de contorno
)

# Customize the layout
fig6a.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.96, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# Uncomment the following line to display the interactive HTML chart:
# fig6a.show()

# -----------------------------------------------------------------------------------------#
# Create a Dashboard with make_subplots
from plotly.subplots import make_subplots

# Define the layout of the subplots
fig12 = make_subplots(
    rows=5,
    cols=2,
    subplot_titles=[
        "A Simple Scatterplot",
        "A Simple Scatterplot with Color and Size",
        "Another Simple Scatterplot with Color and Size",
        "A Simple Boxplot",
        "A Simple Boxplot Comparison",
        "Another Simple Boxplot Comparison",
        "A Simple Histogram",
        "A Simple Multiple Histogram",
        "A Simple Histogram Chart for General Percentage<br>&#x25ba; Sepal Width",
        "A Simple Scatterplot with Regression Lines",
    ],
    horizontal_spacing=0.035,
    vertical_spacing=0.025,
)

# Add traces to the subplots by iterating over individual figures
for trace in fig1["data"]:
    fig12.add_trace(trace, row=1, col=1)
for trace in fig2["data"]:
    fig12.add_trace(trace, row=1, col=2)
for trace in fig2a["data"]:
    fig12.add_trace(trace, row=2, col=1)
for trace in fig5["data"]:
    fig12.add_trace(trace, row=2, col=2)
for trace in fig6["data"]:
    trace['legendgroup'] = trace['name']
    fig12.add_trace(trace, row=3, col=1)
for trace in fig6a["data"]:
    fig12.add_trace(trace, row=3, col=2)
for trace in fig7["data"]:
    fig12.add_trace(trace, row=4, col=1)
for trace in fig8["data"]:
    fig12.add_trace(trace, row=4, col=2)
for trace in fig9["data"]:
    fig12.add_trace(trace, row=5, col=1)
for trace in fig10["data"]:
    fig12.add_trace(trace, row=5, col=2)

# Copy x- and y-axis titles from individual figures to subplots
fig12.update_xaxes(title=fig1.layout.xaxis.title, row=1, col=1)
fig12.update_xaxes(title=fig2.layout.xaxis.title, row=1, col=2)
fig12.update_xaxes(title=fig2a.layout.xaxis.title, row=2, col=1)
fig12.update_xaxes(showticklabels=False, row=2, col=2)
fig12.update_xaxes(title=fig6.layout.xaxis.title, row=3, col=1)
fig12.update_xaxes(title=fig6a.layout.xaxis.title, row=3, col=2)
fig12.update_xaxes(title=fig7.layout.xaxis.title, row=4, col=1)
fig12.update_xaxes(title=fig8.layout.xaxis.title, row=4, col=2)
fig12.update_xaxes(title=fig9.layout.xaxis.title, row=5, col=1)
fig12.update_xaxes(title=fig10.layout.xaxis.title, row=5, col=2)

fig12.update_yaxes(title=fig1.layout.yaxis.title, row=1, col=1)
fig12.update_yaxes(title=fig2.layout.yaxis.title, row=1, col=2)
fig12.update_yaxes(title=fig2a.layout.yaxis.title, row=2, col=1)
fig12.update_yaxes(title=fig5.layout.yaxis.title, row=2, col=2)
fig12.update_yaxes(title=fig6.layout.yaxis.title, row=3, col=1)
fig12.update_yaxes(title=fig6a.layout.yaxis.title, row=3, col=2)
fig12.update_yaxes(title=fig7.layout.yaxis.title, row=4, col=1)
fig12.update_yaxes(title=fig8.layout.yaxis.title, row=4, col=2)
fig12.update_yaxes(title=fig9.layout.yaxis.title, row=5, col=1)
fig12.update_yaxes(title=fig10.layout.yaxis.title, row=5, col=2)

# Get screen resolution
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Update layout settings for the dashboard
fig12.update_layout(
    height=screen_height * 5,
    width=screen_width * 2,
    # showlegend=False,
    # legend_title="<b>General Legend:<b><br>",
    legend=dict(y=0.5, bgcolor="rgba(255, 255, 255, 0.5)"),
    legend_font_color="#262626",
    title_text='<b style="font-size:24px">A Simple Iris Dataset Dashboard</b>',
    font_family="Montserrat",
    template="plotly_dark",
)

# Display the dashboard
fig12.show()

# Save the interactive HTML dashboard
fig12.write_html("./HTMLs/big_iris_dataset_dashboard.html")

# -----------------------------------------------------------------------------------------#
# Explanation:

# The code uses Plotly's make_subplots to create a 5x2 grid for subplots.
# Each subplot corresponds to a different chart from previous examples.
# Individual traces from existing figures (fig1, fig2, etc.) are added to the respective subplots.
# X- and y-axis titles are copied from individual figures to the corresponding subplots.
# The layout is updated with screen resolution, legend settings, title, font family, and a dark template.
# The resulting dashboard is displayed and saved as an interactive HTML file.
# -----------------------------------------------------------------------------------------#