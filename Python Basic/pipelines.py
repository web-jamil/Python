import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib # For saving/loading models

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, FeatureUnion

# Models
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score, mean_squared_error, f1_score

# --- Data Generation ---
# For Classification (mixed types for ColumnTransformer demo)
np.random.seed(42)
data_clf = pd.DataFrame({
    'numerical_feature_1': np.random.rand(100) * 100,
    'numerical_feature_2': np.random.randint(10, 100, 100),
    'categorical_feature': np.random.choice(['A', 'B', 'C', np.nan], 100, p=[0.3, 0.3, 0.3, 0.1]),
    'ordinal_feature': np.random.choice(['Low', 'Medium', 'High'], 100),
    'boolean_feature': np.random.choice([True, False], 100),
    'target': np.random.randint(0, 2, 100)
})
# Introduce some missing numerical values
data_clf.loc[np.random.choice(data_clf.index, 10), 'numerical_feature_1'] = np.nan
data_clf.loc[np.random.choice(data_clf.index, 5), 'numerical_feature_2'] = np.nan

X_clf = data_clf.drop('target', axis=1)
y_clf = data_clf['target']

# For Regression (simpler numerical dataset)
X_reg, y_reg = make_regression(n_samples=100, n_features=5, noise=10, random_state=42)
X_reg = pd.DataFrame(X_reg, columns=[f'feature_{i}' for i in range(5)])

print("--- Scikit-learn Pipelines Demo ---")
print("Libraries and data generated successfully!\n")

# Split data
X_clf_train, X_clf_test, y_clf_train, y_clf_test = train_test_split(
    X_clf, y_clf, test_size=0.3, random_state=42, stratify=y_clf
)

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42
)

print(f"Classification data split. X_clf_train shape: {X_clf_train.shape}")
print(f"Regression data split. X_reg_train shape: {X_reg_train.shape}\n")
print("=" * 50 + "\n")


# --- 1. Basic Pipeline ---

print("1. Basic Pipeline: Chaining a Transformer and an Estimator")
# Example: Scaling features then applying Logistic Regression

# Define the pipeline steps as a list of (name, transformer/estimator) tuples
basic_pipeline_clf = Pipeline([
    ('scaler', StandardScaler()), # First step: Scaling
    ('classifier', LogisticRegression(random_state=42, max_iter=200)) # Second step: Classifier
])

print("  Fitting the basic pipeline on training data (unscaled)...")
basic_pipeline_clf.fit(X_clf_train[['numerical_feature_1', 'numerical_feature_2']].fillna(X_clf_train['numerical_feature_1'].mean()), y_clf_train)
# For this basic demo, we manually handle NaNs for the two numerical features
# In real scenarios, use SimpleImputer inside a more complex pipeline or ColumnTransformer.

y_pred_basic = basic_pipeline_clf.predict(X_clf_test[['numerical_feature_1', 'numerical_feature_2']].fillna(X_clf_train['numerical_feature_1'].mean()))
accuracy_basic = accuracy_score(y_clf_test, y_pred_basic)
print(f"  Basic Pipeline Accuracy on test set: {accuracy_basic:.4f}\n")
print("=" * 50 + "\n")


# --- 2. Accessing Pipeline Steps ---

print("2. Accessing Pipeline Steps and Attributes:")

# Get individual steps
scaler_step = basic_pipeline_clf.named_steps['scaler']
classifier_step = basic_pipeline_clf.named_steps['classifier']

print(f"  Scaler type: {type(scaler_step).__name__}")
print(f"  Classifier type: {type(classifier_step).__name__}")

# Access attributes of fitted steps
print(f"  Scaler's mean (first feature): {scaler_step.mean_[0]:.4f}")
print(f"  Logistic Regression coefficients (first 5): {classifier_step.coef_[0, :5]}\n")
print("=" * 50 + "\n")


# --- 3. Pipelines with Multiple Transformers ---

print("3. Pipelines with Multiple Transformers: Imputation -> Scaling -> Model")
# This is a more realistic scenario for numerical features.

# For numerical features
numerical_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')), # Impute missing values
    ('scaler', StandardScaler())                 # Scale features
])

