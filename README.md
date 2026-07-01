# ComplexConscious
## Intelligencia: Least Action + Compression

ComplexConscious is a small cognitive engine built on two core principles:

1. **Least Action (core/)**
   The `core` modules (`state.py`, `energy.py`, `gradient.py`, `dynamics.py`) define a mind-like system that moves along paths of minimal “cost.”  
   - `state.py` — configuration of the system  
   - `energy.py` — scalar functional measuring how “expensive” a state or trajectory is  
   - `gradient.py` / `dynamics.py` — steepest descent updates that implement a discrete principle of least action

2. **Compression (geometry/)**
   The `geometry` layer (`projection.py`, `curvature.py`, `attractors.py`, `primes.py`) compresses high-dimensional behavior into simple, stable structures.  
   - projections to a complex plane  
   - curvature of the energy landscape  
   - attractors and “prime” seeds as minimal descriptions of behavior

3. **Intelligencia Angle (visualization/ + app/)**
   The `visualization` and `app` layers turn these dynamics and compressed structures into something intelligible:
   - `visualization/` draws planes, spirals, heatmaps, and gradient arrows  
   - `app/run.py` orchestrates the system and can expose metrics like energy, compression, and an “intelligencia index”

In short: **intelligence here is modeled as low-action, high-compression behavior that remains interpretable to a human observer.**
