import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("--- Seaborn: All About in Code ---")

# --- 0. Setting the Aesthetic Style (Optional but Recommended) ---
# Seaborn comes with several built-in themes.
# You can set it once, and it applies to all subsequent plots.
# Common styles: 'darkgrid', 'whitegrid', 'dark', 'white', 'ticks'
sns.set_theme(style="whitegrid") # Sets a nice grid background
# You can also set context for scaling elements (e.g., "paper", "notebook", "talk", "poster")
# sns.set_context("notebook")

print("\n--- 0. Loading Sample Datasets ---")
# Seaborn comes with some useful built-in datasets for examples.
tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
fmri = sns.load_dataset("fmri")
print("Tips Dataset Head:\n", tips.head())
print("\nIris Dataset Head:\n", iris.head())

# --- 1. Relational Plots (Relationships between variables) ---
print("\n--- 1. Relational Plots (`sns.relplot`, `sns.scatterplot`, `sns.lineplot`) ---")
print("These plots show the statistical relationship between numerical variables.")

# 1.1 Scatter Plot (`sns.scatterplot`)
# Good for showing correlation between two numerical variables.
plt.figure(figsize=(8, 6))
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="smoker", style="time", size="size")
plt.title("Scatter Plot: Total Bill vs. Tip (Hue by Smoker, Style by Time, Size by Party Size)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# 1.2 Line Plot (`sns.lineplot`)
# Best for visualizing trends over time or ordered data.
plt.figure(figsize=(10, 6))
sns.lineplot(x="timepoint", y="signal", hue="event", style="region", data=fmri)
plt.title("Line Plot: fMRI Signal over Time (Hue by Event, Style by Region)")
plt.xlabel("Timepoint")
plt.ylabel("Signal")
plt.show()

# 1.3 `sns.relplot` - Figure-level function for relational plots
# Allows creating grids of subplots with `col` and `row` parameters.
print("\n--- 1.3 `sns.relplot` (Figure-level function) ---")
sns.relplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips, kind="scatter")
plt.suptitle("Relational Plot: Total Bill vs. Tip by Time of Day", y=1.02) # y adjusts suptitle position
plt.show()

sns.relplot(x="timepoint", y="signal", col="region", row="event", kind="line", data=fmri)
plt.suptitle("Relational Line Plot: fMRI Signal by Region and Event", y=1.02)
plt.show()


# --- 2. Categorical Plots (Comparisons between categories) ---
print("\n--- 2. Categorical Plots (`sns.catplot`, `sns.boxplot`, `sns.violinplot`, etc.) ---")
print("Used to visualize relationships between a numerical and one or more categorical variables.")

# 2.1 Box Plot (`sns.boxplot`)
# Shows the distribution of a numerical variable across different categories.
plt.figure(figsize=(8, 6))
sns.boxplot(x="day", y="total_bill", hue="smoker", data=tips)
plt.title("Box Plot: Total Bill by Day and Smoker Status")
plt.xlabel("Day of Week")
plt.ylabel("Total Bill ($)")
plt.show()

# 2.2 Violin Plot (`sns.violinplot`)
# Combines a box plot with a kernel density estimate (KDE) to show the full distribution shape.
plt.figure(figsize=(8, 6))
sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, inner="quartile") # inner can be "box", "quartile", "point", None
plt.title("Violin Plot: Total Bill by Day and Smoker Status")
plt.xlabel("Day of Week")
plt.ylabel("Total Bill ($)")
plt.show()

# 2.3 Bar Plot (`sns.barplot`)
# Shows the mean (or other estimator) of a numerical variable for each category.
# The error bars represent a confidence interval (default 95%).
plt.figure(figsize=(8, 6))
sns.barplot(x="sex", y="survived", hue="class", data=titanic)
plt.title("Bar Plot: Survival Rate by Sex and Class")
plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.show()

