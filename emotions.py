class EmotionSystem:
    def __init__(self):
        # Initial emotional states (0.0 to 1.0)
        self.state = {"happiness": 0.5, "fear": 0.0, "curiosity": 0.5}

    def update_emotion(self, event: str, intensity: float = 0.1):
        """
        Update emotional states based on an event type.
        """
        if event == "danger":
            self.state["fear"] = min(1.0, self.state["fear"] + intensity)
            self.state["happiness"] = max(0.0, self.state["happiness"] - intensity)
        elif event == "success":
            self.state["happiness"] = min(1.0, self.state["happiness"] + intensity)
            self.state["fear"] = max(0.0, self.state["fear"] - intensity)
        elif event == "curiosity":
            self.state["curiosity"] = min(1.0, self.state["curiosity"] + intensity)

    def get_emotional_state(self):
        return self.state
