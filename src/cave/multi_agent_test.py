from cave.multi_agent import CaveAgent, compare_many
from visualization.latent_plot import plot_latent_space

agents = [
    CaveAgent("vision"),
    CaveAgent("language"),
    CaveAgent("audio"),
    CaveAgent("astronomy"),
    CaveAgent("physics")
]

inputs = [
    "image of a cat",
    "the quick brown fox",
    "sine wave audio",
    "galaxy spectrum",
    "schrodinger equation"
]

# Each agent ascends its own input
for agent, x in zip(agents, inputs):
    agent.ascend(x)

# Compare all agents
matrix = compare_many(agents)
print("Alignment matrix:")
print(matrix)

# Visualize latent geometry
plot_latent_space(agents)
