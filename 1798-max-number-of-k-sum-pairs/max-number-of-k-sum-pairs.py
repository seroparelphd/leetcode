class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        num_operations = 0
        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum == k:
                num_operations += 1
                l += 1
                r -= 1
            elif curr_sum < k:
                l += 1
            else:
                r -= 1
        return num_operations

# nums = [3,1,3,4,3], k = 6

# nums = [1,3,3,3,4], k = 6
#           l   r

# nums = [1,2,3,3,6,6], k = 6
#             l r