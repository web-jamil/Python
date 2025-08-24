import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification, make_regression

# Classification Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Regression Models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Metrics
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc,
    mean_squared_error, mean_absolute_error, r2_score
)

print("--- Scikit-learn Supervised Learning Demo ---")
print("Libraries imported successfully!\n")

# --- 1. Setting up Data ---

print("1. Setting up Data: Synthetic Datasets")

# 1.1 Classification Dataset
X_clf, y_clf = make_classification(
    n_samples=1000,          # Number of samples
    n_features=10,           # Total number of features
    n_informative=5,         # Number of informative features
    n_redundant=2,           # Number of redundant features
    n_repeated=0,            # Number of repeated features
    n_classes=2,             # Number of target classes
    n_clusters_per_class=1,  # Number of clusters per class
    weights=[0.8, 0.2],      # Class imbalance (80% class 0, 20% class 1)
    flip_y=0.01,             # Noise
    random_state=42          # For reproducibility
)
print(f"Classification dataset generated. X_clf shape: {X_clf.shape}, y_clf shape: {y_clf.shape}")
print(f"Class distribution: {np.bincount(y_clf)}")
print("-" * 30)

# 1.2 Regression Dataset
X_reg, y_reg = make_regression(
    n_samples=1000,          # Number of samples
    n_features=10,           # Total number of features
    n_informative=8,         # Number of informative features
    noise=10,                # Gaussian noise in the output
    random_state=42          # For reproducibility
)
print(f"Regression dataset generated. X_reg shape: {X_reg.shape}, y_reg shape: {y_reg.shape}\n")
print("=" * 50 + "\n")

# --- Splitting Data for all models ---
X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(
    X_clf, y_clf, test_size=0.3, random_state=42, stratify=y_clf
)

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

# Scaling numerical features is often crucial. We'll use a pipeline for cleaner code later.
# For now, let's scale manually for individual model demos.
scaler_clf = StandardScaler()
X_clf_train_scaled = scaler_clf.fit_transform(X_clf_train)
X_clf_test_scaled = scaler_clf.transform(X_clf_test)

scaler_reg = StandardScaler()
X_reg_train_scaled = scaler_reg.fit_transform(X_reg_train)
X_reg_test_scaled = scaler_reg.transform(X_reg_test)


# --- 2. Classification Algorithms, Training, Prediction, and Evaluation ---

print("2. Classification Algorithms, Training, Prediction & Evaluation:")

classification_models = {
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=200),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree Classifier": DecisionTreeClassifier(random_state=42),
    "Support Vector Classifier (SVC)": SVC(probability=True, random_state=42), # probability=True for ROC-AUC
    "Random Forest Classifier": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=100, random_state=42)
}

results_clf = {}

for name, model in classification_models.items():
    print(f"\n--- Training {name} ---")

    # Some models benefit from scaling, others are less sensitive.
    # For a general demo, we'll use scaled data where appropriate.
    if name in ["Logistic Regression", "K-Nearest Neighbors", "Support Vector Classifier (SVC)"]:
        X_train_data = X_clf_train_scaled
        X_test_data = X_clf_test_scaled
    else: # Decision Tree, Random Forest, Gradient Boosting are less sensitive to scaling
        X_train_data = X_clf_train
        X_test_data = X_clf_test

    model.fit(X_train_data, y_clf_train)
    y_pred = model.predict(X_test_data)
    y_pred_proba = model.predict_proba(X_test_data)[:, 1] if hasattr(model, "predict_proba") else None

    # Evaluation
    accuracy = accuracy_score(y_clf_test, y_pred)
    precision = precision_score(y_clf_test, y_pred)
    recall = recall_score(y_clf_test, y_pred)
    f1 = f1_score(y_clf_test, y_pred)
    cm = confusion_matrix(y_clf_test, y_pred)

    print(f"  Accuracy: {accuracy:.4f}")
    print(f"  Precision: {precision:.4f}")
    print(f"  Recall: {recall:.4f}")
    print(f"  F1-Score: {f1:.4f}")
    print(f"  Confusion Matrix:\n{cm}")

    # ROC-AUC (only for models that support predict_proba)
    if y_pred_proba is not None:
        fpr, tpr, _ = roc_curve(y_clf_test, y_pred_proba)
        roc_auc = auc(fpr, tpr)
        print(f"  ROC-AUC: {roc_auc:.4f}")

        # Plot ROC curve for one model (Logistic Regression)
        if name == "Logistic Regression":
            plt.figure(figsize=(6, 5))
            plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
            plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
            plt.xlim([0.0, 1.0])
            plt.ylim([0.0, 1.05])
            plt.xlabel('False Positive Rate')
            plt.ylabel('True Positive Rate')
            plt.title('Receiver Operating Characteristic (ROC) Curve')
            plt.legend(loc="lower right")
            plt.show()

    results_clf[name] = {
        "accuracy": accuracy, "precision": precision,
        "recall": recall, "f1_score": f1, "roc_auc": roc_auc if y_pred_proba is not None else None
    }

