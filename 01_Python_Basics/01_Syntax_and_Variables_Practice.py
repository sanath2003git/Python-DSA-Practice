n = int(input())
numbers = list(map(int,input().split()))
total = 0
largest = numbers[0]
for i in range(n):
    total += numbers[i]
    if numbers[i] > largest:
        largest = numbers[i]
print(total)
print(largest)
if total % 2 == 0:
    print("EVEN")
else:
    print("ODD")