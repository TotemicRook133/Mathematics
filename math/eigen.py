import numpy as np
import matplotlib.pyplot as plt

# Define the 2x2 matrix and its known eigenvector
A = np.array([[2, 1],
              [1, 3]])

known_eigenvector = np.array([1, 1])  # Known eigenvector for this example (change as needed)

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Extract eigenvectors
eigenvector1 = eigenvectors[:, 0]
eigenvector2 = eigenvectors[:, 1]

# Create the plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), marker='o', color='red', label='Eigenvalues')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Plot the known eigenvector as a blue arrow
known_arrow = ax.quiver(0, 0, *known_eigenvector, angles='xy', scale_units='xy', scale=1,
                        color='blue', label='Known Eigenvector')

# Plot the initial eigenvector as a green arrow
initial_eigenvector = np.array([0.5, 0.5])  # Initial position of the eigenvector
eigenvector_arrow = ax.quiver(0, 0, *initial_eigenvector, angles='xy', scale_units='xy', scale=1,
                              color='green', label='Eigenvector')

# Set axis labels and limits
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.grid()
plt.legend()
plt.title('Eigenvalues and Eigenvectors')

# Function to update eigenvector position
def update_eigenvector(event):
    global initial_eigenvector, eigenvector_arrow

    x, y = event.xdata, event.ydata
    eigenvector_arrow.set_offsets((x, y))
    plt.draw()

    # Check if the eigenvector direction is close to the known eigenvector direction
    vec = np.array([x, y])
    vec /= np.linalg.norm(vec)  # Normalize the vector to make it a unit vector
    dot_product = np.dot(known_eigenvector, vec)

    if abs(dot_product - 1) < 0.1:
        ax.annotate("You found it!", (x, y), xytext=(x + 1.5, y + 1),
                    arrowprops=dict(facecolor='green', shrink=0.05))
    else:
        # Remove the previous annotation if the eigenvector is not found
        ax.texts = []

    plt.draw()

# Connect mouse event to update eigenvector position
fig.canvas.mpl_connect('motion_notify_event', update_eigenvector)

plt.show()
