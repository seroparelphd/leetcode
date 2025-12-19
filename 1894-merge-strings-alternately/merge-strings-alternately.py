class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word3 = []
        word_min = min(len(word1),len(word2))

        for i in range(0,word_min):
            word3.append(word1[i])
            word3.append(word2[i])

        if len(word1) > len(word2):
            word3.append(word1[word_min:])
        else:
            word3.append(word2[word_min:])

        return "".join(word3)