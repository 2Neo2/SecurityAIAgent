from langchain_ollama.llms import OllamaLLM
from app.config import settings

llm_model = OllamaLLM(model=settings.MODEL_NAME)