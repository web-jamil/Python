import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    RobustScaler,
    OneHotEncoder,
    LabelEncoder,
    OrdinalEncoder
)
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Data Loading and Preprocessing Practice ---")
print("Libraries imported successfully!\n")

# --- 1. Loading Data ---

print("1. Data Loading Examples:")

# 1.1 From CSV
try:
    # Create a dummy CSV file for demonstration
    csv_data = {
        'ID': [1, 2, 3, 4, 5],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, np.nan, 35, 40],
        'City': ['New York', 'London', 'Paris', 'New York', 'London'],
        'Salary': [50000, 60000, 75000, np.nan, 80000],
        'IsStudent': [True, False, False, True, False]
    }
    df_csv = pd.DataFrame(csv_data)
    df_csv.to_csv('sample_data.csv', index=False)
    df = pd.read_csv('sample_data.csv')
    print("  - Loaded data from 'sample_data.csv':")
    print(df.head())
    print("-" * 30)
except Exception as e:
    print(f"  - Error loading CSV: {e}. Skipping CSV loading example.")

# 1.2 Creating a Synthetic DataFrame (most common for practice)
print("  - Creating a synthetic DataFrame for further processing:")
np.random.seed(42)
data = {
    'Numerical_Feature_1': np.random.rand(10) * 100,
    'Numerical_Feature_2': np.random.randint(1, 50, 10),
    'Categorical_Feature_1': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Categorical_Feature_2': ['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z', 'X'],
    'Ordinal_Feature': ['Low', 'Medium', 'High', 'Medium', 'Low', 'High', 'Medium', 'Low', 'High', 'Medium'],
    'Boolean_Feature': [True, False, True, False, True, False, True, False, True, False],
    'Target': np.random.randint(0, 2, 10) # For classification
}
# Introduce some missing values and duplicates for demonstration
data['Numerical_Feature_1'][2] = np.nan
data['Numerical_Feature_2'][5] = np.nan
data['Categorical_Feature_1'][8] = np.nan
data['Numerical_Feature_1'][9] = data['Numerical_Feature_1'][0] # Duplicate for testing
data['Categorical_Feature_1'][9] = data['Categorical_Feature_1'][0]
data['Numerical_Feature_2'][9] = data['Numerical_Feature_2'][0]


df = pd.DataFrame(data)
print(df)
print("\n" + "=" * 50 + "\n")

# --- 2. Basic Data Inspection ---

print("2. Basic Data Inspection:")
print("  - df.head():")
print(df.head())
print("\n  - df.info():")
df.info()
print("\n  - df.describe() (numerical features):")
print(df.describe())
print(f"\n  - df.shape: {df.shape}")
print(f"  - df.dtypes:\n{df.dtypes}")

print("\n  - Checking for missing values (df.isnull().sum()):")
print(df.isnull().sum())
print("\n  - Checking for duplicate rows (df.duplicated().sum()):")
print(df.duplicated().sum())
print("\n" + "=" * 50 + "\n")

# --- 3. Handling Missing Values ---

print("3. Handling Missing Values:")

# Create a copy to demonstrate different strategies
df_missing_demo = df.copy()

print("  - Original DataFrame with NaNs:")
print(df_missing_demo[['Numerical_Feature_1', 'Numerical_Feature_2', 'Categorical_Feature_1']])
print("  - Missing values before handling:\n", df_missing_demo.isnull().sum())

# 3.1 Dropping Missing Values
df_dropped_rows = df_missing_demo.dropna()
print(f"\n  - After dropping rows with any NaN: Shape {df_dropped_rows.shape}")

df_dropped_cols = df_missing_demo.dropna(axis=1)
print(f"  - After dropping columns with any NaN: Shape {df_dropped_cols.shape}")

# 3.2 Imputation
print("\n  - Imputation Examples:")

# Numerical Imputation (Mean, Median, Constant)
# Mean Imputation
df_mean_imputed = df_missing_demo.copy()
mean_val_num1 = df_mean_imputed['Numerical_Feature_1'].mean()
df_mean_imputed['Numerical_Feature_1'].fillna(mean_val_num1, inplace=True)
print(f"    - Numerical_Feature_1 after mean imputation (filled with {mean_val_num1:.2f})")

