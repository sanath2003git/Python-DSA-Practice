numbers = list(map(int, input().split()))

unique = set(numbers)

if len(numbers) != len(unique):
    print("True")
else:
    print("False")