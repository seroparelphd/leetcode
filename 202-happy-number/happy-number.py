class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()  # don't loop endlessly in a cycle
        while n != 1 and n not in seen:
            seen.add(n)
            digits = []
            while n > 0:
                last_digit = n % 10
                # print(f"last_digit = {n} % 10 = {last_digit}")
                digits.append(last_digit)
                # print(f"  digits = {digits}")
                n //= 10 
                # print(f"  n = {n}")
            # print(f"digits = {digits}")

            total_sum = 0
            for d in digits:
                square = d * d
                # print(f"total_sum = {total_sum} + {square}")
                total_sum = total_sum + square
            n = total_sum
                
        return n == 1