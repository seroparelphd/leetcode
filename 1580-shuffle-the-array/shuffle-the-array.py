class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = nums[0:n]
        right = nums[n:2*n]
        result = ["NA"] * (2*n)
        j = 0

        for i in range(0,2*n,2):
            result[i] = left[j]
            result[i+1] = right[j]
            j += 1

        return result