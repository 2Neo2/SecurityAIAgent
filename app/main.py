from app.graph.graph import build_graph

app = build_graph()

if __name__ == "__main__":
    result = app.invoke({
        "question": "Что такое RAG?",
        "documents": [],
        "answer": ""
    })

    print(result["answer"])