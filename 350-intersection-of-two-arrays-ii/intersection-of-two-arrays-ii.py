from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # for num in nums1:
        #     if num in nums2:
        #         res.append(num)
        #         nums2.remove(num)
        # return res

        # counts = Counter(nums1)
        # res = []
        # for num in nums2:
        #     if counts[num] > 0:
        #         res.append(num)
        #         counts[num] -= 1
        # return res

        nums1.sort()  # [4, 5, 9]
                      #     i
        nums2.sort()  # [4, 4, 8, 9, 9]
                      #        j
        i, j = 0, 0  
        res = []  # [4]

        # i = 1, j = 2
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else: 
                j += 1
        return res