print("\nClassification Model Summary:")
for name, metrics in results_clf.items():
    print(f"- {name}: Acc={metrics['accuracy']:.3f}, F1={metrics['f1_score']:.3f}, ROC-AUC={metrics['roc_auc']:.3f if metrics['roc_auc'] is not None else 'N/A'}")
print("\n" + "=" * 50 + "\n")


# --- 3. Regression Algorithms, Training, Prediction, and Evaluation ---

print("3. Regression Algorithms, Training, Prediction & Evaluation:")

regression_models = {
    "Linear Regression": LinearRegression(),
    "Ridge Regression": Ridge(alpha=1.0, random_state=42),
    "Lasso Regression": Lasso(alpha=0.1, random_state=42),
    "Decision Tree Regressor": DecisionTreeRegressor(random_state=42),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=100, random_state=42),
    "Gradient Boosting Regressor": GradientBoostingRegressor(n_estimators=100, random_state=42)
}

results_reg = {}

for name, model in regression_models.items():
    print(f"\n--- Training {name} ---")

    if name in ["Linear Regression", "Ridge Regression", "Lasso Regression"]:
        X_train_data = X_reg_train_scaled
        X_test_data = X_reg_test_scaled
    else: # Decision Tree, Random Forest, Gradient Boosting are less sensitive to scaling
        X_train_data = X_reg_train
        X_test_data = X_reg_test

    model.fit(X_train_data, y_reg_train)
    y_pred = model.predict(X_test_data)

    # Evaluation
    mse = mean_squared_error(y_reg_test, y_pred)
    rmse = np.sqrt(mse) # Root Mean Squared Error
    mae = mean_absolute_error(y_reg_test, y_pred)
    r2 = r2_score(y_reg_test, y_pred)

    print(f"  Mean Squared Error (MSE): {mse:.4f}")
    print(f"  Root Mean Squared Error (RMSE): {rmse:.4f}")
    print(f"  Mean Absolute Error (MAE): {mae:.4f}")
    print(f"  R-squared (R2): {r2:.4f}")

    results_reg[name] = {"mse": mse, "rmse": rmse, "mae": mae, "r2": r2}

print("\nRegression Model Summary:")
for name, metrics in results_reg.items():
    print(f"- {name}: MSE={metrics['mse']:.3f}, RMSE={metrics['rmse']:.3f}, R2={metrics['r2']:.3f}")
print("\n" + "=" * 50 + "\n")


# --- 4. Cross-Validation ---

print("4. Cross-Validation:")

# Example: 5-Fold Cross-Validation for Logistic Regression
print("\n  - Logistic Regression (Classification) with 5-Fold Cross-Validation:")
lr_clf = LogisticRegression(random_state=42, max_iter=200)
# Cross-validation usually works on the full dataset or the training set.
# Using full dataset X_clf, y_clf for demonstration of CV scoring.
cv_scores_clf = cross_val_score(lr_clf, scaler_clf.fit_transform(X_clf), y_clf, cv=5, scoring='accuracy')
print(f"    Individual CV accuracies: {cv_scores_clf}")
print(f"    Mean CV accuracy: {cv_scores_clf.mean():.4f}")
print(f"    Std Dev of CV accuracy: {cv_scores_clf.std():.4f}")

# Example: 5-Fold Cross-Validation for Linear Regression
print("\n  - Linear Regression (Regression) with 5-Fold Cross-Validation:")
lin_reg = LinearRegression()
cv_scores_reg = cross_val_score(lin_reg, scaler_reg.fit_transform(X_reg), y_reg, cv=5, scoring='neg_mean_squared_error')
# cross_val_score returns negative MSE because scikit-learn metrics are usually higher = better.
# To convert to positive MSE: -cv_scores_reg
print(f"    Individual CV Negative MSEs: {cv_scores_reg}")
print(f"    Mean CV MSE: {-cv_scores_reg.mean():.4f}")
print(f"    Std Dev of CV MSE: {cv_scores_reg.std():.4f}")
print("\n" + "=" * 50 + "\n")


