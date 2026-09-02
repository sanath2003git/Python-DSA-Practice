from collections import defaultdict
edges = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3)
]
graph = defaultdict(list)

for u ,v in edges:
    graph[u].append(v)

for u,v in graph.items():
    print(u,v)