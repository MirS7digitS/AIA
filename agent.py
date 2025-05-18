from core.memory import MemorySystem
from core.emotion import EmotionSystem

class Agent:
    def __init__(self):
        self.memory = MemorySystem()
        self.emotion = EmotionSystem()

    def perceive_and_remember(self, input_text: str):
        # Store input as memory (emotional tagging could be enhanced here)
        emotional_tag = None
        # Simple tagging based on keywords
        if "danger" in input_text.lower():
            emotional_tag = "fear"
            self.emotion.update_emotion("danger")
        elif "win" in input_text.lower():
            emotional_tag = "happiness"
            self.emotion.update_emotion("success")
        elif "curious" in input_text.lower():
            emotional_tag = "curiosity"
            self.emotion.update_emotion("curiosity")

        self.memory.store_experience(input_text, emotional_tag)

        print(f"[Agent] Current emotional state: {self.emotion.get_emotional_state()}")

    def recall_all(self):
        memories = self.memory.get_memories()
        print(f"[Agent] Recalling {len(memories)} memories:")
        for mem in memories:
            print(f"- {mem['text']} (tag: {mem.get('emotional_tag')})")