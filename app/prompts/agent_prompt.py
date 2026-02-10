from langchain_core.prompts import ChatPromptTemplate
from . import messages


agent_prompt = ChatPromptTemplate.from_template(messages.agent_prompt_message)
