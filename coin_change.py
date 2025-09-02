def getNumberOfWays(N, Coins):
    #  'ways' of size N+1, initialized to 0
    # ways[x] will store the number of ways to make amount x
    ways = [0] * (N + 1)

    # Base case
    ways[0] = 1

    for coin in Coins:
        for amt in range(coin, N + 1):
            ways[amt] += ways[amt - coin]

    return ways[N]


def printArray(coins):
    """Utility function to print coins array."""
    for c in coins:
        print(c, end=" ")
    print()


Coins = [1, 5, 10]
N = 12

print("The Coins Array:")
printArray(Coins)

print("Solution:", getNumberOfWays(N, Coins))
