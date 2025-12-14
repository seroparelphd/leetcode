class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # What are all numbers 1 to n expected
        expected = list(range(1,len(nums)+1))

        # Which numbers are not in the intersection
        return list(set(nums) ^ set(expected))