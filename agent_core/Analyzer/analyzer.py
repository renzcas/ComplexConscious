class Analyzer:
    def __init__(self):
        pass

    def analyze(self, parsed):
        text = parsed.get("parsed", "")
        length = len(text)
        return {"analysis": f"Input length = {length}"}

    def execute(self):
        print("[Analyzer] Ready")
