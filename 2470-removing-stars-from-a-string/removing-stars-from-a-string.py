class Solution:
    def removeStars(self, s: str) -> str:
        # s_list = list(s)
        # for i in range(len(s_list)):
        #     if s_list[i] == "*":
        #         s_list[i] = ''
        #         j = i - 1
        #         while j >= 0 and s_list[j] != '':
        #             if s_list[j] != '':
        #                 s_list[j] = ''
        #                 continue
        #             j -= 1
        # print(''.join(s_list))

        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)