# core/energy.py

import numpy as np

class Energy:
    """
    Defines the energy potential V(x) of the system.
    This is the 'electrical engineering' layer:
    energy flowing through data.
    """

    def __init__(self, lambda_s=0.2, lambda_c=0.3):
        # Tunable weights for entropy and coherence
        self.lambda_s = lambda_s
        self.lambda_c = lambda_c

    def E(self, x):
        """
        Base energy term.
        Think of this like electrical potential or 'tension' in the state.
        """
        return 0.5 * np.dot(x, x)

    def S(self, x):
        """
        Entropy-like term.
        Encourages exploration and spreading of the state.
        """
        return np.sum(np.abs(x))

    def C(self, x):
        """
        Coherence term.
        Encourages the state to align into meaningful patterns.
        """
        return -np.sum(np.cos(x))

    def V(self, x):
        """
        Full potential function:
        V(x) = E(x) + λs * S(x) - λc * C(x)
        """
        return self.E(x) + self.lambda_s * self.S(x) - self.lambda_c * self.C(x)
s