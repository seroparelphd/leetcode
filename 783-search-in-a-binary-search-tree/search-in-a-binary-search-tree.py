# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # stack = []
        while root:
            if root.val == val:
                # print(f"root.val = {root.val}")
                # stack.append(root.val)
                return root
            elif root.val > val:
                # stack.append(root.val)
                root = root.left
            elif root.val < val:
                # stack.append(root.val)
                root = root.right
            else:
                return []