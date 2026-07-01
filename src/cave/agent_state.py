from dataclasses import dataclass, field
from typing import Any, List
import numpy as np

@dataclass
class AgentState:
    """
    Represents the evolving internal state of a CaveAgent.
    """
    short_term: List[Any] = field(default_factory=list)
    long_term: List[Any] = field(default_factory=list)
    mood: float = 0.0
    stability: float = 1.0

    def update_memory(self, latent: np.ndarray):
        """
        Store latent vector in short-term memory and optionally long-term memory.
        """
        self.short_term.append(latent)

        # Long-term memory stores only major shifts
        if len(self.short_term) > 2:
            delta = np.linalg.norm(self.short_term[-1] - self.short_term[-2])
            if delta > 5.0:
                self.long_term.append(latent)

    def update_state(self, latent: np.ndarray):
        """
        Update mood and stability based on latent geometry.
        Grounded, symbolic, safe.
        """
        magnitude = float(np.linalg.norm(latent))
        variance = float(np.var(latent))

        # Mood increases with magnitude (symbolic energy)
        self.mood = 0.7 * self.mood + 0.3 * magnitude

        # Stability decreases with variance (symbolic chaos)
        self.stability = 0.8 * self.stability + 0.2 * (1.0 / (1.0 + variance))
