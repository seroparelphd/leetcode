# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_lv = 1                              # Final ans
        current_lv = 1
        max_sum = float('-inf')
        queue = deque([root])                   # For popleft
        while queue:
            queue_len = len(queue)              # Process current depth's nodes
            current_lv_sum = 0
            for i in range(queue_len):
                node = queue.popleft()
                current_lv_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_lv_sum > max_sum:
                max_sum = current_lv_sum
                max_lv = current_lv
            current_lv += 1    
        return max_lv