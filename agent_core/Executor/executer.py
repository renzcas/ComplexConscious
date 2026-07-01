class Executor:
    def __init__(self):
        self.log = []

    def act(self, brain_output):
        action = f"Executing action based on: {brain_output}"
        self.log.append(action)
        return {"execution": action}

    def execute(self):
        print("[Executor] Ready")
