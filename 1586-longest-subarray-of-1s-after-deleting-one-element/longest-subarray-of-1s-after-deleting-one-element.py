class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = 0
        zero_count = 0
        max_consecutive = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            max_consecutive = max(max_consecutive, r - l)
            
        return max_consecutive