import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range of x values
x = np.linspace(-6 * np.pi, 6 * np.pi, 1000)

# Calculate the complex numbers corresponding to each x value
y = np.exp(1j * x)

# Get the real and imaginary parts of y
real_y = np.real(y)
imag_y = np.imag(y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the real and imaginary parts of y
ax.plot(x, real_y, imag_y)

# Set labels for the axes
ax.set_xlabel('x')
ax.set_ylabel('Re(y)')
ax.set_zlabel('Im(y)')

# Set the title for the plot
ax.set_title('3D Graph of y = e^(ix)')

# Show the plot
plt.show()
