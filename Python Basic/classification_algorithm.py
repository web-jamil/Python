import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification, make_blobs

# --- Classification Algorithms ---
# Linear Models
from sklearn.linear_model import LogisticRegression, Perceptron
from sklearn.svm import LinearSVC # Linear Support Vector Classifier

# Tree-based Models
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Instance-based
from sklearn.neighbors import KNeighborsClassifier

# Support Vector Machines
from sklearn.svm import SVC # Support Vector Classifier (handles non-linear with kernels)

# Naive Bayes
from sklearn.naive_bayes import GaussianNB # Gaussian Naive Bayes

# Neural Networks (simple)
from sklearn.neural_network import MLPClassifier

# --- Metrics ---
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc, classification_report
)

print("--- Scikit-learn Classification Algorithms Demo ---")
print("Libraries imported successfully!\n")

# --- 1. Data Generation ---

print("1. Data Generation:")

# 1.1 Binary Classification Dataset
X_binary, y_binary = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    n_classes=2,
    weights=[0.9, 0.1], # Imbalanced classes
    flip_y=0.01,
    random_state=42
)
print(f"Binary Classification dataset generated. X_binary shape: {X_binary.shape}, y_binary shape: {y_binary.shape}")
print(f"Binary Class distribution: {np.bincount(y_binary)}")
print("-" * 30)

# 1.2 Multi-Class Classification Dataset
X_multi, y_multi = make_blobs(
    n_samples=1000,
    n_features=5,
    centers=3, # 3 classes
    cluster_std=1.5,
    random_state=42
)
print(f"Multi-Class Classification dataset generated. X_multi shape: {X_multi.shape}, y_multi shape: {y_multi.shape}")
print(f"Multi-Class distribution: {np.bincount(y_multi)}\n")
print("=" * 50 + "\n")

# --- 2. Preprocessing & Data Splitting ---

print("2. Preprocessing & Data Splitting:")

# For binary classification
X_bin_train, X_bin_test, y_bin_train, y_bin_test = train_test_split(
    X_binary, y_binary, test_size=0.3, random_state=42, stratify=y_binary
)

# For multi-class classification
X_multi_train, X_multi_test, y_multi_train, y_multi_test = train_test_split(
    X_multi, y_multi, test_size=0.3, random_state=42, stratify=y_multi
)

# Feature Scaling (StandardScaler) for numerical features
# We'll use a pipeline for this in the demo for better practice.
# For individual model demos, we'll manually scale the data.
scaler = StandardScaler()
X_bin_train_scaled = scaler.fit_transform(X_bin_train)
X_bin_test_scaled = scaler.transform(X_bin_test)

X_multi_train_scaled = scaler.fit_transform(X_multi_train)
X_multi_test_scaled = scaler.transform(X_multi_test)

print("Data split into training and testing sets and scaled.\n")
print("=" * 50 + "\n")

# --- 3. Core Classification Algorithms, Training, Prediction, and Evaluation ---

print("3. Core Classification Algorithms, Training, Prediction, and Evaluation:\n")

# Define a dictionary of classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=200),
    "K-Nearest Neighbors (KNN)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree Classifier": DecisionTreeClassifier(random_state=42),
    "Support Vector Classifier (Linear)": LinearSVC(random_state=42, dual=False, max_iter=10000), # dual=False for n_samples > n_features
    "Support Vector Classifier (RBF Kernel)": SVC(kernel='rbf', probability=True, random_state=42),
    "Gaussian Naive Bayes": GaussianNB(),
    "Random Forest Classifier": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "MLP Classifier (Neural Network)": MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
}

# --- Binary Classification Demo ---
print("--- Binary Classification Algorithms ---")
results_binary = {}

