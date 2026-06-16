# from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # if "".join(sorted(s)) == "".join(sorted(t)):
        #     return True
        # else:
        #     return False

        # return "".join(sorted(s)) == "".join(sorted(t))

        # print(Counter(s), Counter(t))
        return Counter(s) == Counter(t)

# Time: O(N log N)?
# Space: O(N)