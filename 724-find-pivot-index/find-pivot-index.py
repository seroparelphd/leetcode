class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == (tot - left_sum - num):
                return i
            left_sum += num
        return -1

        