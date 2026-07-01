# src/cave/layers.py
from enum import Enum
from dataclasses import dataclass
from typing import Any

class CaveLayer(Enum):
    ENTRANCE = "entrance"      # raw data
    LABYRINTH = "labyrinth"    # features
    VOLCANO = "volcano"        # latent geometry
    ALIEN = "alien"            # meta-structure

@dataclass
class RepresentationState:
    layer: CaveLayer
    data: Any          # raw input, features, latent, meta
    metadata: dict     # info about transforms, model, etc.
