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
    xaxis_title="Sepal Width",
    yaxis_title="Sepal Length",
    font_family="Montserrat",
)

# Adjust point size fixedly
fig1.update_traces(marker=dict(size=12, line=dict(color="#F2F2F2", width=2)))

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

fig2.update_traces(
    marker=dict(line=dict(color="#F2F2F2", width=1))
)

# Customize the layout
fig2.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# -----------------------------------------------------------------------------------------#
# Similar to Scatterplot with Color and Size of Fig2
fig3 = px.scatter(
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

fig3.update_traces(marker=dict(line=dict(color="#F2F2F2", width=1)))

# Customize the layout
fig3.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)


# -----------------------------------------------------------------------------------------#
# Boxplot

fig4 = px.box(
    df,
    y="sepal_width",
    title='<b style="font-size:24px>A Simple Boxplot</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width"},
    template="plotly_dark",
    color_discrete_sequence=["#3F7AD8"],
)


fig4.update_traces(
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
fig4.update_layout(
    font_family="Montserrat",
)

scatter_trace = go.Scatter(
    y=df["sepal_width"],
    mode="markers",
    marker=dict(color="#12BF80", size=8),
    hovertemplate="Width: %{y}",
    name="",
    showlegend=False,
)

fig4.add_trace(scatter_trace)

# Ajustar las posiciones x de los puntos del scatter plot y el boxplot
fig4.update_traces(xaxis="x", x0=0, dx=0.2, selector=dict(type="box"))
fig4.update_traces(xaxis="x", x0=-0.35, dx=0.0004, selector=dict(type="scatter"))

# Ocultar los valores del eje x
fig4.update_xaxes(showticklabels=False)

# -----------------------------------------------------------------------------------------#

# Boxplot Comparison
# Lista de colores de relleno para los boxplots
fill_colors = ["#6331C5", "#3F7AD8", "#12BF80"]

# Crear una lista de Box traces con colores personalizados
box_traces = []
for i in range(len(fill_colors)):
    box_trace = go.Box(
        x=df[df["species"] == df["species"].unique()[i]]["species"],
        y=df[df["species"] == df["species"].unique()[i]]["sepal_width"],
        name=df["species"].unique()[i],
        # marker=dict(color=fill_colors[i], outliercolor=line_colors[i], line=dict(color=line_colors[i])),
        marker=dict(
            color=fill_colors[i],
            line=dict(color=fill_colors[i]),
        ),
        line=dict(color="#F2F2F2"),
        fillcolor=fill_colors[i],
        boxpoints="all",
    )
    box_traces.append(box_trace)

# Crear la figura y agregar los boxplots personalizados
fig5 = go.Figure(box_traces)

# Configuraciones adicionales
fig5.update_layout(
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

# -----------------------------------------------------------------------------------------#
# Similar to Boxplot Comparison of Fig5
fig6 = px.box(
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

fig6.update_traces(
    marker=dict(color="#12BF80"),  # Color de relleno
    line=dict(color="#F2F2F2"),  # Color de línea de contorno
)

# Customize the layout
fig6.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.96, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# -----------------------------------------------------------------------------------------#
# Histogram
import numpy as np

# Calculate percentage bins from histogram using numpy
# This is because Plotly does not have the ability to display "count" and "percent" at the same time in "hover"
bin = 13
hist, bin_edges = np.histogram(df["sepal_width"], bins=bin, density=False)
hist_percent = (hist / len(df)) * 100

fig7 = px.histogram(
    df,
    x="sepal_width",
    nbins=bin,
    title='<b style="font-size:24px>A Simple Histogram</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={"sepal_width": "Sepal Width"},
    template="plotly_dark",
    color_discrete_sequence=["#6331C5"],
)

fig7.update_traces(
    marker=dict(line=dict(color="#F2F2F2", width=0.5)),
    hovertemplate="Bin: %{x}<br>Count: %{y}<br>Percent: %{customdata:.2f}%",
    customdata=hist_percent,
)

# Customize the layout
fig7.update_layout(font_family="Montserrat")

# Agrega líneas para promedio, mediana y desviación estándar
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

fig7.update_yaxes(title_text="")

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

# -----------------------------------------------------------------------------------------#
# Histogram for General Counting
import screeninfo

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

df_sorted = df.sort_values(by="sepal_width", ascending=False)

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
    font_family="Montserrat",
    showlegend=True,
    yaxis_title=" ",
    legend_title="<b>Sepal Width:<b>",
    legend=dict(bgcolor="rgba(255, 255, 255, 0.5)", traceorder="reversed"),
    legend_font_color="#262626",
)

fig9.update_traces(hovertemplate="<b>Percent</b>: %{y:.2f}%")

# -----------------------------------------------------------------------------------------#
# Scatterplot with Regression Lines
fig10 = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    trendline="ols",
    title='<b style="font-size:24px>A Simple Scatterplot with Regression Lines</b><br><span style="font-size:14px;">from Iris Dataset</span>',
    labels={
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "species": "Species",
    },
    template="plotly_dark",
    color_discrete_sequence=["#6331C5", "#3F7AD8", "#12BF80"],
)

fig10.update_traces(marker=dict(size=10, line=dict(color="#F2F2F2", width=0.5)))
# Customize the layout
fig10.update_layout(
    font_family="Montserrat",
    showlegend=True,
    legend_title="<b>Species:<b>",
    legend=dict(x=0.74, y=0.08, bgcolor="rgba(255, 255, 255, 0.5)", orientation="h"),
    legend_font_color="#262626",
)

# -----------------------------------------------------------------------------------------#
# Create a Dashboard with make_subplots
from plotly.subplots import make_subplots

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
        "A Simple Histogram Chart for General Percentage",
        "A Simple Scatterplot with Regression Lines",
    ],
    horizontal_spacing=0.035,
    vertical_spacing=0.025,
)

# Add traces to the subplots
for trace in fig1['data']:
    fig12.add_trace(trace, row=1, col=1)
for trace in fig2['data']:
    fig12.add_trace(trace, row=1, col=2)
for trace in fig3['data']:
    fig12.add_trace(trace, row=2, col=1)
for trace in fig4['data']:
    fig12.add_trace(trace, row=2, col=2)
for trace in fig5['data']:
    fig12.add_trace(trace, row=3, col=1)
for trace in fig6['data']:
    fig12.add_trace(trace, row=3, col=2)
for trace in fig7['data']:
    fig12.add_trace(trace, row=4, col=1)
for trace in fig8['data']:
    fig12.add_trace(trace, row=4, col=2)
for trace in fig9['data']:
    fig12.add_trace(trace, row=5, col=1)
for trace in fig10['data']:
    fig12.add_trace(trace, row=5, col=2)
# fig12.add_trace(fig9["data"][0], row=5, col=1)
# fig12.add_trace(fig11["data"][0], row=5, col=2)
# fig12.add_trace(fig10['data'][0], row=5, col=2)


# Get screen resolution
screen_info = screeninfo.get_monitors()
screen_width = screen_info[0].width
screen_height = screen_info[0].height

# Update layout
fig12.update_layout(
    height=screen_height*5,
    width=screen_width*2,
    # showlegend=False,
    title_text='<b style="font-size:24px">A Simple Iris Dataset Dashboard</b>',
    font_family="Montserrat",
    template="plotly_dark",
)

# Save the interactive HTML dashboard
fig12.write_html("iris_dataset_dashboard.html")

# Display the dashboard
fig12.show()
