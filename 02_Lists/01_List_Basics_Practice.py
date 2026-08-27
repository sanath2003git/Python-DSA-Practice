n = int(input())
numbers = list(map(int,input().split()))
even_numbers = []
for i in range(n):
    if numbers[i] % 2 == 0:
        even_numbers.append(numbers[i])
print(even_numbers)
print(numbers[-1])
numbers.append(100)
numbers.pop()
print(numbers)