class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


        # s_list = list(s)
        # for i in range(len(s_list)):
        #     if s_list[i] == "*":
        #         s_list[i] = ''
        #         j = i - 1
        #         while j >= 0:
        #             if s_list[j] != '':
        #                 s_list[j] = ''
        #                 break
        #             j -= 1
        # return "".join(s_list)