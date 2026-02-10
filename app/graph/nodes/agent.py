from app.graph.state import AgentState
from app.llm.model import llm_model
from app.prompts.agent_prompt import agent_prompt


def agent_node(state: AgentState) -> AgentState:
    context = "\n\n".join(state["documents"])

    response = llm_model.invoke(
        agent_prompt.format_messages(
            context=context,
            question=state["question"]
        )
    )

    return {
        **state,
        "answer": response
    }
