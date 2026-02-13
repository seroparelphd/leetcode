class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        for num in nums1:
            # print(num)
            if num in nums2:
                # print(num)
                intersection.append(num)
                nums2.remove(num)
        return intersection


        # nums1_ix = {}
        # intersection = []
        # for i, num in enumerate(nums1):
        #     nums1_ix[i] = num
        # # print(f"[DEBUG] nums1_ix = {nums1_ix}")
        # for j, num2 in enumerate(nums2):
        #     if num2 in nums1_ix.values():
        #         intersection.append(num2)
        #     if nums1_ix.get(num2):
        #         # print(nums1_ix.get(num2))
        #         # intersection.append(num2)
        #         intersection.append(nums1_ix.get(num2))
        #         # nums1_ix[num2] -= 1
        
        # # print(nums1_ix)
        # # return intersection