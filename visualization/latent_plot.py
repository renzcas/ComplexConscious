import numpy as np
import matplotlib.pyplot as plt
from typing import List
from cave.multi_agent import CaveAgent

def plot_latent_space(agents: List[CaveAgent]):
    """
    Visualize latent vectors of multiple agents in 2D using PCA.
    """
    # Collect latent vectors
    latent_vectors = np.array([agent.latent for agent in agents])

    # PCA to reduce to 2D
    mean = latent_vectors.mean(axis=0)
    centered = latent_vectors - mean
    U, S, Vt = np.linalg.svd(centered)
    components = centered @ Vt[:2].T

    # Plot
    plt.figure(figsize=(8, 6))
    for agent, point in zip(agents, components):
        plt.scatter(point[0], point[1], label=agent.name)
        plt.text(point[0] + 0.01, point[1] + 0.01, agent.name)

    plt.title("Latent Geometry of Cave Agents")
    plt.xlabel("PC 1")
    plt.ylabel("PC 2")
    plt.legend()
    plt.grid(True)
    plt.show()
