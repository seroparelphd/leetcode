class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # print(len(grid), len(grid[0]))
        m = len(grid)
        n = len(grid[0])
        q = deque()  # Location(s) of rotten orange(s)

        # Count fresh oranges
        fresh = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:  # representing a rotten orange
                    q.append((row, col))
                elif grid[row][col] == 1:  # representing a fresh orange
                    fresh += 1
        # print(f"fresh = {fresh}")
        # print(f"q = {q}")

        # Track: number of minutes that must elapse until no cell has a fresh orange
        minutes = 0
            
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # up, left, right, down
        while q and fresh > 0:
            level_size = len(q)
            for i in range(level_size):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < m and 0 <= col < n and grid[row][col] == 1):
                        grid[row][col] = 2  # turn rotten
                        q.append((row, col))
                        fresh -= 1
            minutes += 1
            # print(minutes, fresh)
        return minutes if fresh == 0 else -1

# grid = [[2,1,1],
#         [0,1,1],
#         [1,0,1]]
