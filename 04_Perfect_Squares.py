def minimum_squares(n):

    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        # Worst case: i = 1² + 1² + ...
        dp[i] = i

        j = 1

        # Try all perfect squares <= i
        while j * j <= i:

            dp[i] = min(
                dp[i],
                1 + dp[i - j * j]
            )

            j += 1

    return dp[n]


# Input
n = int(input())

# Output
print(minimum_squares(n))