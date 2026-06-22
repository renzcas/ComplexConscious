# visualization/arrows.py

import numpy as np
import matplotlib.pyplot as plt

class Arrows:
    """
    Draws the gradient field (flow field) on the complex plane.
    Shows the direction energy wants to move.
    """

    def __init__(self, plane, projection, gradient):
        self.plane = plane
        self.projection = projection
        self.gradient = gradient

    def draw(self, grid_size=20, span=3.0, scale=0.2, color="white"):
        """
        Render a quiver plot of the gradient field.
        """
        xs = np.linspace(-span, span, grid_size)
        ys = np.linspace(-span, span, grid_size)

        U = np.zeros((grid_size, grid_size))
        V = np.zeros((grid_size, grid_size))

        for i, u in enumerate(xs):
            for j, v in enumerate(ys):
                # Lift (u, v) back into state space
                x = self.projection.P.T @ np.array([u, v])

                # Compute gradient
                g = self.gradient.compute(x)

                # Project gradient back to plane
                gu, gv = self.projection.to_plane(g)

                U[j, i] = gu
                V[j, i] = gv

        self.plane.ax.quiver(
            xs, ys, U, V,
            color=color,
            angles="xy",
            scale_units="xy",
            scale=1/scale,
            alpha=0.7
        )
