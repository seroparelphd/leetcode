class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        expected = list(range(1,len(nums)+1))
        return list(set(nums) ^ set(expected))