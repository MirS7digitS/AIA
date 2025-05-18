class EmbodimentSystem:
    def __init__(self):
        self.sensors = {
            "vision": None,  # could integrate OpenCV
            "audio": None,   # microphone in future
        }

    def parse_input(self, raw_text):
        return {"text": raw_text, "source": "user"}
