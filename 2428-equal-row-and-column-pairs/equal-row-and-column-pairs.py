from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter()
        for row in grid:
            # row_counts[row] += 1
            row_counts[tuple(row)] += 1
            # print(row)
            # print(tuple(row))
        # print(row_counts)

        pairs = 0
        for col in zip(*grid):
            # row_counts[tuple(col)] += 1
            if tuple(col) in row_counts:
                pairs += row_counts[tuple(col)]
        # print(row_counts)
        return pairs

        # same = 0
        # for count in row_counts.values():
        #     if count > 1:
        #         same += 1
        # return same