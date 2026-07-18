class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[1] = 1
        # print(dp)
        dp[2] = 2
        dp[3] = 5
        if n < 4:
            return dp[n]
        else:
            for i in range(4, n + 1):
                # f(n) = 2 * f(n - 1) + f(n - 3)
                dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (10**9 + 7)
            return dp[n]


# ABCD
# ABCD

# AABB
# CCDD

# AACB
# ACCB

# f(n) = 2 * f(n - 1) + f(n - 3)
# f(4) = 2 * f(4 - 1) + f(4 - 3)
#      = 2 * f(3) + f(1)
#      = 2 * 5 + 1
#      = 11