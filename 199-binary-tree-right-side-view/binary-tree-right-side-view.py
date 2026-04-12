# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])
        print(queue)
        while queue:
            queue_len = len(queue)
            right_node = None  # Track last valid node seen at given level
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    right_node = node  # Keep updating under end of level
                    queue.append(node.left)
                    queue.append(node.right)
            if right_node:
                result.append(right_node.val)

        return result