class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1  # Start with 2nd element in nums
        while current < len(nums):  
            if nums[current] == nums[current-1]: # If current number is the same as previous
                del nums[current] # Then delete it
            else:  # If current number is DIFFERENT
                current += 1  # Then move on to the next
        
        return current