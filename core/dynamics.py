# core/dynamics.py

import numpy as np

class Dynamics:
    """
    The cognitive update rule.
    This is where energy, data, and gradients turn into motion.
    """

    def __init__(self, gradient, step_size=0.1):
        self.gradient = gradient
        self.step_size = step_size

    def step(self, x):
        """
        One cognitive update:
        x_{t+1} = x_t - step_size * ∇V(x_t)
        """
        grad = self.gradient.compute(x)
        return x - self.step_size * grad

    def run(self, x, steps=1):
        """
        Run multiple updates and return the final state.
        """
        for _ in range(steps):
            x = self.step(x)
        return x
