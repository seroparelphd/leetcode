class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # Track max difference
        max_diff = -1  # Default

        for i in range(0,len(nums)-1):  # Start at the 2nd number
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                
                    # Take the difference b/t current minus previous number
                    diff = nums[j] - nums[i]

                    # Check if this difference is higher than before 
                    # If higher, replace previous max difference
                    max_diff = max(max_diff,diff)
        
        # Return max difference
        return max_diff
