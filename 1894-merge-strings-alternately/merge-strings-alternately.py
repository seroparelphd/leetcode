# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         pt1, pt2 = 0, 0
#         merged = []
        
#         while pt1 < len(word1) and pt2 < len(word2):
#             merged.append(word1[pt1])
#             merged.append(word2[pt2])
#             # print(merged)
#             pt1 += 1
#             pt2 += 1
        
#         merged.append(word1[pt1:])
#         merged.append(word2[pt2:])
#         merged = "".join(merged)
#         return merged

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 1. zip_longest creates an iterator in C (no Python loop overhead)
        # 2. The generator expression (a + b...) stays in a lower-level execution layer
        # 3. "".join() is a single C-call that pre-calculates memory needs
        return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))