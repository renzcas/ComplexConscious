import numpy as np

class State:
    """
    The agent's internal state vector.
    This is the 'data' that energy flows through.
    """

    def __init__(self, dim=8):
        self.x = np.zeros(dim, dtype=float)

    def update(self, new_x):
        self.x = np.array(new_x, dtype=float)

    def copy(self):
        return np.copy(self.x)
