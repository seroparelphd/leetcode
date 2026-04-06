# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def leaf_list(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            leaf_list(node.left, leaves)
            leaf_list(node.right, leaves)
        
        leaves1 = []
        leaves2 = []

        leaf_list(root1, leaves1)
        leaf_list(root2, leaves2)

        return leaves1 == leaves2