from typing import List
from dataclasses import dataclass
from cave.multi_agent import CaveAgent

@dataclass
class DialogueTurn:
    speaker: str
    message: str

@dataclass
class DialogueSession:
    turns: List[DialogueTurn]

def summarize_agent(agent: CaveAgent) -> str:
    """
    Turn Alien-layer reasoning into a short symbolic utterance.
    """
    if agent.reasoning is None:
        return f"{agent.name} is silent (no reasoning yet)."

    concepts = agent.reasoning.concepts
    parts = []
    for c in concepts:
        parts.append(f"{c.name}={c.score:.2f}")

    return f"{agent.name}: {agent.reasoning.inference} | " + ", ".join(parts)

def dialogue_round(agents: List[CaveAgent]) -> DialogueSession:
    """
    One dialogue round: each agent 'speaks' based on its current reasoning.
    """
    turns = []
    for agent in agents:
        msg = summarize_agent(agent)
        turns.append(DialogueTurn(speaker=agent.name, message=msg))
    return DialogueSession(turns=turns)
