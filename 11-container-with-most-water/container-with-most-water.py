class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  # len(height) = 9
        area = 0
        while l < r:
            wd = r - l
            ht = min(height[l], height[r])
            area = max(area, wd * ht)
            # print(area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

# Time: O(n), n = len(height)
# Space: O(1)

# height = [1,8,6,2,5,4,8,3,7]  len = 9
#             l             r

# height = [1,8,6,2,5,4,8,3,7]
#           l               r
# l = 0
# r = 8
# area = 