# Full pipeline including preprocessing for numerical features and then a model
full_pipeline_clf = Pipeline([
    ('preprocessing', numerical_pipeline), # Can embed pipelines within pipelines
    ('classifier', DecisionTreeClassifier(random_state=42))
])

print("  Fitting pipeline with imputation and scaling...")
full_pipeline_clf.fit(X_clf_train[['numerical_feature_1', 'numerical_feature_2']], y_clf_train)

y_pred_full = full_pipeline_clf.predict(X_clf_test[['numerical_feature_1', 'numerical_feature_2']])
accuracy_full = accuracy_score(y_clf_test, y_pred_full)
print(f"  Full Pipeline (Imputation->Scaling->DT) Accuracy: {accuracy_full:.4f}\n")
print("=" * 50 + "\n")


# --- 4. `ColumnTransformer`: Handling Mixed Data Types ---

print("4. `ColumnTransformer`: Applying Different Transformations to Different Columns")

# Identify column types
numerical_cols = ['numerical_feature_1', 'numerical_feature_2']
categorical_nominal_cols = ['categorical_feature']
ordinal_cols = ['ordinal_feature']
boolean_cols = ['boolean_feature'] # Can be handled by OneHotEncoder or manually mapped

# Define preprocessing for numerical features
numerical_transformer_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Define preprocessing for categorical nominal features
categorical_nominal_transformer_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), # Impute missing categories
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Define preprocessing for ordinal features (requires explicit order)
ordinal_categories = ['Low', 'Medium', 'High']
ordinal_transformer_pipe = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OneHotEncoder(handle_unknown='ignore', sparse_output=False)) # Can use OneHot if numbers are just labels
    # Or OrdinalEncoder if you want a single numerical column representing order:
    # ('ordinal', OrdinalEncoder(categories=[ordinal_categories], handle_unknown='use_encoded_value', unknown_value=-1))
])

# Combine transformers using ColumnTransformer
preprocessor_mixed = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer_pipe, numerical_cols),
        ('cat_nom', categorical_nominal_transformer_pipe, categorical_nominal_cols),
        ('ord', ordinal_transformer_pipe, ordinal_cols)
    ],
    remainder='passthrough' # Keep other columns (like boolean_feature) as they are
)

# Create the final pipeline with preprocessing and a model
mixed_data_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor_mixed),
    ('classifier', LogisticRegression(random_state=42, max_iter=500))
])

print("  Fitting ColumnTransformer pipeline (mixed data types)...")
mixed_data_pipeline.fit(X_clf_train, y_clf_train)

y_pred_mixed = mixed_data_pipeline.predict(X_clf_test)
accuracy_mixed = accuracy_score(y_clf_test, y_pred_mixed)
print(f"  Mixed Data Pipeline Accuracy: {accuracy_mixed:.4f}\n")

# You can get transformed column names, but it can be complex for OneHotEncoder
# transformed_columns = mixed_data_pipeline.named_steps['preprocessor'].get_feature_names_out()
# print(f"  Transformed feature names (partial view): {transformed_columns[:5]}...\n")
print("=" * 50 + "\n")


# --- 5. Pipelines with Hyperparameter Tuning (`GridSearchCV`) ---

print("5. Pipelines with Hyperparameter Tuning (`GridSearchCV`):")
# Tuning parameters of steps within a pipeline.
# Parameters are accessed using 'step_name__parameter_name'.

# Re-use the mixed_data_pipeline
param_grid_pipe_tuned = {
    'preprocessor__num__imputer__strategy': ['mean', 'median'],
    'preprocessor__cat_nom__imputer__strategy': ['most_frequent', 'constant'],
    'preprocessor__cat_nom__imputer__fill_value': [None, 'missing'], # Only applies if strategy is 'constant'
    'classifier__C': [0.1, 1.0, 10.0],
    'classifier__solver': ['liblinear', 'lbfgs']
}

# Create GridSearchCV
grid_search_pipe = GridSearchCV(
    estimator=mixed_data_pipeline,
    param_grid=param_grid_pipe_tuned,
    cv=3, # Smaller CV for demo speed
    scoring='f1',
    n_jobs=-1,
    verbose=1
)

print("  Starting Grid Search for the pipeline...")
# Fit Grid Search on the original (unscaled, un-imputed, un-encoded) training data.
# The pipeline handles all preprocessing steps inside each CV fold.
grid_search_pipe.fit(X_clf_train, y_clf_train)

