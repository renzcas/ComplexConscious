import numpy as np
from typing import Any
from cave.latent_geometry import LatentGeometry

class SimpleEmbed(LatentGeometry):
    def __init__(self, dim: int = 16):
        self.dim = dim

    def encode(self, x: Any) -> np.ndarray:
        """
        Convert input to a stable latent vector using hashing.
        This simulates a simple latent geometry model.
        """
        s = str(x)
        h = abs(hash(s))
        vec = np.array([(h >> i) & 0xFF for i in range(self.dim)], dtype=float)
        return vec / np.linalg.norm(vec)

    def decode(self, z: np.ndarray) -> Any:
        """
        Convert latent vector back into a Python list.
        (Not a true decode, but enough for testing.)
        """
        return z.tolist()

    def measure_alignment(self, z1: np.ndarray, z2: np.ndarray) -> float:
        """
        Cosine similarity between two latent vectors.
        """
        return float(np.dot(z1, z2) / (np.linalg.norm(z1) * np.linalg.norm(z2)))
