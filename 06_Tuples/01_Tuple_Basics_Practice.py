point = (10, 20, 30)

print(point[0])
print(point[-1])

x, y, z = point

print(x)
print(y)
print(z)

visited = set()
visited.add((10, 20))
visited.add((30, 40))

print((10, 20) in visited)

dict1 = {(10, 20): "Start"}
print(dict1[(10, 20)])