# 2.4 Count Plot (`sns.countplot`)
# Shows the counts of observations in each category (like a bar plot for categorical frequencies).
plt.figure(figsize=(8, 6))
sns.countplot(x="class", hue="who", data=titanic)
plt.title("Count Plot: Titanic Passengers by Class and Who")
plt.xlabel("Class")
plt.ylabel("Number of Passengers")
plt.show()

# 2.5 Strip Plot (`sns.stripplot`)
# Draws a scatter plot where one variable is categorical. Can show all individual observations.
plt.figure(figsize=(8, 6))
sns.stripplot(x="day", y="tip", hue="sex", data=tips, jitter=True) # jitter avoids overplotting
plt.title("Strip Plot: Tip Amount by Day and Sex")
plt.xlabel("Day of Week")
plt.ylabel("Tip ($)")
plt.show()

# 2.6 Swarm Plot (`sns.swarmplot`)
# Similar to strip plot but adjusts points to avoid overlap. Better for smaller datasets.
plt.figure(figsize=(8, 6))
sns.swarmplot(x="day", y="tip", hue="sex", data=tips)
plt.title("Swarm Plot: Tip Amount by Day and Sex")
plt.xlabel("Day of Week")
plt.ylabel("Tip ($)")
plt.show()

# 2.7 `sns.catplot` - Figure-level function for categorical plots
# Similar to `relplot`, it allows creating grids of subplots.
print("\n--- 2.7 `sns.catplot` (Figure-level function) ---")
sns.catplot(x="sex", y="survived", hue="class", col="embark_town", data=titanic, kind="bar")
plt.suptitle("Categorical Bar Plot: Survival by Sex, Class, and Embarkation Town", y=1.02)
plt.show()


# --- 3. Distribution Plots (Distributions of data) ---
print("\n--- 3. Distribution Plots (`sns.displot`, `sns.histplot`, `sns.kdeplot`, `sns.ecdfplot`) ---")
print("Used to visualize the distribution of a single variable or the relationship between two distribution variables.")

