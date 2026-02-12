class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Convert nums1 into a set (O(n) time, O(n) space)
        nums1_set = {}
        for num in nums1:
            nums1_set[num] = 1 + nums1_set.get(num, 0)
        # 2. Initialize a result set to handle uniqueness
        result = []
        # 3. Iterate through nums2
        for num2 in nums2:
        #    - If num is in the first set, add it to result set
            if num2 in nums1_set and num2 not in result:
                result.append(num2)
        # 4. Return result as a list        
        return result