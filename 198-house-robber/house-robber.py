class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases
        # if n == 0:
        #     return 0
        # if n <= 2:
        #     return 1

        # Function
        trib1, trib2 = 0, 0
        # for _ in range(3, n + 1):
        for n in nums:
            trib1, trib2 = trib2, max(n + trib1, trib2)
        return trib2
