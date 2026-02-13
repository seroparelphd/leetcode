# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # If node empty
        if not root:
            return 0
        # print(f"root.val = {root.val}")
        left_depth = self.maxDepth(root.left)
        # print(f"  left_depth = {left_depth}")
        right_depth = self.maxDepth(root.right)
        # print(f"  right_depth = {right_depth}")
        # print(f"1 + max(left_depth, right_depth) = {1 + max(left_depth, right_depth)}")
        return 1 + max(left_depth, right_depth)