def find_min_max(numbers):

    minimum = numbers[0]
    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return minimum, maximum


numbers = [7, 2, 9, 4, 1, 8]

minimum, maximum = find_min_max(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)