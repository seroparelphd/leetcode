class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1) 
        return candidate



        # counts = {}
        # current_max = 0
        # result = 0
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        #     # current_max = max()
        #     if counts[num] > current_max:
        #         result = num
        #     current_max = max(counts[num], current_max)
        # return result

        # candidate, count = 0, 0
        # for num in nums:
        #     if count == 0:
        #         candidate = num
        #     count += (1 if num == candidate else -1)
        # return candidate