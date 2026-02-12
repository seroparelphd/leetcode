# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check length. If different, return `False`
        if len(s) != len(t):
            return False
        # Count frequency of char in String S and T
        s_freq, t_freq = {}, {} # Counter()
        for i in range(len(s)):
            s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)

        # Compare the two counts.
        return s_freq == t_freq

