class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word3 = ""
        word_min = min(len(word1),len(word2))

        for i in range(0,word_min):
            print(word1[i])
            word3 += word1[i] + word2[i]

        if len(word1) > len(word2):
            word3 += word1[(i+1):]
        else:
            word3 += word2[(i+1):]

        return word3