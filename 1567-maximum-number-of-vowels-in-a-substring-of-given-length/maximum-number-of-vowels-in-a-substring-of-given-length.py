class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count  # max_count = 1
        # print(f"max_count = count = {max_count}")
        for j in range(k, len(s)):  # k = 3, j = 4
            if s[j] in vowels:      # s[j] = i
                count += 1          # count = 3
            if s[j - k] in vowels:
                count -= 1
            max_count = max(max_count, count)
        return max_count
