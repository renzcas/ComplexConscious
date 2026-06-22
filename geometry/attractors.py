# geometry/attractors.py

import numpy as np

class Attractors:
    """
    Finds attractor points of the system:
    points where the gradient is near zero.
    """

    def __init__(self, gradient, threshold=1e-3):
        self.gradient = gradient
        self.threshold = threshold

    def is_attractor(self, x):
        """
        Check if ||∇V(x)|| is small enough to be a stable point.
        """
        grad = self.gradient.compute(x)
        return np.linalg.norm(grad) < self.threshold

    def search(self, x0, dynamics, steps=200):
        """
        Follow the dynamics and see if we converge to an attractor.
        """
        x = x0.copy()
        for _ in range(steps):
            x = dynamics.step(x)
            if self.is_attractor(x):
                return x
        return None
