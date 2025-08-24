import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Basic Scatter Plot ---

# Create some simple data
np.random.seed(42) # for reproducibility
data_basic = pd.DataFrame({
    'X_Value': np.random.rand(100) * 10,
    'Y_Value': np.random.rand(100) * 10 + 2 * np.random.rand(100) # Add some noise
})

plt.figure(figsize=(8, 6))
sns.scatterplot(data=data_basic, x='X_Value', y='Y_Value')
plt.title('Basic Seaborn Scatter Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# ---

# --- 2. Scatter Plot with Hue (Categorical Variable for Color) ---

# Create data with a categorical variable
data_hue = pd.DataFrame({
    'Feature1': np.random.rand(150) * 10,
    'Feature2': np.random.rand(150) * 10,
    'Category': ['Group A'] * 50 + ['Group B'] * 50 + ['Group C'] * 50
})

plt.figure(figsize=(10, 7))
sns.scatterplot(data=data_hue, x='Feature1', y='Feature2', hue='Category')
plt.title('Scatter Plot with Hue (Categorical Coloring)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend(title='Data Group')
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# ---

# --- 3. Scatter Plot with Size and Style Semantics ---

# Create data with additional numerical and categorical variables
data_size_style = pd.DataFrame({
    'X': np.random.rand(200) * 10,
    'Y': np.random.rand(200) * 10,
    'Magnitude': np.random.rand(200) * 20 + 5, # Numerical for size
    'Type': np.random.choice(['Type X', 'Type Y', 'Type Z'], 200) # Categorical for style
})

plt.figure(figsize=(12, 8))
sns.scatterplot(
    data=data_size_style,
    x='X',
    y='Y',
    hue='Magnitude',      # Color based on numerical value
    size='Magnitude',       # Size of points based on numerical value
    style='Type',           # Marker style based on categorical value
    sizes=(50, 500),        # Range of marker sizes
    palette='viridis',      # Color map for hue
    alpha=0.7,              # Transparency of points
    legend='full'           # Show all legends
)
plt.title('Scatter Plot with Hue, Size, and Style Semantics', fontsize=16)
plt.xlabel('X Coordinate', fontsize=12)
plt.ylabel('Y Coordinate', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0) # Move legend outside
plt.tight_layout() # Adjust layout to prevent labels/legend from overlapping
plt.show()

# ---

# --- 4. Combining Scatter Plot with a Regression Line (`lmplot`) ---

# `lmplot` is useful for plotting scatter plots with regression lines,
# especially across facets. It returns a FacetGrid.
data_reg = pd.DataFrame({
    'Study_Hours': np.random.rand(100) * 8 + 1,
    'Exam_Score': (np.random.rand(100) * 15 + 40) + (np.random.rand(100) * 8 + 1) * 5,
    'Gender': np.random.choice(['Male', 'Female'], 100)
})

# Plotting a single regression line
plt.figure(figsize=(9, 6))
sns.regplot(data=data_reg, x='Study_Hours', y='Exam_Score', scatter_kws={'alpha':0.6}, line_kws={'color':'red'})
plt.title('Scatter Plot with Regression Line (using regplot)')
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()


# Plotting multiple regression lines with hue and facets (using lmplot)
g = sns.lmplot(
    data=data_reg,
    x='Study_Hours',
    y='Exam_Score',
    hue='Gender',
    col='Gender', # Create separate columns for each gender
    col_wrap=2,
    height=5, aspect=1.2,
    scatter_kws={'alpha':0.6},
    line_kws={'lw': 2}, # Line width
    ci=95 # Show 95% confidence interval for regression line
)
g.set_axis_labels("Study Hours", "Exam Score")
g.set_titles("Gender: {col_name}")
plt.suptitle('Scatter Plot with Regression Lines by Gender (using lmplot)', y=1.02, fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.98])
plt.show()

# ---

# --- 5. Customizing Markers, Colors, and Other Aesthetics Manually ---

plt.figure(figsize=(9, 6))
sns.scatterplot(
    data=data_basic,
    x='X_Value',
    y='Y_Value',
    color='darkblue',           # Single color for all points
    marker='X',                 # Custom marker style (e.g., 'o', 's', '^', 'X', '+')
    s=150,                      # Size of the markers
    edgecolor='black',          # Color of the marker's edge
    linewidth=1.5,              # Thickness of the marker's edge
    alpha=0.8                   # Transparency
)
plt.title('Customized Scatter Plot (Manual Settings)')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# ---

# --- 6. Saving the Plot ---
# After any plt.show() call, you can save the figure before closing it.
# Make sure the directory exists or you'll get an error.
# plt.savefig('my_scatter_plot.png', dpi=300, bbox_inches='tight')
# plt.savefig('my_scatter_plot.pdf', bbox_inches='tight')