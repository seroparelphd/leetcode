class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        current_max = 0
        result = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            # current_max = max()
            if counts[num] > current_max:
                result = num
            current_max = max(counts[num], current_max)
        return result



        # count = 0
        # result = 0
        # for num in nums:
        #     if count == 0:
        #         result = num
        #     if num == result:
        #         count += 1
        #     else:
        #         count -= 1
        # return result