# --- 5. Hyperparameter Tuning ---

print("5. Hyperparameter Tuning:")

# 5.1 Grid Search (exhaustive search over a defined grid of parameters)
print("\n  - Grid Search for Decision Tree Classifier:")
param_grid_dt = {
    'max_depth': [None, 5, 10, 15],
    'min_samples_split': [2, 5, 10],
    'criterion': ['gini', 'entropy']
}
dt_gs = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid_dt, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
dt_gs.fit(X_clf_train, y_clf_train) # No scaling needed for DT

print(f"    Best parameters: {dt_gs.best_params_}")
print(f"    Best cross-validation score (accuracy): {dt_gs.best_score_:.4f}")
print(f"    Test set accuracy with best model: {accuracy_score(y_clf_test, dt_gs.best_estimator_.predict(X_clf_test)):.4f}")

# 5.2 Randomized Search (random sampling from a distribution of parameters)
print("\n  - Randomized Search for RandomForestClassifier (more efficient for large search spaces):")
from scipy.stats import randint

param_dist_rf = {
    'n_estimators': randint(50, 200),
    'max_features': randint(1, X_clf_train.shape[1]),
    'max_depth': randint(5, 20),
    'min_samples_split': randint(2, 11),
    'min_samples_leaf': randint(1, 11),
    'criterion': ['gini', 'entropy']
}

rf_rs = RandomizedSearchCV(RandomForestClassifier(random_state=42), param_distributions=param_dist_rf,
                           n_iter=10, cv=3, scoring='accuracy', random_state=42, n_jobs=-1, verbose=1)
rf_rs.fit(X_clf_train, y_clf_train)

print(f"    Best parameters: {rf_rs.best_params_}")
print(f"    Best cross-validation score (accuracy): {rf_rs.best_score_:.4f}")
print(f"    Test set accuracy with best model: {accuracy_score(y_clf_test, rf_rs.best_estimator_.predict(X_clf_test)):.4f}")
print("\n" + "=" * 50 + "\n")


# --- 6. Pipelines (Combining Preprocessing and Model) ---

print("6. Pipelines (Combining Preprocessing and Model):")

# Define preprocessing steps within the pipeline
# Here we'll handle both numerical (scaling) and potentially other (passthrough) features.
# For make_classification, all features are numerical, so we apply StandardScaler to all.
preprocessor_pipe = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), list(range(X_clf.shape[1]))) # Apply StandardScaler to all numerical features
    ],
    remainder='passthrough' # Keep any other columns if they existed
)

# Create a full pipeline with preprocessing and a Logistic Regression model
clf_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor_pipe),
    ('classifier', LogisticRegression(random_state=42, max_iter=200))
])

# Train the pipeline directly on the unscaled training data
print("  - Training a Logistic Regression pipeline (scaling + model):")
clf_pipeline.fit(X_clf_train, y_clf_train)

# Make predictions on unscaled test data (pipeline handles scaling internally)
y_pred_pipe = clf_pipeline.predict(X_clf_test)
print(f"  - Pipeline Accuracy on test set: {accuracy_score(y_clf_test, y_pred_pipe):.4f}")

print("\n  - Using the pipeline for Grid Search (hyperparameter tuning on the full workflow):")
# Now, we can tune hyperparameters for the classifier within the pipeline
# The parameter names for the grid search need to be prefixed with the step name and two underscores.
# E.g., 'classifier__C' for LogisticRegression's C parameter.
param_grid_pipeline = {
    'classifier__C': [0.1, 1.0, 10.0],
    'classifier__solver': ['liblinear', 'lbfgs']
}

grid_search_pipeline = GridSearchCV(clf_pipeline, param_grid_pipeline, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search_pipeline.fit(X_clf_train, y_clf_train)

print(f"    Best pipeline parameters: {grid_search_pipeline.best_params_}")
print(f"    Best pipeline cross-validation accuracy: {grid_search_pipeline.best_score_:.4f}")
print(f"    Pipeline test set accuracy with best model: {accuracy_score(y_clf_test, grid_search_pipeline.best_estimator_.predict(X_clf_test)):.4f}")

print("\nSupervised learning demonstration complete!")