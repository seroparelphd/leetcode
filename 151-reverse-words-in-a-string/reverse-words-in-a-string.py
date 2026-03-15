class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        # print(s_list.reversed())
        # print(reversed(s_list))
        # for word in s_list[::-1]:
        #     print(word)
        # reversed_words = words[::-1]
        # return " ".join(reversed_words)
        return " ".join(words[::-1])