import numpy as np
import matplotlib.pyplot as plt
import random

# Theorem: Prime Number Check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Plot prime numbers up to 100
x_values = np.arange(1, 101)
y_values = [is_prime(x) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='g')
plt.xlabel('Number')
plt.ylabel('Is Prime?')
plt.title('Prime Number Check')
plt.grid()
plt.show()