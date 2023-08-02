import numpy as np
import matplotlib.pyplot as plt

# Define the grid
x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))

# Constants
epsilon_0 = 8.85418782e-12  # Permittivity of free space

# Charge distribution (rho) for Gauss's Law for Electric Fields
rho = 1e-8  # Charge density

# Electric field (E) components
Ex = rho * x / (2 * np.pi * epsilon_0 * (x**2 + y**2)**(3/2))
Ey = rho * y / (2 * np.pi * epsilon_0 * (x**2 + y**2)**(3/2))

# Divergence of the electric field
divE = (Ex * (x**2 + y**2)**(1/2) + Ey * (x**2 + y**2)**(1/2)) / epsilon_0

# Create a vector field plot for Gauss's Law for Electric Fields
plt.quiver(x, y, Ex, Ey, angles='xy', scale_units='xy', scale=2, color='b')
plt.streamplot(x, y, Ex, Ey, color='b', linewidth=1, density=1.5, arrowstyle='-|>', arrowsize=1)

# Show the divergence of the electric field using contour lines
plt.contour(x, y, divE, colors='r', levels=[0], linewidths=2)

plt.xlabel('x')
plt.ylabel('y')
plt.title("Maxwell's Equations: Gauss's Law for Electric Fields")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.axis('equal')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
