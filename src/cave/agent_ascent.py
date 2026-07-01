# src/cave/agent_ascent.py
from .layers import RepresentationState, CaveLayer
from .latent_geometry import LatentGeometry, to_volcano_state

def entrance(x: Any) -> RepresentationState:
    return RepresentationState(layer=CaveLayer.ENTRANCE, data=x, metadata={})

def labyrinth(state: RepresentationState) -> RepresentationState:
    # placeholder: feature extraction
    features = {"features": state.data}
    return RepresentationState(layer=CaveLayer.LABYRINTH, data=features, metadata={})

def volcano(state: RepresentationState, model: LatentGeometry) -> RepresentationState:
    return to_volcano_state(state.data, model)

def alien(state: RepresentationState) -> RepresentationState:
    # meta-structure: introspection on latent geometry
    meta = {"summary": "meta-representation", "shape": str(type(state.data))}
    return RepresentationState(layer=CaveLayer.ALIEN, data=meta, metadata={})
