import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV,
    RandomizedSearchCV,
    StratifiedKFold,
    cross_val_score,
    cross_validate
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification

# Models to tune
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# For RandomizedSearchCV parameter distributions
from scipy.stats import randint, uniform

# Metrics
from sklearn.metrics import accuracy_score, f1_score, make_scorer

print("--- Scikit-learn Hyperparameter Tuning Demo ---")
print("Libraries imported successfully!\n")

# --- 1. Setting up Data ---

print("1. Setting up Data: Synthetic Classification Dataset")
X, y = make_classification(
    n_samples=1000,
    n_features=15,
    n_informative=8,
    n_redundant=2,
    n_classes=2,
    weights=[0.8, 0.2], # Slightly imbalanced
    random_state=42
)
print(f"Dataset generated. X shape: {X.shape}, y shape: {y.shape}")
print(f"Class distribution: {np.bincount(y)}\n")

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Data split. X_train shape: {X_train.shape}, X_test shape: {X_test.shape}\n")
print("=" * 50 + "\n")


# --- 2. Grid Search (`GridSearchCV`) ---

print("2. Grid Search (`GridSearchCV`): Exhaustive Search")

# Define the model
model_gs = RandomForestClassifier(random_state=42)

# Define the parameter grid
# 'n_estimators': Number of trees in the forest
# 'max_depth': Maximum depth of the tree
# 'min_samples_split': Minimum number of samples required to split an internal node
param_grid_rf = {
    'n_estimators': [50, 100, 150],
    'max_depth': [10, 20, None], # None means unlimited depth
    'min_samples_split': [2, 5, 10],
    'criterion': ['gini', 'entropy']
}

# Create GridSearchCV object
# cv: number of folds for cross-validation
# scoring: metric to optimize (e.g., 'accuracy', 'f1', 'roc_auc')
# n_jobs: number of CPU cores to use (-1 means all available)
# verbose: verbosity level (higher means more messages)
grid_search = GridSearchCV(
    estimator=model_gs,
    param_grid=param_grid_rf,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), # Use stratified for imbalanced classification
    scoring='f1', # Optimize for F1-score due to imbalance
    n_jobs=-1,
    verbose=2
)

print("  Starting Grid Search for RandomForestClassifier...")
grid_search.fit(X_train, y_train)

print("\n  Grid Search Results:")
print(f"    Best parameters: {grid_search.best_params_}")
print(f"    Best cross-validation score (F1): {grid_search.best_score_:.4f}")

# Evaluate on the unseen test set using the best estimator
best_model_gs = grid_search.best_estimator_
y_pred_gs = best_model_gs.predict(X_test)
test_f1_gs = f1_score(y_test, y_pred_gs)
test_acc_gs = accuracy_score(y_test, y_pred_gs)
print(f"    Test set F1 score with best model: {test_f1_gs:.4f}")
print(f"    Test set Accuracy with best model: {test_acc_gs:.4f}")

# You can inspect all results
# results_df = pd.DataFrame(grid_search.cv_results_)
# print("\n  Sample of GridSearchCV CV results (first 5 rows):\n", results_df.head())
print("\n" + "=" * 50 + "\n")


# --- 3. Randomized Search (`RandomizedSearchCV`) ---

print("3. Randomized Search (`RandomizedSearchCV`): Random Sampling")
# More efficient for large search spaces. Explores a random subset of combinations.

# Define the model (same as before)
model_rs = RandomForestClassifier(random_state=42)

# Define the parameter distributions
# Use scipy.stats distributions for numerical hyperparameters
param_dist_rf = {
    'n_estimators': randint(50, 300), # Integer between 50 and 300
    'max_depth': randint(5, 50),     # Integer between 5 and 50
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'criterion': ['gini', 'entropy']
}

# Create RandomizedSearchCV object
# n_iter: number of parameter settings that are sampled (trade-off between runtime and performance)
random_search = RandomizedSearchCV(
    estimator=model_rs,
    param_distributions=param_dist_rf,
    n_iter=20, # Number of random combinations to try
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring='f1',
    random_state=42, # For reproducibility of random sampling
    n_jobs=-1,
    verbose=2
)

print("  Starting Randomized Search for RandomForestClassifier...")
random_search.fit(X_train, y_train)

print("\n  Randomized Search Results:")
print(f"    Best parameters: {random_search.best_params_}")
print(f"    Best cross-validation score (F1): {random_search.best_score_:.4f}")

