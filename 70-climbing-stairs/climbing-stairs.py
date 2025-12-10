class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        # f(1) = 1, f(2) = 2
        prev2 = 1  # f(1)
        prev1 = 2  # f(2)
        for _ in range(3, n + 1):
            cur = prev1 + prev2
            prev2, prev1 = prev1, cur
        return prev1