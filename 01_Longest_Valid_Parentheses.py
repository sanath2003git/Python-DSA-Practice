def longest_valid_parentheses(s):

    # Stack stores indexes
    stack = [-1]

    max_length = 0

    for i in range(len(s)):

        # Opening parenthesis
        if s[i] == '(':

            stack.append(i)

        # Closing parenthesis
        else:

            stack.pop()

            # Invalid closing parenthesis
            if not stack:

                stack.append(i)

            # Calculate valid parentheses length
            else:

                length = i - stack[-1]

                max_length = max(max_length, length)

    return max_length


# Input
s = input()

# Output
print(longest_valid_parentheses(s))