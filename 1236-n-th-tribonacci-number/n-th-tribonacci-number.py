class Solution:
    def tribonacci(self, n: int) -> int:
        # # Base case: n = 1 or 2
        # if n <= 2:
        #     # return n
        #     if n != 0:
        #         return 1
        #     else:
        #         return 0
            
        # # Recursive case: climbStairs(n) = climbStairs(n - 1) + climbStairs(n - 2)
        # # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        # return self.tribonacci(n - 1) + self.tribonacci(n -  2) + self.tribonacci(n - 3)        

        if n == 0:
            return 0
        if n <= 2:
            return 1

        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):  # range(3, 4 + 1)
            # a = b
            # b = c 
            # c = a + b + c 
            a, b, c = b, c, a + b + c
        return c

# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4

# a = 1
# b = 3
# c = 7
# _ = 4