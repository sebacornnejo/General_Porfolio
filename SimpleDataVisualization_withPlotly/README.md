# Simple Iris Dataset Visualization

## Overview

This repository provides Python code for visualizing the Iris dataset using Plotly and Plotly Express. The code is organized into multiple sections, each focusing on a specific type of plot or visualization. These visualizations include scatterplots, boxplots, histograms, and more.

## Table of Contents

1. [Requirements](#requirements)
2. [Cloning the Repository](#cloning-the-repository)
3. [Scatterplot](#scatterplot)
   - [Basic Scatterplot](#basic-scatterplot)
   - [Scatterplot with Color and Size](#scatterplot-with-color-and-size)
   - [Scatterplot with Regression Lines](#scatterplot-with-regression-lines)
   - [Scatterplot with Marginal Plots](#scatterplot-with-marginal-plots)

4. [Boxplot](#boxplot)
   - [Simple Boxplot](#simple-boxplot)
   - [Boxplot Comparison](#boxplot-comparison)

5. [Histogram](#histogram)
   - [Simple Histogram](#simple-histogram)
   - [Multiple Histograms](#multiple-histograms)
   - [Histogram for General Counting](#histogram-for-general-counting)

6. [Dashboard](#dashboard)

## Requirements

To run the code in this repository, you need the following:

- Python 3.x
- Required Python libraries: Plotly, Plotly Express, NumPy, and Screeninfo

Install the required libraries using the following command: `pip install requirements.txt`

## Cloning the Repository

To clone this repository, use the following command: `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/SimpleDataVisualization_withPlotly`

## Scatterplot

### Basic Scatterplot

- **Visual Output:** A basic scatterplot of sepal length and width is included with customization options.
- **Interactive Chart:** [Interactive HTML Scatterplot](https://sebacornnejo.github.io/scatterplot_basic.html)

### Scatterplot with Color and Size

- **Visual Output:** A scatter plot is explored with variations in color and size depending on the species and sepal width.
- **Interactive Chart:** [Interactive HTML Scatterplot with Color and Size](https://sebacornnejo.github.io/scatterplot_color_size.html)

### Scatterplot with Regression Lines

- **Visual Output:** Regression lines are added to a scatterplot representing the relationship between sepal width and length.
- **Interactive Chart:** [Interactive HTML Scatterplot with Regression Lines](https://sebacornnejo.github.io/scatterplot_regression.html)

### Scatterplot with Marginal Plots

- **Visual Output:** A scatter plot with marginal box plots for sepal width and length is included, along with regression lines.
- **Interactive Chart:** [Interactive HTML Scatterplot with Marginal Plots](https://sebacornnejo.github.io/scatterplot_marginal_plots.html)

## Boxplot

### Simple Boxplot

- **Visual Output:** A simple boxplot of sepal width is presented with customization options.
- **Interactive Chart:** [Interactive HTML Boxplot](https://sebacornnejo.github.io/boxplot_sepal_width.html)

### Boxplot Comparison

- **Visual Output:** A boxplot comparison is created using different colors for each species.
- **Interactive Chart:** [Interactive HTML Boxplot Comparison](https://sebacornnejo.github.io/boxplot_species_comparison.html)

## Histogram

### Simple Histogram

- **Visual Output:** A simple histogram of sepal width with percentage intervals is developed.
- **Interactive Chart:** [Interactive HTML Histogram](https://sebacornnejo.github.io/histogram_sepal_width.html)

### Multiple Histograms

- **Visual Output:** A multiple histogram is generated, showcasing the distribution of sepal width for each species.
- **Interactive Chart:** [Interactive HTML Multiple Histogram](https://sebacornnejo.github.io/histogram_species_overlay.html)

### Histogram for General Counting

- **Visual Output:** A histogram for the overall count is presented with a color palette.
- **Interactive Chart:** [Interactive HTML Histogram for General Counting](https://sebacornnejo.github.io/histogram_general_count.html)

## Dashboard

- **Visual Output:** A dashboard is developed using Plotly's make_subplots to combine various visualizations.
- **Interactive Chart:** [Interactive HTML Dashboard](https://sebacornnejo.github.io/big_iris_dataset_dashboard.html)

**Note:** Feel free to explore the interactive HTML files by clicking on the provided links. For a comprehensive view, open the dashboard to visualize multiple charts at once.
**Note:** Uncomment the `fig.show()` lines in the individual analysis scripts if you want to display the charts interactively in your development environment.
