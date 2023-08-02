import numpy as np
import matplotlib.pyplot as plt
import random

# Theorem: Fermat's Little Theorem (Primality Testing)
def is_prime_fermat(n, k=5):
    if n <= 1:
        return False
    if n == 2:
        return True
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(int(a), int(n - 1), int(n)) != 1:
            return False
    return True

# Plot primality test using Fermat's Little Theorem
x_values = np.arange(1, 101)
y_values = [is_prime_fermat(x) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='purple')
plt.xlabel('Number')
plt.ylabel('Is Prime?')
plt.title("Fermat's Little Theorem (Primality Testing)")
plt.grid()
plt.show()
