class SelfModel:
    def __init__(self):
        self.internal_state = {}

    def update(self, memory, goals):
        self.internal_state["memory_size"] = len(memory.memory)
        self.internal_state["top_goal"] = goals.get_top_goal()
