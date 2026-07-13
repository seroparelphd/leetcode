class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def dfs(i):
            # print(f"i = {i}")
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            # print(f"  cache = {cache}")
            return cache[i]
        # print(f"dfs(0), dfs(1) = {dfs(0), dfs(1)}")
        return min(dfs(0), dfs(1))