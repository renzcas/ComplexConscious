# visualization/heatmap.py

import numpy as np
import matplotlib.pyplot as plt

class Heatmap:
    """
    Draws an energy heatmap on the complex plane.
    Shows the shape of the energy landscape.
    """

    def __init__(self, plane, projection, energy):
        self.plane = plane
        self.projection = projection
        self.energy = energy

    def draw(self, grid_size=80, span=3.0, cmap="inferno"):
        """
        Render a heatmap of V(x) over the 2D projection plane.
        """
        xs = np.linspace(-span, span, grid_size)
        ys = np.linspace(-span, span, grid_size)

        Z = np.zeros((grid_size, grid_size))

        # For each point on the plane, estimate energy by lifting back to state space
        for i, u in enumerate(xs):
            for j, v in enumerate(ys):
                # Reconstruct a pseudo-state in high dimensions
                # (simple inverse projection approximation)
                x = self.projection.P.T @ np.array([u, v])
                Z[j, i] = self.energy.V(x)

        self.plane.ax.imshow(
            Z,
            extent=[-span, span, -span, span],
            origin="lower",
            cmap=cmap,
            alpha=0.75
        )
