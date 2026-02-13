# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: What happens if the node is empty?
        if not root:
            return 0 # Fill this in
        # Recursive Step:
        # 1. Get the depth of the left side
        left_depth = self.maxDepth(root.left)
        # 2. Get the depth of the right side
        right_depth = self.maxDepth(root.right)
        # 3. Return the formula we discussed
        return 1 + max(left_depth, right_depth) # Fill this in