# 3.1 Histogram (`sns.histplot`)
# Shows the frequency distribution of a numerical variable.
plt.figure(figsize=(8, 6))
sns.histplot(data=tips, x="total_bill", bins=20, kde=True, hue="smoker") # kde=True overlays KDE
plt.title("Histogram of Total Bill (with KDE and Smoker Hue)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.show()

# 3.2 KDE Plot (`sns.kdeplot`)
# Kernel Density Estimate plot, visualizes the probability density function.
plt.figure(figsize=(8, 6))
sns.kdeplot(data=tips, x="total_bill", y="tip", fill=True, cmap="mako", cbar=True)
plt.title("2D KDE Plot: Total Bill vs. Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# 3.3 ECDF Plot (`sns.ecdfplot`)
# Empirical Cumulative Distribution Function plot.
plt.figure(figsize=(8, 6))
sns.ecdfplot(data=tips, x="total_bill", hue="time")
plt.title("ECDF Plot of Total Bill by Time of Day")
plt.xlabel("Total Bill ($)")
plt.ylabel("Cumulative Proportion")
plt.show()

# 3.4 `sns.displot` - Figure-level function for distribution plots
# Can combine hist, kde, ecdf, and show them in a grid.
print("\n--- 3.4 `sns.displot` (Figure-level function) ---")
sns.displot(data=tips, x="total_bill", col="time", kind="kde", rug=True) # rug adds small ticks
plt.suptitle("Distribution of Total Bill by Time of Day (KDE Plot)", y=1.02)
plt.show()


# --- 4. Regression Plots (Visualizing linear relationships) ---
print("\n--- 4. Regression Plots (`sns.regplot`, `sns.lmplot`) ---")
print("Used to visualize and model linear relationships between variables.")

# 4.1 `sns.regplot` - Axes-level function
# Plots scatter plot and fits a linear regression model.
plt.figure(figsize=(8, 6))
sns.regplot(x="total_bill", y="tip", data=tips, scatter_kws={"alpha":0.6}, line_kws={"color":"red"})
plt.title("Regression Plot: Total Bill vs. Tip")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# 4.2 `sns.lmplot` - Figure-level function for regression plots
# Integrates `regplot` with Faceting for multi-variate insights.
print("\n--- 4.2 `sns.lmplot` (Figure-level function) ---")
sns.lmplot(x="total_bill", y="tip", hue="smoker", col="time", data=tips,
           scatter_kws={"alpha":0.5}, line_kws={"lw":2})
plt.suptitle("Regression Plot: Total Bill vs. Tip by Smoker and Time", y=1.02)
plt.show()


# --- 5. Matrix Plots (Visualizing relationships in matrices) ---
print("\n--- 5. Matrix Plots (`sns.heatmap`, `sns.clustermap`) ---")

# 5.1 Heatmap (`sns.heatmap`)
# Good for visualizing correlation matrices, confusion matrices, or other grid-like data.
# First, calculate correlation matrix for numerical columns in iris dataset
iris_corr = iris.drop(columns='species').corr() # Drop non-numerical column before correlation
print("\nIris Correlation Matrix:\n", iris_corr)

plt.figure(figsize=(8, 7))
sns.heatmap(iris_corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
plt.title("Heatmap: Iris Feature Correlation")
plt.show()

# 5.2 Clustermap (`sns.clustermap`)
# Combines heatmap with hierarchical clustering to reorder rows/columns.
print("\n--- 5.2 `sns.clustermap` ---")
sns.clustermap(iris.drop(columns='species'), cmap="mako", standard_scale=1) # standard_scale standardizes rows/cols
plt.suptitle("Clustermap: Iris Features with Clustering", y=1.05) # suptitle for clustermap
plt.show()


# --- 6. Multi-Variate Grids ---
print("\n--- 6. Multi-Variate Grids (`sns.pairplot`, `sns.jointplot`) ---")

# 6.1 Pair Plot (`sns.pairplot`)
# Plots pairwise relationships between variables in a dataset.
# Diagonal plots show the distribution of each variable.
print("\n--- 6.1 `sns.pairplot` ---")
sns.pairplot(iris, hue="species", diag_kind="kde") # diag_kind can be "hist", "kde"
plt.suptitle("Pair Plot of Iris Dataset by Species", y=1.02)
plt.show()

# 6.2 Joint Plot (`sns.jointplot`)
# Visualizes the bivariate distribution of two variables along with their individual (marginal) distributions.
print("\n--- 6.2 `sns.jointplot` ---")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter", hue="smoker", alpha=0.7)
plt.suptitle("Joint Plot: Total Bill vs. Tip", y=1.02) # Note: suptitle works differently for jointplot
plt.show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="kde", fill=True, cmap="Blues")
plt.suptitle("Joint Plot (KDE): Total Bill vs. Tip", y=1.02)
plt.show()


# --- 7. Customization and Aesthetics ---
print("\n--- 7. Customization and Aesthetics ---")

# 7.1 Color Palettes
# You can set default palettes or use them directly in plots.
print(sns.color_palette("pastel")) # Displays the pastel palette colors
plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=tips, palette="rocket") # Use a specific palette
plt.title("Bar Plot with 'rocket' Color Palette")
plt.show()

# Set a palette globally for all plots
sns.set_palette("bright") # This will affect subsequent plots if not overridden

# 7.2 Customizing Matplotlib elements after Seaborn plot
plt.figure(figsize=(9, 6))
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris, s=100, alpha=0.8)

# Now use Matplotlib functions to customize
plt.title("Iris Sepal Dimensions (Customized Matplotlib Elements)", fontsize=16, color='darkgreen')
plt.xlabel("Sepal Length (cm)", fontsize=12, color='navy')
plt.ylabel("Sepal Width (cm)", fontsize=12, color='navy')
plt.xticks(rotation=45) # Rotate x-axis ticks
plt.legend(title="Iris Species", frameon=True, shadow=True, facecolor='lightyellow')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# Reset palette to default for next examples (optional)
sns.set_palette("tab10")
sns.set_theme(style="whitegrid") # Reset theme too

print("\n--- End of Seaborn All About in Code ---")