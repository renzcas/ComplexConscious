# geometry/curvature.py

import numpy as np

class Curvature:
    """
    Computes local curvature of the energy surface V(x).
    Emotion = curvature.
    """

    def __init__(self, energy, eps=1e-4):
        self.energy = energy
        self.eps = eps

    def hessian(self, x):
        """
        Numerical Hessian matrix H_ij = ∂²V/∂x_i∂x_j
        """
        n = len(x)
        H = np.zeros((n, n))
        base = self.energy.V(x)

        for i in range(n):
            for j in range(n):
                e_i = np.zeros(n); e_i[i] = self.eps
                e_j = np.zeros(n); e_j[j] = self.eps

                V_ij = self.energy.V(x + e_i + e_j)
                V_i  = self.energy.V(x + e_i)
                V_j  = self.energy.V(x + e_j)

                H[i, j] = (V_ij - V_i - V_j + base) / (self.eps**2)

        return H

    def curvature_scalar(self, x):
        """
        Returns a single scalar curvature measure:
        the trace of the Hessian (sum of diagonal elements).
        """
        H = self.hessian(x)
        return np.trace(H)
