from backend.gemini_client import GeminiClient
from backend.prompts import build_prompt
from backend.memory import ConversationMemory

class CareerAdvisorBot:
    def __init__(self):
        self.client = GeminiClient()
        self.memory = ConversationMemory()

    def chat(self, user_input: str) -> str:
        # 1. Save user input
        self.memory.add("User", user_input)
        
        # 2. Build contextual prompt
        prompt = build_prompt(user_input, self.memory.get())
        
        # 3. Call Gemini
        response = self.client.generate(prompt)
        
        # 4. Save AI responsefrom backend.gemini_client import GeminiClient
from backend.prompts import build_prompt
from backend.memory import ConversationMemory

class CareerAdvisorBot:
    def __init__(self):
        self.client = GeminiClient()
        self.memory = ConversationMemory()

    # NEW: Renamed and updated to handle the stream
    def chat_stream(self, user_input: str):
        # 1. Save user input
        self.memory.add("User", user_input)
        
        # 2. Build contextual prompt
        prompt = build_prompt(user_input, self.memory.get())
        
        # 3. Stream the response chunks from Gemini
        full_response = ""
        for chunk in self.client.generate_stream(prompt):
            full_response += chunk
            yield chunk  # Send chunk to the UI immediately
            
        # 4. Save the completed AI response to memory
        self.memory.add("Advisor", full_response)

    def reset(self):
        self.memory.clear()
        self.memory.add("Advisor", response)
        
        return response

    def reset(self):
        self.memory.clear()