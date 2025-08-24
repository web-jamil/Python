import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- 1. Basic Line Plot ---

# Create some sample data
x_data = np.linspace(0, 10, 100)
y_data = np.sin(x_data) + np.random.normal(0, 0.1, 100) # Add some noise
df_basic = pd.DataFrame({'X': x_data, 'Y': y_data})

plt.figure(figsize=(8, 5))
sns.lineplot(data=df_basic, x='X', y='Y')
plt.title('Basic Seaborn Line Plot')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# --- 2. Line Plot with Multiple Lines (Hue Semantic) ---

# Create data for multiple categories
categories = ['Category A'] * 50 + ['Category B'] * 50 + ['Category C'] * 50
time_points = list(range(50)) * 3
values = np.random.normal(10, 1, 50).cumsum() + np.random.normal(0, 0.5, 50) # A
values = np.concatenate([values, np.random.normal(12, 1, 50).cumsum() + np.random.normal(0, 0.5, 50)]) # B
values = np.concatenate([values, np.random.normal(8, 1, 50).cumsum() + np.random.normal(0, 0.5, 50)]) # C

df_multi = pd.DataFrame({
    'Time': time_points,
    'Value': values,
    'Category': categories
})

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_multi, x='Time', y='Value', hue='Category')
plt.title('Line Plot with Multiple Categories (Hue)')
plt.xlabel('Time Point')
plt.ylabel('Value')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(title='Data Category')
plt.show()

# --- 3. Line Plot with Error Bands (Default in lineplot for multiple observations per x) ---

# Generate data with multiple observations for each 'Day' to show confidence intervals
days = np.repeat(np.arange(1, 11), 5) # 10 days, 5 observations per day
group_a_values = np.random.normal(5, 1, len(days)) + days * 0.5
group_b_values = np.random.normal(6, 1.2, len(days)) + days * 0.3

df_error_bands = pd.DataFrame({
    'Day': days,
    'Value': np.concatenate([group_a_values, group_b_values]),
    'Group': ['Group A'] * len(days) + ['Group B'] * len(days)
})

plt.figure(figsize=(10, 6))
# Seaborn's lineplot automatically calculates and displays confidence intervals (95% by default)
# if there are multiple observations per x-value and hue group.
sns.lineplot(data=df_error_bands, x='Day', y='Value', hue='Group')
plt.title('Line Plot with Error Bands (Confidence Intervals)')
plt.xlabel('Day')
plt.ylabel('Observed Value')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# --- 4. Customizing Line Plot Aesthetics ---

plt.figure(figsize=(12, 7))
sns.lineplot(
    data=df_multi,
    x='Time',
    y='Value',
    hue='Category',
    style='Category',      # Different line styles per category
    markers=True,          # Add markers to data points
    dashes=False,          # Disable automatic dashing (useful if style is not set)
    palette='viridis',     # Choose a different color palette
    linewidth=2.5,         # Thicker lines
    alpha=0.8,             # Transparency of lines
    errorbar='sd',         # Show standard deviation instead of CI (if applicable)
    err_style='bars',      # Show error as bars instead of bands
    legend='full'          # Show full legend
)
plt.title('Highly Customized Seaborn Line Plot', fontsize=16)
plt.xlabel('Time Point', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='-', alpha=0.4) # Solid, more visible grid
plt.legend(title='Data Category', bbox_to_anchor=(1.05, 1), loc='upper left') # Move legend outside
plt.tight_layout() # Adjust layout to prevent labels/legend from overlapping
plt.show()

# --- 5. Line Plot with Aggregation (e.g., Mean over categories) ---

# Let's use the df_error_bands data again to show aggregation
plt.figure(figsize=(9, 6))
sns.lineplot(
    data=df_error_bands,
    x='Day',
    y='Value',
    estimator='mean',  # Explicitly state to plot the mean
    errorbar='ci',     # Show confidence interval (default)
    fmt='o',           # Format for marker only (no line if `linefmt` not given)
    markers=True,
    markerfacecolor='red',
    markeredgecolor='black',
    markeredgewidth=1,
    markersize=8,
    color='blue',      # Single color for the line
    label='Mean Value' # Label for the legend
)
plt.title('Line Plot with Mean and Confidence Interval')
plt.xlabel('Day')
plt.ylabel('Average Value')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()

# --- 6. Plotting from Wide-Form Data (using `melt` or `col`) ---

# Create wide-form data
df_wide = pd.DataFrame({
    'Time': np.arange(10),
    'Experiment_1': np.random.rand(10).cumsum(),
    'Experiment_2': np.random.rand(10).cumsum() + 2,
    'Experiment_3': np.random.rand(10).cumsum() + 4
})

# To plot with hue, it's often best to convert to long-form first using melt
df_long = df_wide.melt(id_vars='Time', var_name='Experiment', value_name='Result')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_long, x='Time', y='Result', hue='Experiment', marker='o')
plt.title('Line Plot from Wide-Form Data (after melting)')
plt.xlabel('Time')
plt.ylabel('Result')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# --- 7. Plotting on a FacetGrid for multiple subplots ---

g = sns.FacetGrid(df_multi, col='Category', col_wrap=2, height=4, aspect=1.2, sharey=False)
g.map(sns.lineplot, 'Time', 'Value', marker='o', color='skyblue')
g.set_axis_labels("Time Point", "Value")
g.set_titles("Category: {col_name}")
g.add_legend()
plt.suptitle('Line Plots on FacetGrid (Categorical Subplots)', y=1.02, fontsize=16) # Adjust suptitle position
plt.tight_layout(rect=[0, 0, 1, 0.98]) # Adjust layout to make space for suptitle
plt.show()

# --- 8. Customizing Markers, Colors, and Line Styles Manually (less common with hue, but possible) ---

plt.figure(figsize=(8, 5))
sns.lineplot(data=df_basic, x='X', y='Y',
             color='purple',
             linestyle='--',
             marker='^',
             markersize=8,
             markeredgecolor='black',
             markerfacecolor='yellow')
plt.title('Line Plot with Manual Line/Marker Customization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()

# --- 9. Saving the plot ---
# After any plt.show() call, you can save the figure before closing it.
# plt.savefig('my_line_plot.png', dpi=300, bbox_inches='tight')
# plt.savefig('my_line_plot.pdf', bbox_inches='tight')