for name, model in classifiers.items():
    print(f"\n--- Model: {name} (Binary Classification) ---")

    # Determine if scaling is beneficial/required for the model
    # Most models perform better with scaled data, especially distance-based or regularization-based ones.
    if name in ["Logistic Regression", "K-Nearest Neighbors (KNN)",
                "Support Vector Classifier (Linear)", "Support Vector Classifier (RBF Kernel)",
                "MLP Classifier (Neural Network)"]:
        X_train_current = X_bin_train_scaled
        X_test_current = X_bin_test_scaled
    else: # Tree-based models and Naive Bayes are generally less sensitive to scaling
        X_train_current = X_bin_train
        X_test_current = X_bin_test

    try:
        model.fit(X_train_current, y_bin_train)
        y_pred = model.predict(X_test_current)

        # Common Metrics
        accuracy = accuracy_score(y_bin_test, y_pred)
        precision = precision_score(y_bin_test, y_pred)
        recall = recall_score(y_bin_test, y_pred)
        f1 = f1_score(y_bin_test, y_pred)
        cm = confusion_matrix(y_bin_test, y_pred)

        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Precision: {precision:.4f}")
        print(f"  Recall: {recall:.4f}")
        print(f"  F1-Score: {f1:.4f}")
        print(f"  Confusion Matrix:\n{cm}")

        # Classification Report
        print("\n  Classification Report:")
        print(classification_report(y_bin_test, y_pred))

        # ROC-AUC (for binary classification, requires predict_proba or decision_function)
        if hasattr(model, "predict_proba"):
            y_pred_proba = model.predict_proba(X_test_current)[:, 1]
            fpr, tpr, _ = roc_curve(y_bin_test, y_pred_proba)
            roc_auc = auc(fpr, tpr)
            print(f"  ROC-AUC: {roc_auc:.4f}")

            # Plot ROC curve for Logistic Regression as an example
            if name == "Logistic Regression":
                plt.figure(figsize=(6, 5))
                plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (area = {roc_auc:.2f})')
                plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
                plt.xlim([0.0, 1.0])
                plt.ylim([0.0, 1.05])
                plt.xlabel('False Positive Rate')
                plt.ylabel('True Positive Rate')
                plt.title('ROC Curve for Logistic Regression (Binary)')
                plt.legend(loc="lower right")
                plt.show()
        elif hasattr(model, "decision_function"): # For LinearSVC
            y_score = model.decision_function(X_test_current)
            fpr, tpr, _ = roc_curve(y_bin_test, y_score)
            roc_auc = auc(fpr, tpr)
            print(f"  ROC-AUC (from decision_function): {roc_auc:.4f}")
        else:
            print("  ROC-AUC not available for this model (no predict_proba or decision_function).")

        results_binary[name] = {
            "accuracy": accuracy, "precision": precision,
            "recall": recall, "f1_score": f1,
            "roc_auc": roc_auc if (hasattr(model, "predict_proba") or hasattr(model, "decision_function")) else None
        }

    except Exception as e:
        print(f"  Error training/evaluating {name}: {e}")
        results_binary[name] = {"accuracy": "Error", "f1_score": "Error", "roc_auc": "Error"}


print("\nBinary Classification Model Summary:")
for name, metrics in results_binary.items():
    print(f"- {name}: Acc={metrics['accuracy']:.3f}, F1={metrics['f1_score']:.3f}, ROC-AUC={metrics['roc_auc']:.3f if metrics['roc_auc'] is not None else 'N/A'}")
print("\n" + "=" * 50 + "\n")


# --- Multi-Class Classification Demo ---
print("--- Multi-Class Classification Algorithms ---")
results_multi = {}

# Re-initializing some models that might have been trained on binary data
classifiers_multi = {
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=200),
    "K-Nearest Neighbors (KNN)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree Classifier": DecisionTreeClassifier(random_state=42),
    "Support Vector Classifier (RBF Kernel)": SVC(kernel='rbf', probability=True, random_state=42),
    "Gaussian Naive Bayes": GaussianNB(),
    "Random Forest Classifier": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting Classifier": GradientBoostingClassifier(n_estimators=100, random_state=42),
    "MLP Classifier (Neural Network)": MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)
}

# LinearSVC supports multi-class but usually One-vs-Rest, so its direct usage for multi-class ROC is more complex.
# We omit Perceptron and LinearSVC for simple multi-class ROC-AUC for brevity here, sticking to models with predict_proba.

for name, model in classifiers_multi.items():
    print(f"\n--- Model: {name} (Multi-Class Classification) ---")

    if name in ["Logistic Regression", "K-Nearest Neighbors (KNN)",
                "Support Vector Classifier (RBF Kernel)",
                "MLP Classifier (Neural Network)"]:
        X_train_current = X_multi_train_scaled
        X_test_current = X_multi_test_scaled
    else:
        X_train_current = X_multi_train
        X_test_current = X_multi_test

    try:
        model.fit(X_train_current, y_multi_train)
        y_pred = model.predict(X_test_current)

        accuracy = accuracy_score(y_multi_test, y_pred)
        # For multi-class, precision, recall, f1 need 'average' parameter
        precision_macro = precision_score(y_multi_test, y_pred, average='macro')
        recall_macro = recall_score(y_multi_test, y_pred, average='macro')
        f1_macro = f1_score(y_multi_test, y_pred, average='macro')
        cm = confusion_matrix(y_multi_test, y_pred)

        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Precision (macro): {precision_macro:.4f}")
        print(f"  Recall (macro): {recall_macro:.4f}")
        print(f"  F1-Score (macro): {f1_macro:.4f}")
        print(f"  Confusion Matrix:\n{cm}")

        print("\n  Classification Report:")
        print(classification_report(y_multi_test, y_pred))

        # ROC-AUC for multi-class is more complex (e.g., One-vs-Rest strategy).
        # We'll skip plotting for brevity but mention the concept.
        if hasattr(model, "predict_proba"):
            print("  Model supports predict_proba. Multi-class ROC-AUC can be computed (e.g., One-vs-Rest).")
        else:
            print("  ROC-AUC not directly available for this model (no predict_proba).")

        results_multi[name] = {
            "accuracy": accuracy, "precision_macro": precision_macro,
            "recall_macro": recall_macro, "f1_macro": f1_macro
        }

    except Exception as e:
        print(f"  Error training/evaluating {name}: {e}")
        results_multi[name] = {"accuracy": "Error", "f1_macro": "Error"}


