import numpy as np
import matplotlib.pyplot as plt
import random

# Theorem: Euclidean Algorithm for GCD (Greatest Common Divisor)
def euclidean_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Plot GCD values for various pairs of numbers
x_values = np.arange(1, 101)
y_values = [euclidean_gcd(a, b) for a in x_values for b in range(1, 101)]

plt.figure(figsize=(8, 6))
plt.plot(y_values, marker='o', linestyle='-', color='b')
plt.xlabel('Pairs of Numbers')
plt.ylabel('GCD (Greatest Common Divisor)')
plt.title('Euclidean Algorithm for GCD')
plt.grid()
plt.show()