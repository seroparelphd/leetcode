class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0                   # Start with 0th element
        while i < len(nums):    
            if nums[i] == val:  # If current num is the same as target value
                del nums[i]     # then delete it; len(nums) decreases by 1
            else:
                i += 1          # If not the same, move on to next

        return len(nums)