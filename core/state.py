# core/state.py

import numpy as np

class State:
    """
    The agent's internal state vector.
    This is the 'data' that energy flows through.
    """

    def __init__(self, dim=8):
        # Initialize the state as a vector of zeros
        self.x = np.zeros(dim, dtype=float)

    def update(self, new_x):
        """Replace the internal state with a new vector."""
        self.x = np.array(new_x, dtype=float)

    def copy(self):
        """Return a copy of the current state."""
        return np.copy(self.x)