print("\n  Grid Search Pipeline Results:")
print(f"    Best parameters: {grid_search_pipe.best_params_}")
print(f"    Best cross-validation F1 score: {grid_search_pipe.best_score_:.4f}")

best_pipeline_tuned = grid_search_pipe.best_estimator_
y_pred_tuned = best_pipeline_tuned.predict(X_clf_test)
test_f1_tuned = f1_score(y_clf_test, y_pred_tuned)
print(f"    Test set F1 score with best pipeline: {test_f1_tuned:.4f}\n")
print("=" * 50 + "\n")


# --- 6. Feature Union (Brief Mention) ---

print("6. Feature Union (combining different feature sets):")
# Combines the results of multiple transformer objects.
# Less common than ColumnTransformer for typical preprocessing but useful for specific feature engineering.

# Example: One transformer extracts numerical features and scales them, another uses specific categorical.
numerical_pipeline_fu = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_pipeline_fu = Pipeline([
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Create a FeatureUnion to combine the output of these pipelines
# Note: FeatureUnion concatenates the outputs. ColumnTransformer stacks them.
feature_union = FeatureUnion([
    ('numeric_features', numerical_pipeline_fu),
    ('categorical_features', categorical_pipeline_fu)
])

# A full pipeline using FeatureUnion (using only relevant columns for simplicity here)
# This example is simplified as FeatureUnion takes the *entire* X and each transformer selects its own columns
# which is less common in modern scikit-learn compared to ColumnTransformer.
# For a more robust demo, ColumnTransformer is preferred for selecting specific columns.

# Here, for demonstration, let's process X_clf using FeatureUnion if we apply it to specific columns manually:
# X_numerical_transformed = numerical_pipeline_fu.fit_transform(X_clf_train[numerical_cols])
# X_categorical_transformed = categorical_pipeline_fu.fit_transform(X_clf_train[categorical_nominal_cols])
# X_combined = np.hstack((X_numerical_transformed, X_categorical_transformed))
# print(f"  Shape after manual FeatureUnion-like combination: {X_combined.shape}")

# In a pipeline, FeatureUnion processes the input X directly.
# Let's create a dummy FeatureUnion pipeline for demonstration of its structure:
fu_pipe = Pipeline([
    ('features', FeatureUnion([
        ('num_scaler', StandardScaler()),
        ('pass_through_original_first_feature', FunctionTransformer(lambda x: x[:, 0].reshape(-1,1), validate=False)) # Just for demo
    ])),
    ('classifier', LogisticRegression(random_state=42, max_iter=200))
])
# This is an abstract example of its structure, not a practical use with mixed types as is.
# ColumnTransformer is generally more powerful for mixed data types.
print("  FeatureUnion conceptually combines outputs of transformers.")
print("  Often superseded by `ColumnTransformer` for feature selection based on column names.\n")
print("=" * 50 + "\n")


# --- 7. Saving and Loading Pipelines ---

print("7. Saving and Loading Pipelines (for deployment):")

# Re-train a simple pipeline for saving
final_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(random_state=42, max_iter=200))
])

final_pipeline.fit(X_clf_train[['numerical_feature_1', 'numerical_feature_2']], y_clf_train)

# Save the trained pipeline
filename = 'final_pipeline.joblib'
joblib.dump(final_pipeline, filename)
print(f"  Pipeline saved to '{filename}'.")

# Load the pipeline
loaded_pipeline = joblib.load(filename)
print(f"  Pipeline loaded from '{filename}'.")

# Make predictions with the loaded pipeline
y_pred_loaded = loaded_pipeline.predict(X_clf_test[['numerical_feature_1', 'numerical_feature_2']])
accuracy_loaded = accuracy_score(y_clf_test, y_pred_loaded)
print(f"  Accuracy with loaded pipeline: {accuracy_loaded:.4f}")

# Verify it's the same as original
y_pred_original = final_pipeline.predict(X_clf_test[['numerical_feature_1', 'numerical_feature_2']])
print(f"  Accuracy matches original pipeline: {accuracy_loaded == accuracy_score(y_clf_test, y_pred_original)}")
print("\n" + "=" * 50 + "\n")

print("Pipelines demonstration complete!")