# Median Imputation
df_median_imputed = df_missing_demo.copy()
median_val_num2 = df_median_imputed['Numerical_Feature_2'].median()
df_median_imputed['Numerical_Feature_2'].fillna(median_val_num2, inplace=True)
print(f"    - Numerical_Feature_2 after median imputation (filled with {median_val_num2:.2f})")

# Constant Imputation (e.g., 0 for numerical, 'Missing' for categorical)
df_constant_imputed = df_missing_demo.copy()
df_constant_imputed['Numerical_Feature_1'].fillna(0, inplace=True)
df_constant_imputed['Categorical_Feature_1'].fillna('Missing', inplace=True)
print("    - Numerical_Feature_1 filled with 0, Categorical_Feature_1 filled with 'Missing'")

# Using SimpleImputer from scikit-learn (more robust for pipelines)
print("\n  - Using SimpleImputer (Scikit-learn):")
numerical_imputer_mean = SimpleImputer(strategy='mean')
df_missing_demo['Numerical_Feature_1'] = numerical_imputer_mean.fit_transform(df_missing_demo[['Numerical_Feature_1']])
numerical_imputer_median = SimpleImputer(strategy='median')
df_missing_demo['Numerical_Feature_2'] = numerical_imputer_median.fit_transform(df_missing_demo[['Numerical_Feature_2']])

categorical_imputer_mode = SimpleImputer(strategy='most_frequent')
df_missing_demo['Categorical_Feature_1'] = categorical_imputer_mode.fit_transform(df_missing_demo[['Categorical_Feature_1']])

print("    - DataFrame after SimpleImputer (mean for num1, median for num2, mode for cat1):")
print(df_missing_demo[['Numerical_Feature_1', 'Numerical_Feature_2', 'Categorical_Feature_1']])
print("    - Missing values after imputation:\n", df_missing_demo.isnull().sum())
print("\n" + "=" * 50 + "\n")

# --- 4. Handling Duplicate Data ---

print("4. Handling Duplicate Data:")
print("  - Original DataFrame (potential duplicates introduced initially):")
print(df)
print(f"  - Number of duplicate rows found: {df.duplicated().sum()}")

df_no_duplicates = df.drop_duplicates()
print("  - DataFrame after dropping all duplicate rows:")
print(df_no_duplicates)
print(f"  - New shape: {df_no_duplicates.shape}")
print("\n" + "=" * 50 + "\n")

# Re-align df for subsequent steps to be cleaner after imputation and duplicates
df = df_missing_demo.drop_duplicates().reset_index(drop=True)
print("  - DataFrame for subsequent steps (imputed & no duplicates, reset index):")
print(df)
print("\n" + "=" * 50 + "\n")

# --- 5. Feature Scaling ---

print("5. Feature Scaling:")
# Assume 'Numerical_Feature_1' and 'Numerical_Feature_2' are our numerical features
numerical_features_to_scale = ['Numerical_Feature_1', 'Numerical_Feature_2']

# 5.1 StandardScaler (Z-score normalization)
scaler_standard = StandardScaler()
df_scaled_standard = df.copy()
df_scaled_standard[numerical_features_to_scale] = scaler_standard.fit_transform(df[numerical_features_to_scale])
print("  - After StandardScaler (mean=0, std=1):")
print(df_scaled_standard[numerical_features_to_scale].describe())
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
sns.histplot(df['Numerical_Feature_1'], kde=True, color='skyblue')
plt.title('Original Numerical_Feature_1')
plt.subplot(1, 2, 2)
sns.histplot(df_scaled_standard['Numerical_Feature_1'], kde=True, color='salmon')
plt.title('Scaled Numerical_Feature_1 (StandardScaler)')
plt.tight_layout()
plt.show()


# 5.2 MinMaxScaler (Normalization to [0, 1])
scaler_minmax = MinMaxScaler()
df_scaled_minmax = df.copy()
df_scaled_minmax[numerical_features_to_scale] = scaler_minmax.fit_transform(df[numerical_features_to_scale])
print("\n  - After MinMaxScaler (values between 0 and 1):")
print(df_scaled_minmax[numerical_features_to_scale].describe())