print("\nMulti-Class Classification Model Summary:")
for name, metrics in results_multi.items():
    print(f"- {name}: Acc={metrics['accuracy']:.3f}, F1(macro)={metrics['f1_macro']:.3f}")
print("\n" + "=" * 50 + "\n")


# --- 4. Cross-Validation ---

print("4. Cross-Validation:")

print("  - 5-Fold Cross-Validation for RandomForestClassifier (Binary):")
rf_cv = RandomForestClassifier(n_estimators=100, random_state=42)
# Use unscaled data for tree-based models
cv_scores = cross_val_score(rf_cv, X_binary, y_binary, cv=5, scoring='accuracy', n_jobs=-1)
print(f"    Individual CV accuracies: {cv_scores}")
print(f"    Mean CV accuracy: {cv_scores.mean():.4f}")
print(f"    Standard Deviation of CV accuracy: {cv_scores.std():.4f}")

print("\n  - 5-Fold Cross-Validation for Logistic Regression (Multi-Class) with Scaling:")
lr_multi_cv = LogisticRegression(random_state=42, max_iter=200)
# Use scaled data for Logistic Regression
cv_scores_scaled = cross_val_score(lr_multi_cv, scaler.fit_transform(X_multi), y_multi, cv=5, scoring='accuracy', n_jobs=-1)
print(f"    Individual CV accuracies (scaled): {cv_scores_scaled}")
print(f"    Mean CV accuracy (scaled): {cv_scores_scaled.mean():.4f}")
print(f"    Standard Deviation of CV accuracy (scaled): {cv_scores_scaled.std():.4f}")
print("\n" + "=" * 50 + "\n")


# --- 5. Hyperparameter Tuning (Grid Search) ---

print("5. Hyperparameter Tuning (Grid Search):")

print("\n  - Grid Search for K-Nearest Neighbors (KNN) Classifier (Binary):")
knn = KNeighborsClassifier()
param_grid_knn = {
    'n_neighbors': [3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'p': [1, 2] # 1 for Manhattan distance, 2 for Euclidean distance
}

grid_search_knn = GridSearchCV(knn, param_grid_knn, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
# Fit Grid Search on scaled training data
grid_search_knn.fit(X_bin_train_scaled, y_bin_train)

print(f"    Best parameters found: {grid_search_knn.best_params_}")
print(f"    Best cross-validation score (accuracy): {grid_search_knn.best_score_:.4f}")
print(f"    Test set accuracy with best model: {accuracy_score(y_bin_test, grid_search_knn.best_estimator_.predict(X_bin_test_scaled)):.4f}")
print("\n" + "=" * 50 + "\n")


# --- 6. Pipelines (Combining Preprocessing and Model) ---

print("6. Pipelines (Combining Preprocessing and Model):")

# Define preprocessing for numerical features
numerical_transformer = StandardScaler()

# Create a ColumnTransformer to apply preprocessing
# For these synthetic datasets, all features are numerical.
preprocessor_full = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, list(range(X_binary.shape[1])))
    ],
    remainder='passthrough'
)

# Example: Pipeline for Logistic Regression (Binary Classification)
print("\n  - Building a Pipeline for Logistic Regression (Scaling + Model):")
pipeline_lr = Pipeline(steps=[
    ('preprocessor', preprocessor_full),
    ('classifier', LogisticRegression(random_state=42, max_iter=200))
])

print("    Fitting pipeline on unscaled training data (pipeline handles scaling):")
pipeline_lr.fit(X_bin_train, y_bin_train) # Pass unscaled data
y_pred_pipe_lr = pipeline_lr.predict(X_bin_test) # Predict on unscaled test data
print(f"    Pipeline Logistic Regression accuracy: {accuracy_score(y_bin_test, y_pred_pipe_lr):.4f}")

# Example: Using the Pipeline with GridSearchCV
print("\n  - Hyperparameter tuning a RandomForestClassifier within a Pipeline:")

pipeline_rf = Pipeline(steps=[
    ('preprocessor', preprocessor_full), # Scaling is often good for RF too, though not strictly required
    ('classifier', RandomForestClassifier(random_state=42))
])

param_grid_pipe_rf = {
    'classifier__n_estimators': [50, 100, 150],
    'classifier__max_depth': [None, 10, 20]
}

grid_search_pipe_rf = GridSearchCV(pipeline_rf, param_grid_pipe_rf, cv=3, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search_pipe_rf.fit(X_bin_train, y_bin_train) # Fit on unscaled data

print(f"    Best pipeline RF parameters: {grid_search_pipe_rf.best_params_}")
print(f"    Best pipeline RF cross-validation accuracy: {grid_search_pipe_rf.best_score_:.4f}")
print(f"    Pipeline RF test set accuracy: {accuracy_score(y_bin_test, grid_search_pipe_rf.best_estimator_.predict(X_bin_test)):.4f}")

print("\nClassification algorithms demonstration complete!")