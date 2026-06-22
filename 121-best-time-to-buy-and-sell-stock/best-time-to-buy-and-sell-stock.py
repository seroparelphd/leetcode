class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                max_profit = max(max_profit, diff)
            else:
                l = r
            r += 1
        return max_profit

# prices = [7,1,5,3,6,4]
#           l r
# l = 0
# r = 1
# diff = 
# max_profit = 

# Time O(N)
# Space O(1)