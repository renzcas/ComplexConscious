import numpy as np
from typing import Any, List

from cave.agent_ascent import entrance, labyrinth, volcano
from cave.models.simple_embed import SimpleEmbed
from cave.agent_state import AgentState
from cave.alien_reasoning import extract_concepts, infer_reasoning


class CaveAgent:
    """
    A cognitive agent that ascends the Cave layers:
    Entrance → Labyrinth → Volcano → Alien
    Now with:
    - latent geometry
    - memory (short + long term)
    - mood + stability (state)
    - symbolic reasoning (Alien layer)
    """

    def __init__(self, name: str, model_dim: int = 32):
        self.name = name
        self.model = SimpleEmbed(dim=model_dim)
        self.latent = None
        self.state = AgentState()
        self.reasoning = None

    def ascend(self, x: Any):
        """
        Run the agent through the Cave ascent pipeline.
        """
        # Cave layers
        s1 = entrance(x)
        s2 = labyrinth(s1)
        s3 = volcano(s2, self.model)

        # Latent geometry
        self.latent = s3.data

        # Update agent memory + state
        self.state.update_memory(self.latent)
        self.state.update_state(self.latent)

        # Alien layer symbolic reasoning
        concepts = extract_concepts(self.latent)
        self.reasoning = infer_reasoning(concepts)

        return self.latent


def measure_alignment(agent_a: CaveAgent, agent_b: CaveAgent) -> float:
    """
    Compare two agents' latent geometry using cosine similarity.
    """
    if agent_a.latent is None or agent_b.latent is None:
        raise ValueError("Both agents must ascend before measuring alignment.")

    return agent_a.model.measure_alignment(agent_a.latent, agent_b.latent)


def compare_many(agents: List[CaveAgent]) -> np.ndarray:
    """
    Produce an NxN alignment matrix for a list of agents.
    """
    n = len(agents)
    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            matrix[i, j] = measure_alignment(agents[i], agents[j])

    return matrix
