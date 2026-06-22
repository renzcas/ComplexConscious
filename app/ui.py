# app/ui.py

import argparse
from app.run import main

def cli():
    """
    Simple command-line interface for ComplexConscious.
    Later you can add modes, presets, parameters, etc.
    """
    parser = argparse.ArgumentParser(description="Run ComplexConscious")
    parser.add_argument("--steps", type=int, default=80, help="Number of dynamics steps")
    args = parser.parse_args()

    # For now, just run the main loop
    main()

if __name__ == "__main__":
    cli()
