from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        # for num in arr:
        #     counter[num] += 1
        # print(counter)
        return len(counter.values()) == len(set(counter.values()))

# Time: O(n)
# Space: O(n)