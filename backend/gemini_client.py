import google.generativeai as genai
import logging
from backend.config import Config

logger = logging.getLogger(__name__)

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=Config.GEMINI_API_KEY)
        
        # Production fallback strategy
        model_candidates = [
            Config.MODEL_NAME,
            "gemini-2.0-flash", 
            "gemini-1.5-flash"
        ]
        
        self.model = None
        for name in model_candidates:
            try:
                self.model = genai.GenerativeModel(name)
                logger.info(f"Successfully loaded model: {name}")
                break
            except Exception:
                continue
                
        if not self.model:
            raise RuntimeError("No compatible Gemini model found in the free tier.")

    # NEW: Streaming generator method
    def generate_stream(self, prompt: str):
        try:
            response = self.model.generate_content(prompt, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
                    
        except Exception as e:
            logger.error(f"Gemini API Error: {e}")
            yield f"⚠️ API Error: {str(e)}"