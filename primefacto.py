import numpy as np
import matplotlib.pyplot as plt
import random
# Theorem: Prime Factorization
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor
        divisor += 1
    return factors

# Plot prime factors for numbers up to 100
x_values = np.arange(1, 101)
y_values = [prime_factors(x) for x in x_values]

plt.figure(figsize=(8, 6))
plt.plot(x_values, [len(factors) for factors in y_values], marker='o', linestyle='-', color='r')
plt.xlabel('Number')
plt.ylabel('Number of Prime Factors')
plt.title('Prime Factorization')
plt.grid()
plt.show()