import json
import time
from typing import List, Dict, Optional

class MemorySystem:
    def __init__(self, memory_file: str = "data/memory_store.json"):
        self.memory_file = memory_file
        self.memories: List[Dict] = []
        self.load_memory()

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as f:
                self.memories = json.load(f)
            print(f"[MemorySystem] Loaded {len(self.memories)} memories.")
        except FileNotFoundError:
            self.memories = []
            print("[MemorySystem] No memory file found. Starting fresh.")

    def save_memory(self):
        with open(self.memory_file, "w") as f:
            json.dump(self.memories, f, indent=2)

    def store_experience(self, experience_text: str, emotional_tag: Optional[str] = None):
        entry = {
            "timestamp": time.time(),
            "text": experience_text,
            "emotional_tag": emotional_tag
        }
        self.memories.append(entry)
        self.save_memory()
        print(f"[MemorySystem] Stored experience: '{experience_text}' with tag: '{emotional_tag}'")

    def get_memories(self, filter_tag: Optional[str] = None) -> List[Dict]:
        if filter_tag:
            return [m for m in self.memories if m.get("emotional_tag") == filter_tag]
        return self.memories