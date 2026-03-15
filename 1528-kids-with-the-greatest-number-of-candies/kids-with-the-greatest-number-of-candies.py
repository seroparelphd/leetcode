class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            total_candy = candies[i] + extraCandies
            if total_candy >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res
