from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

queue = deque([0])
visited = {0}

while queue:
    node = queue.popleft()
    print(node, end=' ')

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)