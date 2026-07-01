class Planner:
    def __init__(self):
        self.plan = []

    def create_plan(self, analysis):
        step = f"Plan created from: {analysis}"
        self.plan.append(step)
        return {"plan": self.plan}

    def execute(self):
        print("[Planner] Ready")
