class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        collection = []  # Collect elements here
        ops = 0  # Count number of operations
        target = [x for x in range(1,k+1)]

        for i in range(0,len(nums)+1):
            if set(target).issubset(set(collection)):
                # print(collection)
                # print(ops)
                return ops
            
            collection.append(nums.pop())
            ops += 1

        # print(collection)
            