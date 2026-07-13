class Solution:
    def tribonacci(self, n: int) -> int:
        
        # Base cases
        if n == 0:
            return 0
        if n <= 2:
            return 1

        # Function
        trib1, trib2, trib3 = 0, 1, 1
        for _ in range(3, n + 1):
            trib1, trib2, trib3 = trib2, trib3, trib1 + trib2 + trib3
        return trib3

        # if n <= 1:
        #     return n
        # cache = [0, 1, 1]
        # if n in cache:
        #     return cache[n]
        # cache[n] = tribonacci(n - 1, cache) + tribonacci(n - 2, cache) + tribonacci(n - 3, cache)
        # return cache[n]