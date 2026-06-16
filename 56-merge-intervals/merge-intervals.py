class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # print(sorted(intervals), intervals.sort())
        intervals = sorted(intervals)
        # print(intervals, intervals[0])
        
        merged = [intervals[0]]  # empty list
        # print(f"merged = {merged}")
        # print(len(intervals))

        for i in range(1, len(intervals)):
            # print(intervals[i])
            # print(intervals[i][0])
            # print(f"len(merged) = {len(merged)}")
            # print(f"merged[-1] = {merged[-1]}, merged[-1][1] = {merged[-1][1]}") #, i[0] = {i[0]}")
            # print(f"intervals[i][0] = {intervals[i][0]}")
            if merged[-1][1] >= intervals[i][0]:
                # merged[-1][1] = intervals[i][1]
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged