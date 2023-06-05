import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 3)

# Generate y values for each exponential graph
y1 = np.exp(x)       # Steep exponential graph
y2 = np.exp(0.65 * x) # Less steep exponential graph
y3 = x # Least steep exponential graph

# Plot the exponential graphs
plt.plot(x, y1, label='Worst Case')
plt.plot(x, y2, label='Average Case')
plt.plot(x, y3, label='Best Case')

# Set labels and title
plt.xlabel('Input Size')
plt.ylabel('Running Time')
plt.title('Job Scheduling - Greedy')

# Add legend
plt.legend()

# Display the plot
plt.show()