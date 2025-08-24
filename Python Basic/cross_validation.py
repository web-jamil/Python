import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    cross_validate,
    KFold,
    StratifiedKFold,
    LeaveOneOut,
    ShuffleSplit,
    StratifiedShuffleSplit,
    RepeatedKFold,
    RepeatedStratifiedKFold,
    TimeSeriesSplit
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.datasets import make_classification, make_regression

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    mean_squared_error, r2_score, make_scorer
)

print("--- Scikit-learn Cross-Validation Demo ---")
print("Libraries imported successfully!\n")

# --- 1. Data Generation ---

print("1. Data Generation:")

# For Classification Demos
X_clf, y_clf = make_classification(
    n_samples=1000,
    n_features=10,
    n_informative=5,
    n_redundant=2,
    n_classes=2,
    weights=[0.8, 0.2], # Imbalanced classes for StratifiedKFold demo
    random_state=42
)
print(f"Classification dataset generated. X_clf shape: {X_clf.shape}, y_clf shape: {y_clf.shape}")
print(f"Binary Class distribution: {np.bincount(y_clf)}")
print("-" * 30)

# For Regression Demos
X_reg, y_reg = make_regression(
    n_samples=1000,
    n_features=5,
    noise=15,
    random_state=42
)
print(f"Regression dataset generated. X_reg shape: {X_reg.shape}, y_reg shape: {y_reg.shape}\n")
print("=" * 50 + "\n")


# --- 2. Basic cross_val_score (K-Fold) ---

print("2. Basic `cross_val_score` (K-Fold Classification):")
model_clf = LogisticRegression(max_iter=200, random_state=42)

# Default is StratifiedKFold for classification for versions >= 0.22
# For regression, it's KFold by default
scores_clf = cross_val_score(model_clf, X_clf, y_clf, cv=5, scoring='accuracy')
print(f"  Accuracy scores (5-fold CV): {scores_clf}")
print(f"  Mean Accuracy: {scores_clf.mean():.4f}")
print(f"  Standard Deviation: {scores_clf.std():.4f}\n")

print("  Basic `cross_val_score` (K-Fold Regression):")
model_reg = LinearRegression()
scores_reg = cross_val_score(model_reg, X_reg, y_reg, cv=5, scoring='neg_mean_squared_error')
# Scores are negative MSE, so convert to positive
mse_scores_reg = -scores_reg
print(f"  MSE scores (5-fold CV): {mse_scores_reg}")
print(f"  Mean MSE: {mse_scores_reg.mean():.4f}")
print(f"  Standard Deviation: {mse_scores_reg.std():.4f}\n")
print("=" * 50 + "\n")


# --- 3. `KFold` (Manual K-Fold) ---

print("3. `KFold` (Manual K-Fold for Regression):")
# KFold does not care about class distribution, suitable for regression or when stratification is not needed.
kf = KFold(n_splits=5, shuffle=True, random_state=42)
dt_reg_model = DecisionTreeRegressor(random_state=42)
fold_mses = []

for fold, (train_index, test_index) in enumerate(kf.split(X_reg, y_reg)):
    X_train, X_test = X_reg[train_index], X_reg[test_index]
    y_train, y_test = y_reg[train_index], y_reg[test_index]

    dt_reg_model.fit(X_train, y_train)
    y_pred = dt_reg_model.predict(X_test)
    fold_mse = mean_squared_error(y_test, y_pred)
    fold_mses.append(fold_mse)
    print(f"  Fold {fold+1} MSE: {fold_mse:.4f}")

print(f"  Manual KFold Mean MSE: {np.mean(fold_mses):.4f}")
print(f"  Manual KFold Std Dev MSE: {np.std(fold_mses):.4f}\n")
print("=" * 50 + "\n")


# --- 4. `StratifiedKFold` (for Classification) ---

print("4. `StratifiedKFold` (for Classification):")
# Ensures that each fold has approximately the same percentage of samples of each target class as the complete set.
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
dt_clf_model = DecisionTreeClassifier(random_state=42)
fold_accuracies = []

print("  Class distribution per fold:")
for fold, (train_index, test_index) in enumerate(skf.split(X_clf, y_clf)):
    X_train, X_test = X_clf[train_index], X_clf[test_index]
    y_train, y_test = y_clf[train_index], y_clf[test_index]

    print(f"    Fold {fold+1}: y_train counts: {np.bincount(y_train)}, y_test counts: {np.bincount(y_test)}")
    dt_clf_model.fit(X_train, y_train)
    y_pred = dt_clf_model.predict(X_test)
    fold_acc = accuracy_score(y_test, y_pred)
    fold_accuracies.append(fold_acc)
    print(f"    Fold {fold+1} Accuracy: {fold_acc:.4f}")

