from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # for num in nums1:
        #     if num in nums2:
        #         res.append(num)
        #         nums2.remove(num)
        # return res

        counts = Counter(nums1)
        # print(counts)
        res = []
        for num in nums2:
            if counts[num] > 0:
                res.append(num)
                counts[num] -= 1
        return res

