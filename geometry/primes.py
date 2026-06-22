# geometry/primes.py

import numpy as np

class Primes:
    """
    Identifies irreducible attractors — the 'Cantor primes' of the mind.
    These are attractors that cannot be decomposed into smaller ones.
    """

    def __init__(self, attractors, min_separation=0.2):
        self.attractors = attractors
        self.min_separation = min_separation
        self.primes = []

    def add_if_prime(self, x):
        """
        Add x to the list of primes if it is sufficiently far
        from all existing primes.
        """
        for p in self.primes:
            if np.linalg.norm(x - p) < self.min_separation:
                return  # too close — not a new prime

        self.primes.append(x.copy())

    def discover(self, seeds, dynamics):
        """
        Given a list of initial states (seeds),
        find all unique irreducible attractors.
        """
        for x0 in seeds:
            attractor = self.attractors.search(x0, dynamics)
            if attractor is not None:
                self.add_if_prime(attractor)

        return self.primes
