class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        # peak = float('-inf')
        # print(peak)
        while lo <= hi:
            mid = lo + (hi - lo) // 2  # 0 + (3 - 0) // 2 = 1 -> nums[1] = 2
            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')
            # if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:    # nums[1] = 2 > -inf
            if nums[mid] > left and nums[mid] > right:    # nums[1] = 2 > -inf
                return mid          # peak = 1
                # lo = mid + 1        # lo = 1 + 1 = 2  -->  2 <= 3? yes
            elif nums[mid] < right:
                lo = mid + 1
            else:  # nums[mid] > nums[mid + 1]
                hi = mid - 1
        return -1
