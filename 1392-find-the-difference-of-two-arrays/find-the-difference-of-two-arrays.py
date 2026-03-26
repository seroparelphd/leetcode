class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        diff1 = [x for x in set1 if x not in set2]
        diff2 = [y for y in set2 if y not in set1]
        return (list([diff1, diff2]))
        # return