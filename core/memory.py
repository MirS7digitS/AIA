import json
import os

class MemorySystem:
    def __init__(self, config):
        self.config = config
        self.memory_file = self.config.memory_file
        self.max_entries = self.config.memory_max_entries
        self.auto_prune_threshold = self.config.memory_auto_prune
        self.emotional_tagging_enabled = self.config.emotional_tagging_enabled
        self.emotional_tags = self.config.emotional_tags
        self.memories = []
        self.load_memory()

    def load_memory(self):
        if not os.path.exists(self.memory_file):
            # Initialize empty memory file if missing
            with open(self.memory_file, "w") as f:
                json.dump([], f)
            self.memories = []
            return

        try:
            with open(self.memory_file, "r") as f:
                self.memories = json.load(f)
        except json.JSONDecodeError:
            print("Memory file corrupted or empty, starting fresh memory")
            self.memories = []

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memories, f, indent=2)

    def add_memory(self, text, tags=None):
        if tags is None and self.emotional_tagging_enabled:
            tags = [self.config.emotional_tags[0]]  # default tag (e.g., "neutral")
        memory_entry = {
            "text": text,
            "tags": tags or [],
        }
        self.memories.append(memory_entry)
        if len(self.memories) > self.auto_prune_threshold:
            self.prune_memory()
        self.save_memory()

    def prune_memory(self):
        # Simple prune oldest memories to keep within max_entries
        excess = len(self.memories) - self.max_entries
        if excess > 0:
            self.memories = self.memories[excess:]

    def search_memories(self, keyword):
        return [m for m in self.memories if keyword in m["text"]]

