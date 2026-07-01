# src/cave/latent_geometry.py
from typing import Protocol, Any
from .layers import RepresentationState, CaveLayer

class LatentGeometry(Protocol):
    def encode(self, x: Any) -> Any:
        ...

    def decode(self, z: Any) -> Any:
        ...

    def measure_alignment(self, z1: Any, z2: Any) -> float:
        ...

def to_volcano_state(x: Any, model: LatentGeometry) -> RepresentationState:
    z = model.encode(x)
    return RepresentationState(
        layer=CaveLayer.VOLCANO,
        data=z,
        metadata={"source": type(model).__name__}
    )
