class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Initialize count dictionary
        counts = {}
        
        # 2. Iterate through nums and count frequencies
        # CRITICAL: Use the .get(key, 0) pattern you learned today!
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        # 3. Check for the majority element
        # You can do this inside the loop or in a separate loop 
        return max(counts, key = counts.get)       