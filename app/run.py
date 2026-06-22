# app/run.py

import numpy as np

from core.state import State
from core.energy import Energy
from core.gradient import Gradient
from core.dynamics import Dynamics

from geometry.projection import Projection
from geometry.attractors import Attractors
from geometry.primes import Primes

from visualization.plane import Plane
from visualization.spirals import Spirals
from visualization.heatmap import Heatmap
from visualization.arrows import Arrows


def main():
    # --- CORE SYSTEM ---
    state = State(dim=8)
    energy = Energy()
    gradient = Gradient(energy)
    dynamics = Dynamics(gradient, step_size=0.1)

    # --- GEOMETRY ---
    projection = Projection(dim=8)
    attractors = Attractors(gradient)
    primes = Primes(attractors)

    # --- VISUALIZATION ---
    plane = Plane(size=6)
    spirals = Spirals(plane, projection)
    heatmap = Heatmap(plane, projection, energy)
    arrows = Arrows(plane, projection, gradient)

    # --- INITIAL STATE ---
    x = np.random.normal(size=8)

    # --- RUN DYNAMICS ---
    orbit = []
    for _ in range(80):
        orbit.append(x.copy())
        x = dynamics.step(x)

    # --- DRAW ---
    heatmap.draw()
    arrows.draw()
    spirals.plot_orbit(orbit, color="cyan")
    spirals.plot_point(x, color="red")

    plane.show()


if __name__ == "__main__":
    main()
