class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pt1, pt2 = 0, 0
        merged = []
        
        while pt1 < len(word1) and pt2 < len(word2):
            merged.append(word1[pt1])
            merged.append(word2[pt2])
            # print(merged)
            pt1 += 1
            pt2 += 1
        
        merged.append(word1[pt1:])
        merged.append(word2[pt2:])
        merged = "".join(merged)
        return merged

