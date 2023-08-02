import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Function to plot the Collatz sequence
def plot_collatz(n):
    sequence = collatz_sequence(n)
    x_values = range(len(sequence))

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, sequence, marker='o', linestyle='-', color='b')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.title(f'Collatz Conjecture for n = {n}')
    plt.grid()
    plt.show()

# Example usage
plot_collatz(6)
