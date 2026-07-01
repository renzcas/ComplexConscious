class WorldModel:
    def __init__(self):
        self.state = {}

    def update(self, parsed):
        self.state.update({"last_parsed": parsed})
        return {"world_state": self.state}

    def execute(self):
        print("[WorldModel] Ready")
