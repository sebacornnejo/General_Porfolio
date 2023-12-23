# Solar Power Generation Prediction using LSTM

[Link Colab ->](https://colab.research.google.com/drive/1rAGf3-Y-jNnY-XaMYYgaplfMfuAPmbqW?usp=sharing)

This repository contains a Jupyter Notebook ([SimpleSolarPred_LSTM.ipynb](SimpleSolarPred_LSTM.ipynb)) that demonstrates the prediction of solar power generation using a Long Short-Term Memory (LSTM) neural network. The notebook covers data preprocessing, model training, evaluation, and visualization of the results.

## Overview

### Dataset

The dataset used for this project includes various environmental and power-related features recorded at a solar power generation location. These features include air temperature, humidity, wind speed, solar radiation, and more.

### Notebook Structure

- **Data Exploration:** Initial exploration of the dataset, including data sampling, feature descriptions, and visualization of feature distributions.
- **Preprocessing:** Extraction of training and validation datasets, optimization of memory usage, and feature scaling for better model performance.
- **Exploratory Data Analysis (EDA):** Visualization of feature distributions using histograms and kernel density estimation to understand underlying data patterns.
- **Correlation Analysis:** Calculation of correlation matrices to identify relationships between features.
- **Model Development:** Implementation of an LSTM model using TensorFlow and Keras for solar power generation prediction.
- **Training and Evaluation:** Model training on the training set and evaluation on a separate validation set to assess generalization performance.
- **Model Evaluation on Unseen Data:** Model evaluation on a separate test set (unseen data) to measure its performance on real-world scenarios.
- **Visualization of Results:** Visualization of the model's prediction compared to actual values in the test set.

## How to Use

1. **Clone the Repository:** `git clone --depth=1 --filter=blob:none https://github.com/sebacornnejo/General_Porfolio.git/SimpleRNN_SolarPrediction`
2. **Install the required libraries:** `pip install -r requirements.txt`

## Results

The notebook provides insights into the relationships within the dataset, the performance of the LSTM model, and visualizations comparing predicted and actual values of solar power generation.

Feel free to explore and adapt the notebook for your own projects.

Happy coding!
