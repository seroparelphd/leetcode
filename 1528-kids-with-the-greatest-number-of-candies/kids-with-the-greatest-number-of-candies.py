class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        for i in range(len(candies)):
            total_candy = candies[i] + extraCandies
            if total_candy >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res
