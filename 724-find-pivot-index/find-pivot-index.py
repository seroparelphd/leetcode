class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # half = sum(nums) // 2
        tot = sum(nums)
        left_sum = 0
        # print(half)
        # curr_sum = 0
        # for i in range(len(nums)):
        for i, num in enumerate(nums):
            # curr_sum += nums[i]
            # if int(curr_sum) == int(half):
            if left_sum == (tot - left_sum - num):
                return i
            left_sum += num
        return -1

        