# 5.3 RobustScaler (less sensitive to outliers)
scaler_robust = RobustScaler()
df_scaled_robust = df.copy()
df_scaled_robust[numerical_features_to_scale] = scaler_robust.fit_transform(df[numerical_features_to_scale])
print("\n  - After RobustScaler (uses IQR):")
print(df_scaled_robust[numerical_features_to_scale].describe())
print("\n" + "=" * 50 + "\n")


# --- 6. Encoding Categorical Features ---

print("6. Encoding Categorical Features:")

df_encoded_demo = df.copy()

# 6.1 One-Hot Encoding (for nominal categories)
print("  - One-Hot Encoding 'Categorical_Feature_1':")
encoder_ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False) # sparse_output=False for dense array
ohe_features = encoder_ohe.fit_transform(df_encoded_demo[['Categorical_Feature_1']])
ohe_df = pd.DataFrame(ohe_features, columns=encoder_ohe.get_feature_names_out(['Categorical_Feature_1']))
df_encoded_ohe = pd.concat([df_encoded_demo, ohe_df], axis=1)
df_encoded_ohe.drop('Categorical_Feature_1', axis=1, inplace=True) # Drop original column
print(df_encoded_ohe[['Categorical_Feature_1_A', 'Categorical_Feature_1_B', 'Categorical_Feature_1_C']].head())
print(f"    - New columns: {ohe_df.columns.tolist()}")

# 6.2 Label Encoding (for target variables or when order doesn't matter and not many categories)
# For 'Target' variable (binary classification 0/1, already encoded in this case, but useful for strings)
print("\n  - Label Encoding 'Boolean_Feature' (converting True/False to 0/1):")
encoder_le = LabelEncoder()
df_encoded_demo['Boolean_Feature_Encoded'] = encoder_le.fit_transform(df_encoded_demo['Boolean_Feature'])
print(df_encoded_demo[['Boolean_Feature', 'Boolean_Feature_Encoded']].head())
print(f"    - Mapping: {list(encoder_le.classes_)} -> {list(encoder_le.transform(encoder_le.classes_))}")


# 6.3 Ordinal Encoding (for ordinal categories with a specific order)
print("\n  - Ordinal Encoding 'Ordinal_Feature':")
# Define the order
ordered_categories = ['Low', 'Medium', 'High']
encoder_oe = OrdinalEncoder(categories=[ordered_categories])
df_encoded_demo['Ordinal_Feature_Encoded'] = encoder_oe.fit_transform(df_encoded_demo[['Ordinal_Feature']])
print(df_encoded_demo[['Ordinal_Feature', 'Ordinal_Feature_Encoded']].head())
print(f"    - Mapping: {ordered_categories} -> {list(encoder_oe.transform(np.array(ordered_categories).reshape(-1, 1)).flatten())}")
print("\n" + "=" * 50 + "\n")


# --- 7. Feature Engineering (Basic Examples) ---

print("7. Feature Engineering (Basic Examples):")

df_fe = df.copy()

# 7.1 Creating new features from existing numerical features
df_fe['Numerical_Sum'] = df_fe['Numerical_Feature_1'] + df_fe['Numerical_Feature_2']
df_fe['Numerical_Product'] = df_fe['Numerical_Feature_1'] * df_fe['Numerical_Feature_2']
print("  - Created 'Numerical_Sum' and 'Numerical_Product':")
print(df_fe[['Numerical_Feature_1', 'Numerical_Feature_2', 'Numerical_Sum', 'Numerical_Product']].head())

# 7.2 Binning/Discretization of a numerical feature
# Cut 'Numerical_Feature_1' into 3 bins
bins = pd.cut(df_fe['Numerical_Feature_1'], bins=3, labels=['Low_Num1', 'Medium_Num1', 'High_Num1'])
df_fe['Numerical_Feature_1_Bin'] = bins
print("\n  - Binned 'Numerical_Feature_1' into 3 categories:")
print(df_fe[['Numerical_Feature_1', 'Numerical_Feature_1_Bin']].head())
print(f"    - Value counts for bin: \n{df_fe['Numerical_Feature_1_Bin'].value_counts()}")
print("\n" + "=" * 50 + "\n")


# --- 8. Data Splitting ---

print("8. Data Splitting:")

X = df.drop('Target', axis=1) # Features
y = df['Target']             # Target variable

print(f"  - Original features (X) shape: {X.shape}")
print(f"  - Original target (y) shape: {y.shape}")

