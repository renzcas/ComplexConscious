from modules.scanner import Scanner
from modules.parser import Parser
from modules.analyzer import Analyzer
from modules.reactor import Reactor
from modules.memory import Memory
from modules.planner import Planner
from modules.worldmodel import WorldModel
from modules.agentbrain import AgentBrain
from modules.executor import Executor


class AgentSystem:
    def __init__(self):
        # Core modules
        self.scanner = Scanner()
        self.parser = Parser()
        self.analyzer = Analyzer()
        self.reactor = Reactor()

        # Cognitive modules
        self.memory = Memory()
        self.planner = Planner()
        self.worldmodel = WorldModel()

        # Brain + executor
        self.brain = AgentBrain(
            memory=self.memory,
            planner=self.planner,
            worldmodel=self.worldmodel,
            reactor=self.reactor
        )
        self.executor = Executor()

    def run(self, raw_input):
        print("\n=== Agent Cycle Start ===")

        scanned = self.scanner.scan(raw_input)
        print("Scanned:", scanned)

        parsed = self.parser.parse(scanned)
        print("Parsed:", parsed)

        analysis = self.analyzer.analyze(parsed)
        print("Analysis:", analysis)

        reaction = self.reactor.react(analysis)
        print("Reaction:", reaction)

        brain_output = self.brain.think(analysis)
        print("Brain Output:", brain_output)

        execution = self.executor.act(brain_output)
        print("Execution:", execution)

        print("=== Agent Cycle End ===\n")
        return execution


if __name__ == "__main__":
    agent = AgentSystem()

    while True:
        user_input = input("Enter input for agent (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        agent.run(user_input)
