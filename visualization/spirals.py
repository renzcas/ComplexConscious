# visualization/spirals.py

import matplotlib.pyplot as plt

class Spirals:
    """
    Draws the trajectory (orbit) of the mind on the complex plane.
    """

    def __init__(self, plane, projection):
        self.plane = plane
        self.projection = projection

    def plot_orbit(self, states, color="blue", alpha=0.8):
        """
        Plot a sequence of states as a spiral/orbit on the plane.
        """
        xs = []
        ys = []

        for x in states:
            u, v = self.projection.to_plane(x)
            xs.append(u)
            ys.append(v)

        self.plane.ax.plot(xs, ys, color=color, alpha=alpha, linewidth=2)

    def plot_point(self, x, color="red", size=40):
        """
        Plot a single point (e.g., an attractor).
        """
        u, v = self.projection.to_plane(x)
        self.plane.ax.scatter([u], [v], color=color, s=size)
