# geometry/projection.py

import numpy as np

class Projection:
    """
    Projects high-dimensional state vectors into 2D
    for complex-plane visualization.
    """

    def __init__(self, dim=8):
        # Random projection matrix (fixed once)
        rng = np.random.default_rng(42)
        self.P = rng.normal(size=(2, dim))

    def to_plane(self, x):
        """
        Map x ∈ R^n → (u, v) ∈ R^2
        """
        uv = self.P @ x
        return float(uv[0]), float(uv[1])
