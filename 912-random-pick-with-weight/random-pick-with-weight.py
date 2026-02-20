class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sums.append(current_sum)
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        # print(f"target = {target}")
        low, high = 0, len(self.prefix_sums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            print(f"low = {low}, high = {high}, mid = {mid}")
            if self.prefix_sums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()