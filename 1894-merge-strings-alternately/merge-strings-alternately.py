class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        shortest = min(len(word1), len(word2))
        print(shortest)
        for i in range(shortest):
            print(word1[i])
            res = res + word1[i] + word2[i]
            print(res)
        res = res + word1[shortest:]
        res = res + word2[shortest:]
        return res