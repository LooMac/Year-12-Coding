from collections import deque

def breadth_first_search(graph, start):
    nodes = graph.keys()

    res = []
    q = deque()
    
    visited = {visit: False for i, visit in enumerate(nodes)}

    q.append(start)

    while q:
        curr = q.popleft()
        res.append(curr)

        for _ in graph[curr]:
            if not visited[_]:
                visited[_] = True
                q.append(_)
    return res

graph = {
    "A": ("B","C","D"),
    "B": ("A", "C", "D"),
    "C": ("A", "B", "D"),
    "D": ("A", "B" , "C" , "E"),
    "E": ("D")
}

print(breadth_first_search(graph, "E"))
