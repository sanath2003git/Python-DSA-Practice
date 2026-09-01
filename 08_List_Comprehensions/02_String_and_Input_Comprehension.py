s = "programming"
v_in_s = [ch for ch in s if ch in "aeiou"]
print(v_in_s)
numbers = [int(num) for num in input().split()]
cube_odd_numbers = [num * num * num for num in numbers if num % 2 != 0]
print(cube_odd_numbers)