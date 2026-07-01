class Reactor:
    def __init__(self):
        pass

    def react(self, analysis):
        return {"reaction": f"Reacting to: {analysis}"}

    def execute(self):
        print("[Reactor] Ready")
