from langchain_openai import ChatOpenAI
from app.config import settings

# llm_model = ChatOpenAI(
#     model=settings.MODEL_NAME,
#     temperature=settings.TEMPERATURE,
#     max_tokens=2000,
#     timeout=30,
#     max_retries=3,
#     streaming=True
# )

llm_model = ChatOpenAI(
    model=settings.MODEL_NAME,
    temperature=settings.TEMPERATURE,
    api_key=settings.OPENAI_API_KEY,
)