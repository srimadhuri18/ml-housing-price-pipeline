# End-to-End Machine Learning Pipeline for Housing Price Prediction

## Project Overview

This project implements a complete end-to-end machine learning pipeline to predict housing prices using the California Housing dataset. The objective is to demonstrate the full lifecycle of a machine learning workflow, including data loading, preprocessing, model training, evaluation, and prediction.

The project compares multiple machine learning models to determine the most effective approach for predicting housing prices based on demographic and geographic features.

This project highlights practical skills in machine learning, data preprocessing, and model evaluation using Python and Scikit-learn.

---

## Objectives

The main goals of this project are:

* Build a complete machine learning pipeline
* Perform data preprocessing and feature scaling
* Train multiple machine learning models
* Evaluate model performance using appropriate metrics
* Identify the best-performing model for the prediction task

---

## Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

## Machine Learning Pipeline

The project follows a structured machine learning pipeline:

```text
Data Loading
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Prediction
```

---

## Dataset

The project uses the **California Housing Dataset**, which contains information collected from the 1990 California census.

### Dataset Features

* Median Income
* House Age
* Average Rooms
* Average Bedrooms
* Population
* Average Occupancy
* Latitude
* Longitude

### Target Variable

* Median House Value

The dataset allows the model to learn relationships between housing features and property prices.

---

## Project Structure

```text
ml-housing-price-pipeline
│
├── data
│
├── src
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── evaluate_model.py
│   └── predict.py
│
├── models
│
├── requirements.txt
└── run_pipeline.py
```

### Folder Description

**data/**
Contains the dataset used for training and evaluation.

**notebooks/**
Contains exploratory data analysis and experimentation.

**src/**
Contains modular Python scripts implementing the machine learning pipeline.

**models/**
Stores trained machine learning models.

**run_pipeline.py**
Main script that executes the entire pipeline.

**requirements.txt**
List of required Python libraries.

---

## Machine Learning Models Used

The project compares multiple regression algorithms:

### Linear Regression

A baseline model that captures linear relationships between features and target values.

### Decision Tree Regressor

A non-linear model capable of capturing complex feature interactions.

### Random Forest Regressor

An ensemble learning method that improves prediction accuracy by combining multiple decision trees.

---

## Model Evaluation

Models are evaluated using standard regression metrics:

**Root Mean Squared Error (RMSE)**
Measures the average magnitude of prediction errors.

**R² Score**
Represents the proportion of variance explained by the model.

The model with the lowest RMSE and highest R² score is selected as the best-performing model.

---

## Installation

Clone the repository:

```
git clone https://github.com/srimadhuri18/ml-housing-price-pipeline.git
```

Navigate to the project directory:

```
cd ml-housing-price-pipeline
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

Run the complete pipeline using:

```
python run_pipeline.py
```

The script performs the following steps:

1. Loads the dataset
2. Preprocesses the data
3. Splits the data into training and testing sets
4. Trains multiple machine learning models
5. Evaluates model performance
6. Displays evaluation metrics

---

## Example Output

Example model performance results:

```
Model: Linear Regression
RMSE: 0.72
R2 Score: 0.60

Model: Decision Tree
RMSE: 0.65
R2 Score: 0.70

Model: Random Forest
RMSE: 0.50
R2 Score: 0.82
```

Random Forest typically achieves the best performance among the tested models.

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Machine Learning Pipelines
* Data Preprocessing and Feature Scaling
* Model Training and Evaluation
* Regression Algorithms
* Python for Machine Learning
* Modular Code Design
* Reproducible ML Workflows

---

## Future Improvements

Possible extensions to enhance the project:

* Hyperparameter tuning using GridSearchCV
* Cross-validation for better model reliability
* Feature engineering for improved accuracy
* Model deployment using FastAPI or Flask
* Interactive dashboards for visualization

---


This project is intended for educational and research purposes.
