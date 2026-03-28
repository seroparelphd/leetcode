from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter()
        for row in grid:
            row_counts[tuple(row)] += 1

        pairs = 0
        for col in zip(*grid):
            if tuple(col) in row_counts:
                pairs += row_counts[tuple(col)]
        return pairs