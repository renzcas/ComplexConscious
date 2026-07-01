from cave.multi_agent import CaveAgent

agent = CaveAgent("vision")

inputs = [
    "image of a cat",
    "image of a dog",
    "image of a galaxy",
    "image of a volcano",
    "image of an alien artifact"
]

for x in inputs:
    agent.ascend(x)
    print(f"After '{x}':")
    print("  Mood:", agent.state.mood)
    print("  Stability:", agent.state.stability)
    print("  Short-term memory size:", len(agent.state.short_term))
    print("  Long-term memory size:", len(agent.state.long_term))
    print()
