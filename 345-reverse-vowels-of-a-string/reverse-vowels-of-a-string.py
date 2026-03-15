class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = []
        for char in s:
            s_list.append(char)

        vowels = ["A","a","E","e","I","i","O","o","U","u"]
        l, r = 0, len(s_list) - 1
        while l < r:
            while l < r and s_list[l] not in vowels:
                l += 1
            while l < r and s_list[r] not in vowels:
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        
        return "".join(s_list)