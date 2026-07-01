class Parser:
    def __init__(self):
        pass

    def parse(self, scanned):
        raw = scanned.get("raw", "")
        return {"parsed": raw.strip()}

    def execute(self):
        print("[Parser] Ready")
