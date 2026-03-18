class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

# nums = [0,1,0,3,12]
# nums = [1,0,0,3,12]
# nums = [1,3,0,0,12]
# nums = [1,3,12,0,0]
#             l
#                  r
# l = 2
# r = 3
# nums[l] = 0
# nums[r] = 3