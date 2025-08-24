import matplotlib.pyplot as plt
import numpy as np

# 1. Basic Plotting
# plt.plot() is the most common function
# It automatically creates a figure and axes if none exist.

# Line plot
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show() # Displays the figure

# 2. Adding Labels and Title (Pyplot style)
plt.plot(np.array([1, 2, 3]), np.array([4, 5, 6]))
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('My First Pyplot')
plt.show()

# 3. Customizing Line Styles, Colors, Markers
x = np.linspace(0, 10, 50)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, 'r--', label='Sine Wave') # 'r--' is a shorthand for red dashed line
plt.plot(x, y_cos, 'bo:', label='Cosine Wave') # 'bo:' is shorthand for blue circles, dotted line
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.title('Sine and Cosine Waves')
plt.legend() # Displays the legend based on 'label' arguments
plt.grid(True) # Adds a grid
plt.show()

# 4. Scatter Plot
plt.scatter([1, 2, 3, 4], [4, 1, 3, 2], color='green', marker='X', s=100, alpha=0.7)
plt.title('Scatter Plot Example')
plt.show()

# 5. Bar Chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 12]
plt.bar(categories, values, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])
plt.title('Bar Chart Example')
plt.show()

# 6. Histogram
data = np.random.randn(1000) # 1000 random numbers from a standard normal distribution
plt.hist(data, bins=30, color='purple', alpha=0.7, edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
plt.savefig('my_plot1.png') # Saves as PNG
plt.savefig('my_plot1.pdf', dpi=300) # Saves as PDF with 300 DPI
plt.close() # Closes the cur

# 7. Multiple Plots in One Figure (Subplots with Pyplot)
# plt.subplot(nrows, ncols, index)
plt.figure(figsize=(10, 5)) # Create a figure explicitly

plt.subplot(1, 2, 1) # 1 row, 2 columns, first plot
plt.plot(x, y_sin, 'b-')
plt.title('Sine')

plt.subplot(1, 2, 2) # 1 row, 2 columns, second plot
plt.plot(x, y_cos, 'g:')
plt.title('Cosine')

plt.suptitle('Two Subplots Example') # Figure title
plt.tight_layout() # Adjust layout to prevent overlapping
plt.show()

# 8. Saving a Figure
plt.plot([1, 2], [3, 4])
plt.title('Plot to Save')
plt.savefig('my_plot.png') # Saves as PNG
plt.savefig('my_plot.pdf', dpi=300) # Saves as PDF with 300 DPI
plt.close() # Closes the current figure to free memory if not showing