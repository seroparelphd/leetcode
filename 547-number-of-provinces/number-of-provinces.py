class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(city):
            for other_city in range(len(isConnected)):
                if isConnected[city][other_city] == 1 and other_city not in visited:
                    visited.add(other_city)
                    dfs(other_city)

        num_provinces = 0
        visited = set()
        for city in range(len(isConnected)):
            if city not in visited:
                num_provinces += 1
                visited.add(city)
                dfs(city)

        return num_provinces