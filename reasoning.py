class ReasoningEngine:
    def deliberate(self, self_model, memory, goals):
        last_memory = memory.memory[-1]["content"]
        goal = goals.get_top_goal()
        return f"I remember '{last_memory['text']}'. My current goal is to {goal}."
