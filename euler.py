import numpy as np
import matplotlib.pyplot as plt

# Define values for theta from 0 to 2*pi
theta = np.linspace(0, 2 * np.pi, 1000)

# Calculate the complex number e^(i*theta)
complex_num = np.exp(1j * theta)

# Separate real and imaginary parts for plotting
real_part = np.real(complex_num)
imaginary_part = np.imag(complex_num)

# Plot the complex number in the complex plane
plt.figure(figsize=(8, 6))
plt.plot(real_part, imaginary_part, label='e^(iθ)', color='b')
plt.scatter(-1, 0, color='r', label='-1')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Visualization of Euler's Identity: e^(iθ)+1=0")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
