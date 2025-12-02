class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_a = nums[0:n]
        nums_b = nums[n:2*n]
        nums2 = ["NA"] * (2*n)
        j = 0

        for i in range(0,2*n,2):
            nums2[i] = nums_a[j]
            nums2[i+1] = nums_b[j]
            j += 1

        return nums2