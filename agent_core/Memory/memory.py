class Memory:
    def __init__(self):
        self.store = {}

    def remember(self, key, value):
        self.store[key] = value
        return {"memory_write": {key: value}}

    def recall(self, key):
        return {"memory_read": self.store.get(key, None)}

    def execute(self):
        print("[Memory] Ready")
