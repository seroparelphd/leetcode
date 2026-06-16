# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            middle = (left + right) // 2
            print(f"middle = {middle}")
            result = guess(middle)
            print(f"  result = {result}")
            if result == 1:
                left = middle + 1
            elif result == -1:
                right = middle
            else:
                return middle

# 1 2 3 4 5 6 7 8 9 10
# L       L M R     R

# 1 2
# L/M R