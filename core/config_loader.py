import json

class Config:
    def __init__(self, path="config.json"):
        with open(path, "r") as f:
            self.config = json.load(f)

        memory_cfg = self.config.get("memory", {})
        self.memory_file = memory_cfg.get("file_path", "data/memory_store.json")
        self.memory_max_entries = memory_cfg.get("max_entries", 1000)
        self.memory_auto_prune = memory_cfg.get("auto_prune_threshold", 900)
        self.emotional_tagging_enabled = memory_cfg.get("emotional_tagging", {}).get("enabled", True)
        self.emotional_tags = memory_cfg.get("emotional_tagging", {}).get("tags", [])

        consciousness_cfg = self.config.get("consciousness", {})
        self.self_modeling_enabled = consciousness_cfg.get("self_modeling", {}).get("enabled", True)
        self.reflection_depth = consciousness_cfg.get("self_modeling", {}).get("reflection_depth", 2)
        self.reflection_update_interval = consciousness_cfg.get("self_modeling", {}).get("update_interval_seconds", 60)
        self.memory_integration_real_time = consciousness_cfg.get("memory_integration", {}).get("real_time", True)
        self.memory_context_window = consciousness_cfg.get("memory_integration", {}).get("context_window", 5)

        embodiment_cfg = self.config.get("embodiment", {})
        sensory = embodiment_cfg.get("sensory_inputs", {})
        self.vision_enabled = sensory.get("vision", {}).get("enabled", True)
        self.audio_enabled = sensory.get("audio", {}).get("enabled", True)
        self.proprioception_enabled = sensory.get("proprioception", {}).get("enabled", True)

        emotion_cfg = self.config.get("emotion", {})
        self.emotion_states = emotion_cfg.get("state_variables", {})
        feedback = emotion_cfg.get("feedback_loop", {})
        self.emotion_feedback_enabled = feedback.get("enabled", True)
        self.reinforcement_weights = feedback.get("reinforcement_weights", {})
        self.emotion_decay_rate = feedback.get("decay_rate_per_minute", 0.01)

        goals_cfg = self.config.get("goals", {})
        autonomy_cfg = goals_cfg.get("autonomy", {})
        self.goals_enabled = autonomy_cfg.get("enabled", True)
        self.goal_types = autonomy_cfg.get("goal_types", [])
        self.goal_priority_weights = autonomy_cfg.get("priority_weights", {})

        logging_cfg = self.config.get("logging", {})
        self.log_level = logging_cfg.get("level", "INFO")
        self.memory_log_interval = logging_cfg.get("memory_log_interval_seconds", 300)
        self.emotion_log_interval = logging_cfg.get("emotion_log_interval_seconds", 60)
        self.save_on_shutdown = logging_cfg.get("save_on_shutdown", True)

    def __repr__(self):
        return f"<Config memory_file={self.memory_file} goals_enabled={self.goals_enabled}>"

