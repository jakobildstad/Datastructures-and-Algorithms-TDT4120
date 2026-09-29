def rod_cutting(prices, n):
    """Finn maksimal inntekt for en stang med lengde n."""
    dp = [0] * (n + 1)

    for length in range(1, n + 1):
        for piece_length in range(1, length + 1):
            revenue = (
                prices[piece_length - 1]
                + dp[length - piece_length]
            )
            dp[length] = max(dp[length], revenue)

    return dp[n]


print(rod_cutting([1, 4, 3, 6, 8, 5, 9], 7))


