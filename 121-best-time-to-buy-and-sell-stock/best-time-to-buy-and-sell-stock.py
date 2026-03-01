class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r  
            r += 1
        return max_profit

# l = 0
# r = 2
# prices[l] = 7
# prices[r] = 5
# profit = 6
# max_profit = 6



# l = 0
# r = 1
# max_profit = 0
# prices[l] = 7
# prices[r] = 1
# profit = 6