print(f"  StratifiedKFold Mean Accuracy: {np.mean(fold_accuracies):.4f}")
print(f"  StratifiedKFold Std Dev Accuracy: {np.std(fold_accuracies):.4f}\n")
print("=" * 50 + "\n")


# --- 5. `LeaveOneOut` (LOO) ---

print("5. `LeaveOneOut` (LOO - for small datasets):")
# Each sample is used once as a test set while the remaining samples form the training set.
# Very computationally expensive for large datasets.
loo = LeaveOneOut()
lr_loo = LogisticRegression(max_iter=200, random_state=42)

# Using a very small subset for demonstration
X_clf_small = X_clf[:50]
y_clf_small = y_clf[:50]

loo_scores = []
for train_index, test_index in loo.split(X_clf_small):
    X_train, X_test = X_clf_small[train_index], X_clf_small[test_index]
    y_train, y_test = y_clf_small[train_index], y_clf_small[test_index]

    lr_loo.fit(X_train, y_train)
    y_pred = lr_loo.predict(X_test)
    loo_scores.append(accuracy_score(y_test, y_pred))

print(f"  LOO Mean Accuracy (on 50 samples): {np.mean(loo_scores):.4f}")
print(f"  LOO Std Dev Accuracy (on 50 samples): {np.std(loo_scores):.4f}\n")
print("=" * 50 + "\n")


# --- 6. `ShuffleSplit` ---

print("6. `ShuffleSplit` (Random sampling without replacement):")
# Generates a user-defined number of independent train/test dataset splits.
# Each split samples a fraction of the data for training and testing.
ss = ShuffleSplit(n_splits=10, test_size=0.3, random_state=42)
lr_ss = LogisticRegression(max_iter=200, random_state=42)

ss_scores = cross_val_score(lr_ss, X_clf, y_clf, cv=ss, scoring='accuracy', n_jobs=-1)
print(f"  ShuffleSplit Accuracy Scores (10 splits): {ss_scores}")
print(f"  ShuffleSplit Mean Accuracy: {ss_scores.mean():.4f}")
print(f"  ShuffleSplit Std Dev: {ss_scores.std():.4f}\n")
print("=" * 50 + "\n")


# --- 7. `StratifiedShuffleSplit` ---

print("7. `StratifiedShuffleSplit` (Stratified Random sampling):")
# Similar to ShuffleSplit but preserves the percentage of samples for each class.
sss = StratifiedShuffleSplit(n_splits=10, test_size=0.3, random_state=42)
dt_sss = DecisionTreeClassifier(random_state=42)

sss_scores = cross_val_score(dt_sss, X_clf, y_clf, cv=sss, scoring='accuracy', n_jobs=-1)
print(f"  StratifiedShuffleSplit Accuracy Scores (10 splits): {sss_scores}")
print(f"  StratifiedShuffleSplit Mean Accuracy: {sss_scores.mean():.4f}")
print(f"  StratifiedShuffleSplit Std Dev: {sss_scores.std():.4f}\n")
print("=" * 50 + "\n")


# --- 8. `RepeatedKFold` / `RepeatedStratifiedKFold` ---

print("8. `RepeatedKFold` / `RepeatedStratifiedKFold`:")
# Repeats K-Fold or Stratified K-Fold n times. Useful for getting more robust estimates.

print("  - `RepeatedKFold` (Regression):")
rkf = RepeatedKFold(n_splits=5, n_repeats=3, random_state=42) # 3 repetitions of 5 folds = 15 total splits
dt_reg_rkf = DecisionTreeRegressor(random_state=42)
rkf_scores_mse = -cross_val_score(dt_reg_rkf, X_reg, y_reg, cv=rkf, scoring='neg_mean_squared_error', n_jobs=-1)
print(f"    RepeatedKFold Mean MSE: {rkf_scores_mse.mean():.4f}")
print(f"    RepeatedKFold Std Dev MSE: {rkf_scores_mse.std():.4f}\n")


print("  - `RepeatedStratifiedKFold` (Classification):")
rskf = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=42) # 3 repetitions of 5 stratified folds
lr_rskf = LogisticRegression(max_iter=200, random_state=42)
rskf_scores_acc = cross_val_score(lr_rskf, StandardScaler().fit_transform(X_clf), y_clf, cv=rskf, scoring='accuracy', n_jobs=-1)
print(f"    RepeatedStratifiedKFold Mean Accuracy: {rskf_scores_acc.mean():.4f}")
print(f"    RepeatedStratifiedKFold Std Dev Accuracy: {rskf_scores_acc.std():.4f}\n")
print("=" * 50 + "\n")


# --- 9. Time Series Cross-Validation (`TimeSeriesSplit`) ---

print("9. Time Series Cross-Validation (`TimeSeriesSplit`):")
# Ensures that training sets always precede test sets in time.
# No shuffling.
# Create dummy time-series like data
n_samples_ts = 300
X_ts = np.arange(n_samples_ts).reshape(-1, 1) # Feature is just time index
y_ts = np.sin(X_ts / 10) + np.random.randn(n_samples_ts, 1) * 0.1 # Simple sine wave with noise

