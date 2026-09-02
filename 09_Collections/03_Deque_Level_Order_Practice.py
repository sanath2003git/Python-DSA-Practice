from collections import deque

queue = deque([10, 20, 30, 40, 50])

level = 1

while queue:
    size = min(2, len(queue))

    print(f"Level {level}:", end=" ")

    for _ in range(size):
        current = queue.popleft()
        print(current, end=" ")

    level += 1
    print()