class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums[-1] = nums.pop(0)
        # print(nums)
        l = 0
        # while l < r:
        #     if nums[l] == 0:
        #         nums.append(nums.pop(l))
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

                


# nums = [0,1,0,3,12]

# nums = [0,1,0,3,12]
# nums = [1,0,0,3,12]
# nums = [1,3,0,0,12]
#             l
#                 r
# l = 1
# r = 3
# nums[l] = 0
# nums[r] = 3