tscv = TimeSeriesSplit(n_splits=5)
dt_reg_ts = DecisionTreeRegressor(random_state=42)
ts_mses = []

print("  Time Series Splits (Indices):")
for fold, (train_index, test_index) in enumerate(tscv.split(X_ts)):
    X_train, X_test = X_ts[train_index], X_ts[test_index]
    y_train, y_test = y_ts[train_index], y_ts[test_index]

    dt_reg_ts.fit(X_train, y_train)
    y_pred = dt_reg_ts.predict(X_test)
    fold_mse = mean_squared_error(y_test, y_pred)
    ts_mses.append(fold_mse)

    print(f"    Fold {fold+1}: Train size={len(train_index)}, Test size={len(test_index)}")
    print(f"      Train indices range: {train_index.min()} to {train_index.max()}")
    print(f"      Test indices range: {test_index.min()} to {test_index.max()}")
    print(f"      MSE: {fold_mse:.4f}")

print(f"  TimeSeriesSplit Mean MSE: {np.mean(ts_mses):.4f}")
print(f"  TimeSeriesSplit Std Dev MSE: {np.std(ts_mses):.4f}\n")
print("=" * 50 + "\n")


# --- 10. Cross-Validation with Pipelines ---

print("10. Cross-Validation with Pipelines:")
# Recommended approach to prevent data leakage during preprocessing.

# Define a pipeline for classification: Scaling + Logistic Regression
pipeline_clf = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(max_iter=200, random_state=42))
])

# Perform cross-validation on the pipeline
pipeline_clf_scores = cross_val_score(pipeline_clf, X_clf, y_clf, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), scoring='accuracy', n_jobs=-1)
print(f"  Pipeline (Scaled LR) Mean Accuracy: {pipeline_clf_scores.mean():.4f}")
print(f"  Pipeline (Scaled LR) Std Dev: {pipeline_clf_scores.std():.4f}\n")

# Define a pipeline for regression: Scaling + Linear Regression
pipeline_reg = Pipeline([
    ('scaler', StandardScaler()),
    ('linreg', LinearRegression())
])
pipeline_reg_scores = -cross_val_score(pipeline_reg, X_reg, y_reg, cv=KFold(n_splits=5, shuffle=True, random_state=42), scoring='neg_mean_squared_error', n_jobs=-1)
print(f"  Pipeline (Scaled LR) Mean MSE: {pipeline_reg_scores.mean():.4f}")
print(f"  Pipeline (Scaled LR) Std Dev: {pipeline_reg_scores.std():.4f}\n")
print("=" * 50 + "\n")


# --- 11. Custom Scorers and `cross_validate` ---

print("11. Custom Scorers and `cross_validate`:")

# 11.1 Custom Scorer Example (F1-macro for classification)
# Scikit-learn's 'f1_macro' is already built-in, but this shows how to create one.
f1_macro_scorer = make_scorer(f1_score, average='macro')

print("  - Using Custom Scorer (F1-macro) with `cross_val_score`:")
lr_clf_f1 = LogisticRegression(max_iter=200, random_state=42)
f1_scores_clf = cross_val_score(lr_clf_f1, StandardScaler().fit_transform(X_clf), y_clf, cv=5, scoring=f1_macro_scorer, n_jobs=-1)
print(f"    Mean F1-macro: {f1_scores_clf.mean():.4f}")
print(f"    Std Dev F1-macro: {f1_scores_clf.std():.4f}\n")


# 11.2 `cross_validate` for multiple metrics and more details
print("  - Using `cross_validate` for multiple metrics and fitting times:")
scoring = {
    'accuracy': 'accuracy',
    'precision': 'precision',
    'recall': 'recall',
    'f1_macro': 'f1_macro',
    'roc_auc': 'roc_auc' # For binary classification with predict_proba
}

results_clf_detailed = cross_validate(
    LogisticRegression(max_iter=200, random_state=42),
    StandardScaler().fit_transform(X_clf),
    y_clf,
    cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42),
    scoring=scoring,
    return_train_score=True, # Also returns scores on training set
    return_estimator=True,   # Returns fitted estimators for each fold
    n_jobs=-1
)

print("    `cross_validate` Results:")
for metric_name, scores_array in results_clf_detailed.items():
    if 'test' in metric_name or 'train' in metric_name:
        print(f"      {metric_name}: Mean {np.mean(scores_array):.4f}, Std {np.std(scores_array):.4f}")
    elif 'time' in metric_name:
        print(f"      {metric_name}: Mean {np.mean(scores_array):.4f}s")
print("\n" + "=" * 50 + "\n")

print("Cross-validation demonstration complete!")