# Evaluate on the unseen test set using the best estimator
best_model_rs = random_search.best_estimator_
y_pred_rs = best_model_rs.predict(X_test)
test_f1_rs = f1_score(y_test, y_pred_rs)
test_acc_rs = accuracy_score(y_test, y_pred_rs)
print(f"    Test set F1 score with best model: {test_f1_rs:.4f}")
print(f"    Test set Accuracy with best model: {test_acc_rs:.4f}")
print("\n" + "=" * 50 + "\n")


# --- 4. Pipelines with Hyperparameter Tuning ---

print("4. Pipelines with Hyperparameter Tuning:")
# Essential for proper preprocessing (e.g., scaling) within each cross-validation fold
# to prevent data leakage from the test fold into the training process.

# Define a pipeline with preprocessing and a model
pipeline_svc = Pipeline([
    ('scaler', StandardScaler()), # Step 1: Scale features
    ('svc', SVC(random_state=42)) # Step 2: Support Vector Classifier
])

# Define the parameter grid for the pipeline
# Hyperparameters are accessed using the format 'step_name__parameter_name'
param_grid_svc = {
    'svc__C': [0.1, 1, 10],            # Regularization parameter
    'svc__kernel': ['linear', 'rbf'],  # Kernel type
    'svc__gamma': ['scale', 0.1, 1]    # Kernel coefficient for 'rbf', 'poly' and 'sigmoid'
}

# Perform Grid Search on the pipeline
grid_search_pipeline = GridSearchCV(
    estimator=pipeline_svc,
    param_grid=param_grid_svc,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring='f1',
    n_jobs=-1,
    verbose=2
)

print("  Starting Grid Search for SVC Pipeline (Scaler + SVC)...")
# Fit the pipeline's GridSearchCV to the original (unscaled) training data.
# The pipeline handles scaling internally within each CV fold.
grid_search_pipeline.fit(X_train, y_train)

print("\n  SVC Pipeline Grid Search Results:")
print(f"    Best parameters: {grid_search_pipeline.best_params_}")
print(f"    Best cross-validation score (F1): {grid_search_pipeline.best_score_:.4f}")

# Evaluate on the unseen test set using the best pipeline
best_pipeline_svc = grid_search_pipeline.best_estimator_
y_pred_pipe_svc = best_pipeline_svc.predict(X_test)
test_f1_pipe_svc = f1_score(y_test, y_pred_pipe_svc)
test_acc_pipe_svc = accuracy_score(y_test, y_pred_pipe_svc)
print(f"    Test set F1 score with best pipeline: {test_f1_pipe_svc:.4f}")
print(f"    Test set Accuracy with best pipeline: {test_acc_pipe_svc:.4f}")
print("\n" + "=" * 50 + "\n")


# --- 5. Nested Cross-Validation (for reliable performance estimation) ---

print("5. Nested Cross-Validation:")
# Provides a more robust estimate of the model's generalization performance
# by having an outer loop for evaluation and an inner loop for hyperparameter tuning.

# Define the inner cross-validation for tuning
inner_cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

# Define the outer cross-validation for performance estimation
outer_cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Define the GridSearchCV object (this is the 'inner' loop)
# Use a smaller grid for faster demonstration
param_grid_nested = {
    'svc__C': [0.1, 1],
    'svc__kernel': ['rbf']
}

# The GridSearchCV object itself acts as the 'estimator' for the outer cross_val_score
nested_grid_search = GridSearchCV(
    estimator=pipeline_svc, # Use the pipeline defined earlier
    param_grid=param_grid_nested,
    cv=inner_cv,
    scoring='f1',
    n_jobs=-1
)

# Perform nested cross-validation
# This will run the inner GridSearchCV for each fold of the outer_cv
print("  Starting Nested Cross-Validation for SVC Pipeline...")
nested_scores = cross_val_score(
    nested_grid_search, # The estimator is the GridSearchCV object
    X, y,               # Use the full dataset here, as the outer CV splits it
    cv=outer_cv,
    scoring='f1',
    n_jobs=-1,
    verbose=1
)

print("\n  Nested Cross-Validation Results:")
print(f"    Individual outer fold F1 scores: {nested_scores}")
print(f"    Mean Nested CV F1 score: {nested_scores.mean():.4f}")
print(f"    Standard Deviation of Nested CV F1 score: {nested_scores.std():.4f}")
print("\n  This mean score is a more reliable estimate of how the model (and its tuning process)\n  will perform on truly unseen data.")

print("\nHyperparameter tuning demonstration complete!")