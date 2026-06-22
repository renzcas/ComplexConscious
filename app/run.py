import sys, os

# ---------------------------------------------------------
# FORCE Python to see the project root (Codespaces fix)
# ---------------------------------------------------------
ROOT = "/workspaces/ComplexConscious"
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ---------------------------------------------------------
# Normal imports
# ---------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

from core.state import State
from core.energy import Energy
from core.gradient import Gradient
from core.dynamics import Dynamics


def main():
    # Initialize components
    state = State()
    energy = Energy()
    gradient = Gradient(energy)      # ⭐ Gradient needs Energy
    dynamics = Dynamics(gradient)    # ⭐ Dynamics needs Gradient

    steps = 100
    values = []

    for _ in range(steps):
        x = state.x
        e = energy.V(x)
        g = gradient.compute(x)
        state.update(g)
        values.append(e)

    plt.plot(values)
    plt.title("Energy Over Time")
    plt.xlabel("Step")
    plt.ylabel("Energy")
    plt.show()
#    replace plt.show() wth these lines
#     plt.savefig("energy_plot.png")
#     print("Saved plot as energy_plot.png")

if __name__ == "__main__":
    main()
