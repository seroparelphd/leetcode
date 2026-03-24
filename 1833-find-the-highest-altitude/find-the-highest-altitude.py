class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_sum = 0
        max_sum = 0
        # prefix_sums = {}
        for i in range(len(gain)):
            curr_sum += gain[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum

        

# nums    = [-5, 1,5,0,-7]
# prefix  = [-5,-4,1,1,-6]
# index   = [ 0, 1,2,3, 4]
# hashmap = {0: -5,
#             1: -4
#             2: }