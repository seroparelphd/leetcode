class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l, r = 0, 0
        cur_max = 0
        while r < len(s):
            if s[r] in seen:
                last_seen = seen[s[r]]
                l = max(l, last_seen + 1)
            seen[s[r]] = r
            cur_max = max(cur_max, r - l + 1)
            r += 1
        return cur_max
            