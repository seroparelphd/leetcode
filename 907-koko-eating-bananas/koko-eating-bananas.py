class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            # mid = (hi + lo) // 2
            print(f"mid = {mid}")
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)
                # print(f"  p = {p}, hours = {hours}")
            if hours > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

# lo = 1
# hi = 30
# mid = 1 + (30 - 1) // 2 = 15
# 31 // 2 = 15
# p = 11
# hours = 3