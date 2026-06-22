# core/gradient.py

import numpy as np

class Gradient:
    """
    Computes the gradient of the energy potential V(x).
    This is the 'flow' — the direction energy wants to move.
    """

    def __init__(self, energy, eps=1e-5):
        self.energy = energy
        self.eps = eps  # small step for numerical derivative

    def compute(self, x):
        """
        Numerical gradient of V(x) using finite differences.
        ∂V/∂x_i ≈ (V(x + eps*e_i) - V(x)) / eps
        """
        grad = np.zeros_like(x)
        base = self.energy.V(x)

        for i in range(len(x)):
            step = np.zeros_like(x)
            step[i] = self.eps
            grad[i] = (self.energy.V(x + step) - base) / self.eps

        return grad
