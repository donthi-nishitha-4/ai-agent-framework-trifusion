class ShortTermMemory:
    def __init__(self):
        self.history = []

    def add(self, record):
        self.history.append(record)

    def recent(self, n=5):
        return self.history[-n:]
