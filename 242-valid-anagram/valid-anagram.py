from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. Check length. If different, return `False`.
        if len(s) != len(t):
            return False
        # 2. Count frequency of char in String S.
        s_freq, t_freq = {}, {} # Counter()
        for i in range(len(s)):
            # print(s[i])
            # s_freq[i] += 1
            s_freq[s[i]] = 1 + s_freq.get(s[i], 0)
            t_freq[t[i]] = 1 + t_freq.get(t[i], 0)


        # 3. Count frequency of char in String T.
        # t_freq = {} # Counter()
        # for j in range(len(t)):
        #     t_freq[j] += 1

        # 4. Compare the two counts.
        return s_freq == t_freq

