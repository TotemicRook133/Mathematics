import numpy as np
import matplotlib.pyplot as plt
from scipy.special import zeta

# Define the range of x values
x = np.linspace(0.1, 30, 1000)

# Calculate the corresponding y values using the Riemann zeta function
y = zeta(x)

# Create the plot
plt.plot(x, y)

# Set labels for the axes
plt.xlabel('x')
plt.ylabel('ζ(x)')

# Set the title for the plot
plt.title('Graph of Riemann zeta function')

# Show the plot
plt.show()
