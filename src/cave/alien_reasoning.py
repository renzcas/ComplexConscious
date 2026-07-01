import numpy as np
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class SymbolicConcept:
    name: str
    score: float
    tags: List[str]

@dataclass
class ReasoningOutput:
    concepts: List[SymbolicConcept]
    inference: str
    confidence: float

def extract_concepts(latent: np.ndarray) -> List[SymbolicConcept]:
    """
    Convert latent geometry into symbolic concepts.
    Grounded, safe, computational.
    """

    magnitude = float(np.linalg.norm(latent))
    variance = float(np.var(latent))
    direction = float(np.mean(latent))

    concepts = []

    # Energy → activity
    concepts.append(SymbolicConcept(
        name="activation",
        score=magnitude,
        tags=["energy", "intensity"]
    ))

    # Variance → chaos/order
    concepts.append(SymbolicConcept(
        name="coherence",
        score=1.0 / (1.0 + variance),
        tags=["order", "stability"]
    ))

    # Direction → positivity/negativity (symbolic only)
    concepts.append(SymbolicConcept(
        name="orientation",
        score=direction,
        tags=["direction", "bias"]
    ))

    return concepts

def infer_reasoning(concepts: List[SymbolicConcept]) -> ReasoningOutput:
    """
    Produce a symbolic inference from concepts.
    """

    activation = concepts[0].score
    coherence = concepts[1].score
    orientation = concepts[2].score

    # Simple symbolic inference rules
    if activation > 10 and coherence > 0.05:
        inference = "Agent is in a high‑energy, stable reasoning mode."
    elif activation < 5 and coherence < 0.02:
        inference = "Agent is in a low‑energy, chaotic reasoning mode."
    elif orientation > 0.5:
        inference = "Agent is oriented toward constructive interpretation."
    else:
        inference = "Agent is processing with neutral orientation."

    confidence = float((activation + coherence + abs(orientation)) / 3.0)

    return ReasoningOutput(
        concepts=concepts,
        inference=inference,
        confidence=confidence
    )
