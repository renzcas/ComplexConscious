import numpy as np
from dataclasses import dataclass
from typing import Any

@dataclass
class CaveScene:
    name: str
    description: str
    intensity: float
    color: str
    symbol: str

def latent_to_scene(z: np.ndarray) -> CaveScene:
    """
    Convert a latent vector into a symbolic Cave scene.
    This is NOT mystical — it's a grounded mapping from geometry → metaphor.
    """

    # Basic geometric properties
    magnitude = float(np.linalg.norm(z))
    direction = float(np.mean(z))
    variance = float(np.var(z))

    # Map geometry → symbolic scene
    if magnitude < 2.0:
        return CaveScene(
            name="Entrance Chamber",
            description="Dim shadows flicker along rough stone walls.",
            intensity=magnitude,
            color="gray",
            symbol="🜁"  # air
        )

    if variance < 50.0:
        return CaveScene(
            name="Labyrinth Corridor",
            description="Twisting tunnels echo with repeating patterns.",
            intensity=variance,
            color="blue",
            symbol="🜂"  # fire
        )

    if direction > 0.5:
        return CaveScene(
            name="Volcano Lake",
            description="A vast molten lake glows with unified geometry.",
            intensity=direction,
            color="red",
            symbol="🜄"  # water
        )

    return CaveScene(
        name="Alien Transport Layer",
        description="A silent chamber of impossible angles and meta‑structure.",
        intensity=direction + variance,
        color="violet",
        symbol="🜀"  # quintessence
    )
