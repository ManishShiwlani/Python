def numRollsToTarget(d, f,target):
    # Edge cases
    if d * f < target or d > target:
        return 0
    # One die only, check whether f >= target
    if d == 1:
        if target <= f:
            return 1
        else:
            return 0
    # Mod
    M = 10 ** 9 + 7
    # Initialize DP matrix
    dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
    # Base case
    dp[0][0] = 1
    # Bottom-Up approach
    for i in range(1, d + 1):
        for j in range(1, target + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][0]
            elif j <= f:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
            else:
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1] - dp[i - 1][j - f - 1])

    return dp[d][target] % M


d = 1
f = 6
target = 3
print(numRollsToTarget(d,f,target))
