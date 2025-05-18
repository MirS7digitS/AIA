from core.memory import MemorySystem
from core.config_loader import Config

class Agent:

    def __init__(self):
        self.config = Config()
        self.memory = MemorySystem(self.config)
        self.emotion_states = dict(self.config.emotion_states or {})
        self.goals_enabled = self.config.goals_enabled
        self.goal_types = self.config.goal_types
        self.goal_priority_weights = self.config.goal_priority_weights

    def reflect_on_self(self):
        if not self.config.self_modeling_enabled:
            return
        recent_memories = self.memory.memories[-self.config.reflection_depth:]
        reflections = [f"I recall: '{m['text']}'" for m in recent_memories]
        reflection_text = " | ".join(reflections)
        self.memory.add_memory(f"Reflection: {reflection_text}", tags=["curious"])

    def update_emotions(self, event_type):
        if not self.config.emotion_feedback_enabled:
            return
        weights = self.config.reinforcement_weights
        if event_type == "goal_achieved":
            self.emotion_states["happiness"] = min(
                1.0,
                self.emotion_states.get("happiness", 0.5) + weights.get("goal_achievement", 0.1)
            )
        elif event_type == "goal_threatened":
            self.emotion_states["fear"] = min(
                1.0,
                self.emotion_states.get("fear", 0.1) + weights.get("goal_threat", 0.2)
            )
        # Decay emotions slowly
        for emotion, value in self.emotion_states.items():
            self.emotion_states[emotion] = max(0.0, value - self.config.emotion_decay_rate)

    def pursue_goals(self):
        if not self.goals_enabled:
            return
        # Choose highest priority goal to pursue
        prioritized_goals = sorted(
            self.goal_types,
            key=lambda g: self.goal_priority_weights.get(g, 0)
        )
        top_goal = prioritized_goals[-1] if prioritized_goals else None
        if top_goal:
            self.memory.add_memory(f"Pursuing goal: {top_goal}", tags=["goal"])
