class BaseAgent:
    def __init__(self, llm, memory=None):
        self.llm = llm
        self.memory = memory

    def run(self, input_data):
        raise NotImplementedError
