# visualization/plane.py

import matplotlib.pyplot as plt

class Plane:
    """
    The 2D complex-plane canvas.
    All visualizations draw on this.
    """

    def __init__(self, size=6):
        self.fig, self.ax = plt.subplots(figsize=(size, size))
        self.ax.set_aspect('equal')
        self.ax.set_xlabel("Real axis")
        self.ax.set_ylabel("Imaginary axis")
        self.ax.set_title("ComplexConscious Plane")

    def clear(self):
        """Clear the plane for a new frame."""
        self.ax.cla()
        self.ax.set_aspect('equal')
        self.ax.set_xlabel("Real axis")
        self.ax.set_ylabel("Imaginary axis")

    def show(self):
        """Display the plot."""
        plt.show()
