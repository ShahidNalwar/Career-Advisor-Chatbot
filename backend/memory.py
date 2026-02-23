from backend.config import Config

class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, role, content):
        self.history.append({
            "role": role,
            "content": content
        })

        # Keep only recent messages to save free-tier tokens
        if len(self.history) > Config.MAX_HISTORY:
            self.history = self.history[-Config.MAX_HISTORY:]

    def get(self):
        return self.history

    def clear(self):
        self.history = []