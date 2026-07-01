from cave.multi_agent import CaveAgent
from cave.dialogue import dialogue_round

agents = [
    CaveAgent("vision"),
    CaveAgent("language"),
    CaveAgent("physics")
]

inputs = [
    "image of a cat",
    "the quick brown fox",
    "schrodinger equation"
]

for agent, x in zip(agents, inputs):
    agent.ascend(x)

session = dialogue_round(agents)

for turn in session.turns:
    print(f"{turn.speaker}: {turn.message}")
