from collections import deque
numbers = list(map(int,input().split()))
queue = deque(numbers)
while queue:
    current = queue.popleft()
    print(current)
print("EMPTY")