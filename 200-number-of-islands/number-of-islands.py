class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_islands = 0
        
        def dfs(row, col): 
            if row < 0 or col < 0 or row >=m or col >= n or grid[row][col] != "1":
                return
            grid[row][col] = "0"
            dfs(row, col + 1)  # right
            dfs(row + 1, col)  # down
            dfs(row, col - 1)  # left
            dfs(row - 1, col)  # up

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)
        

        return num_islands