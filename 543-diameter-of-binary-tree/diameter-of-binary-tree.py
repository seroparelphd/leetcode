# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Track max diameter
        self.diameter = 0

        def dfs(curr):
            # Base case
            if not curr:
                return 0

            # Height of subtrees
            left_subtree_height = dfs(curr.left)
            right_subtree_height = dfs(curr.right)

            # Update max diameter found so far
            self.diameter = max(self.diameter, left_subtree_height + right_subtree_height)

            # Calculate height of current node to return to parent
            height = 1 + max(left_subtree_height, right_subtree_height)
            return height

        # Start DFS from root node
        dfs(root)
        return self.diameter