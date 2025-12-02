class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak = 0  # Start with 0 consecutive numbers
        max_streak = 0

        # Scan each element i of list
        for i in nums:
            if i == 1: # Check if i is a 1
                streak += 1 # If i = 1, add to streak
                if streak > max_streak:
                    max_streak += 1
            else:
                streak = 0  # If i = 0, reset the streak

        return max_streak
                


        