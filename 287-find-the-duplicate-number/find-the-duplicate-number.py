class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Find duplicate
        read = set()
        for i in nums:
            if i in read:
                return i
            else:
                read.add(i)