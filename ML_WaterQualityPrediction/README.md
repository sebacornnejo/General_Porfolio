# Water Quality Prediction Project (Extended)

[Link Colab ->](https://colab.research.google.com/drive/1bnJOI4WIvq2wHJUM7kKb_NVx9fgnAb5r?usp=sharing)

## Overview

This project aims to develop a machine learning model for predicting water quality based on a dataset obtained from '[water.csv](https://www.kaggle.com/datasets/xiaoxiaoliangzi/water-potability-prediction)'. The dataset is an extension of the classic '[water_potability.csv](https://www.kaggle.com/datasets/uom190346a/water-quality-and-potability/data)'. The dataset contains various features related to water quality, and the goal is to build a predictive model that can classify water samples into different quality categories.

## Data Sampling

The original dataset ('water.csv') consists of 349,440 rows and 16 features. Due to computational constraints, we have extracted two subsets from the original data:

- **Training and Validation Dataset (`df`):** A 10% random sample (34,944 rows) for developing and validating the machine learning model.

- **Evaluation Dataset (`df_rest`):** A 1% random sample (3,494 rows) for evaluating the model's performance with unseen data.

The sampling approach balances the need for representative datasets with computational efficiency.

## Visualizations

The project incorporates various visualizations to better understand the dataset and model performance. Some notable visualizations include:

- **Potability Index Bar Chart (`fig1`):**
  - A bar chart representing the distribution of potability labels (0 and 1) in the dataset. This provides a quick overview of the potability index.

- **Distribution of Water Quality Features (`fig2`):**
  - A subplot of histograms and kernel density estimations for each feature in the dataset. This visualization aids in understanding the distribution of individual features. [View HTML](https://sebacornnejo.github.io/DistributionOfWaterQualityFeatures.html)

- **Pairwise Relationship Scatter Matrix (`fig3`):**
  - A scatter matrix representing the pairwise relationships between features, colored by potability. This visualization helps identify potential correlations between features. [View HTML](https://sebacornnejo.github.io/PairwiseRelationship.html)

- **Correlation Heatmap (`fig4`):**
  - A heatmap displaying the correlation matrix between water quality features. This visualization highlights potential relationships and dependencies among features. [View HTML](https://sebacornnejo.github.io/HeatmapBetweenWaterQualityFeatures.html)

- **Feature Values Distribution Box Plots (`fig5`):**
  - Box plots illustrating the distribution of feature values in the dataset. This visualization provides insights into the variability and potential outliers in the data. [View HTML](https://sebacornnejo.github.io/FeatureValuesDistribution.html)

## Implementation Details

The project includes the implementation of the following machine learning models:

- **Decision Tree (DT):**
  - A Decision Tree classifier is trained and tuned using grid search for optimal hyperparameters.

- **K-Nearest Neighbors (KNN):**
  - A K-Nearest Neighbors classifier is implemented with specific hyperparameters.

## Model Evaluation

The models are evaluated using various metrics, including accuracy, classification reports and confusion matrix (`fig6`, `fig7`, `fig8`, and `fig9`). The evaluation process involves training on the `df` subset and testing on the `df_rest` subset to ensure robust model performance.

## Saved Models

The trained models, both individual classifiers (DT and KNN) and hyperparameter-tuned models (gridsearch_dth and gridsearch_knnh), are saved using the `joblib` library. These saved models can be loaded for further analysis or deployment.

## How to Use

1. Clone the repository: `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/ML_WaterQualityPrediction`
2. Install the required libraries: `pip install -r requirements.txt`
3. Run the individual analysis scripts or the full dashboard script.
4. Explore the generated charts and dashboard HTML files.

### Additional Codes

- [discrete_colorscale.py](discrete_colorscale.py)

This Python function associates a discrete color scale with a list of limit values for the ranges to be highlighted in the color bar.

For detailed comments and code, view the [predefined_codes.py](predefined_codes.py).

### Note: Visualizations and outputs are displayed using Plotly, and other relevant libraries
