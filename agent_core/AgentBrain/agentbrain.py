class AgentBrain:
    def __init__(self, memory, planner, worldmodel, reactor):
        self.memory = memory
        self.planner = planner
        self.worldmodel = worldmodel
        self.reactor = reactor

    def think(self, data):
        mem = self.memory.remember("last_input", data)
        plan = self.planner.create_plan(data)
        world = self.worldmodel.update(data)
        reaction = self.reactor.react(data)

        return {
            "brain": {
                "memory": mem,
                "plan": plan,
                "world": world,
                "reaction": reaction
            }
        }

    def execute(self):
        print("[AgentBrain] Ready")
