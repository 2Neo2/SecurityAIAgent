from typing import TypedDict, List


class AgentState(TypedDict):
    question: str
    documents: List[str]
    answer: str
