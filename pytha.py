import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_plot():
    side_a = side_a_entry.get()
    side_b = side_b_entry.get()

    if side_a and side_b:
        try:
            a = float(side_a)
            b = float(side_b)
            
            c = (a**2 + b**2)**0.5

            ax.clear()
            ax.plot([0, a, 0, 0], [0, 0, b, 0], 'b-')  # Triangle sides
            ax.plot([0, a, a, 0], [0, 0, b, 0], 'ro')  # Points a, b, c
            ax.plot([0, a, a, 0], [0, 0, -c, 0], 'g--')  # Dashed line representing c
            ax.set_xlim(-0.5, a + 0.5)
            ax.set_ylim(-0.5, max(b, c) + 0.5)
            ax.set_aspect('equal', adjustable='box')
            canvas.draw()
        except ValueError:
            pass

# Create the main window
root = tk.Tk()
root.title('Pythagorean Theorem Proof')

# Create the input fields
side_a_label = tk.Label(root, text='Side a:')
side_a_label.grid(row=0, column=0)

side_a_entry = tk.Entry(root)
side_a_entry.grid(row=0, column=1)

side_b_label = tk.Label(root, text='Side b:')
side_b_label.grid(row=1, column=0)

side_b_entry = tk.Entry(root)
side_b_entry.grid(row=1, column=1)

# Create the update button
update_button = tk.Button(root, text='Update Triangle', command=update_plot)
update_button.grid(row=2, column=0, columnspan=2)

# Create the Matplotlib figure
fig = Figure(figsize=(5, 5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

# Initial plot
update_plot()

# Run the main event loop
root.mainloop()