# 8.1 Basic Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(f"\n  - Basic Train-Test Split (test_size=0.3):")
print(f"    - X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
print(f"    - X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")
print(f"    - Target distribution in original: \n{y.value_counts(normalize=True)}")
print(f"    - Target distribution in y_train: \n{y_train.value_counts(normalize=True)}")
print(f"    - Target distribution in y_test: \n{y_test.value_counts(normalize=True)}")

# 8.2 Stratified Train-Test Split (important for imbalanced classification targets)
# Ensures that the proportion of each class in the target variable is the same in both the training and testing sets.
X_train_strat, X_test_strat, y_train_strat, y_test_strat = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"\n  - Stratified Train-Test Split (test_size=0.3, stratify=y):")
print(f"    - X_train_strat shape: {X_train_strat.shape}, y_train_strat shape: {y_train_strat.shape}")
print(f"    - X_test_strat shape: {X_test_strat.shape}, y_test_strat shape: {y_test_strat.shape}")
print(f"    - Target distribution in y_train_strat: \n{y_train_strat.value_counts(normalize=True)}")
print(f"    - Target distribution in y_test_strat: \n{y_test_strat.value_counts(normalize=True)}")
print("\n" + "=" * 50 + "\n")


# --- 9. Using Pipelines and ColumnTransformers ---

print("9. Using Pipelines and ColumnTransformers:")
print("  - This is the recommended way for production-ready preprocessing.")

# Define column types based on the original DataFrame for the pipeline
numerical_cols = ['Numerical_Feature_1', 'Numerical_Feature_2']
categorical_nominal_cols = ['Categorical_Feature_1', 'Categorical_Feature_2']
categorical_ordinal_cols = ['Ordinal_Feature']

# Define preprocessing steps
# Numerical features: Impute with mean, then scale
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Categorical nominal features: Impute with most frequent, then One-Hot Encode
categorical_nominal_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Categorical ordinal features: Impute with most frequent, then Ordinal Encode
# Ensure the order is explicitly defined
ordinal_categories_order = [['Low', 'Medium', 'High']] # Must be list of lists for OrdinalEncoder
categorical_ordinal_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('ordinal', OrdinalEncoder(categories=ordinal_categories_order, handle_unknown='use_encoded_value', unknown_value=-1)) # unknown_value for new categories
])

# Create a ColumnTransformer to apply different transformations to different columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat_nom', categorical_nominal_transformer, categorical_nominal_cols),
        ('cat_ord', categorical_ordinal_transformer, categorical_ordinal_cols)
    ],
    remainder='passthrough' # Keep other columns (like 'Boolean_Feature') as they are
)

# Example: Using the preprocessor in a full pipeline with a classifier
from sklearn.linear_model import LogisticRegression

full_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                ('classifier', LogisticRegression(random_state=42, max_iter=200))])

# Re-split data for pipeline demonstration, ensuring it has all original columns
X_pipeline_train, X_pipeline_test, y_pipeline_train, y_pipeline_test = train_test_split(
    df.drop('Target', axis=1), df['Target'], test_size=0.3, random_state=42, stratify=df['Target']
)

print("\n  - Fitting the full pipeline on training data (includes imputation, scaling, encoding):")
full_pipeline.fit(X_pipeline_train, y_pipeline_train)

print("\n  - Transforming test data using the fitted pipeline:")
# The pipeline automatically applies the trained preprocessor to the test data
y_pred_pipeline = full_pipeline.predict(X_pipeline_test)

from sklearn.metrics import accuracy_score
print(f"\n  - Accuracy of the model with full pipeline: {accuracy_score(y_pipeline_test, y_pred_pipeline):.4f}")

# You can also transform data separately
X_train_processed = preprocessor.fit_transform(X_pipeline_train)
X_test_processed = preprocessor.transform(X_pipeline_test)

# To see the column names after transformation (requires knowing the order of transformers)
# This can be tricky with OneHotEncoder as it adds multiple columns
# For a simpler view, you can check shapes:
print(f"\n  - X_train_processed shape: {X_train_processed.shape}")
print(f"  - X_test_processed shape: {X_test_processed.shape}")


print("\nAll data loading and preprocessing techniques demonstrated for practice!")