class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        exclusive_times = {i: 0 for i in range(n)}
        stack = []
        prev_time = 0
        for log in logs:
            fid_str, typ, ts_str = log.split(":")
            fid, ts = int(fid_str), int(ts_str)
            if typ == "start":
                if stack:
                    exclusive_times[stack[-1]] += ts - prev_time
                stack.append(fid)
                prev_time = ts
            else:
                exclusive_times[stack.pop()] += ts - prev_time + 1
                prev_time = ts + 1
        return list(exclusive_times.values())