class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            for other_city in range(len(isConnected)):
                if isConnected[city][other_city] == 1:
                    isConnected[city][other_city] = 0
                    isConnected[other_city][city] = 0
                    dfs(other_city)

        num_provinces = 0
        for city in range(len(isConnected)):
            if isConnected[city][city] == 1:
                num_provinces += 1
                dfs(city)
        return num_provinces

# Time: O(n^2)
# Space: O(n)