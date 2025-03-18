from collections import deque

faq_graph = {
    "What is AI?": ["Machine Learning", "Deep Learning"],
    "Machine Learning": ["Supervised Learning", "Unsupervised Learning"],
    "Deep Learning": ["Neural Networks"],
    "answers": {
        "Neural Networks": "Neural Networks are AI models inspired by the human brain.",
        "Supervised Learning": "Supervised Learning uses labeled data for training."
    }
}

def bfs_find_answer(faq_graph, start_question):
    queue = deque([start_question])
    visited = set()

    while queue:
        current = queue.popleft()

        if "answers" in faq_graph and current in faq_graph["answers"]:
            return faq_graph["answers"][current]

        if current not in visited:
            visited.add(current)
            neighbors = faq_graph.get(current, [])
            queue.extend(neighbors)

    return "No relevant answer found."

query = "What is AI?"
answer = bfs_find_answer(faq_graph, query)

print(f"Relevant answer: {answer}")