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
        queue = deque([root])  # For popleft
        print(queue)
        while queue:
            queue_len = len(queue)  # Process current depth's nodes
            right_node = None  # Track right-most node seen at given depth
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    right_node = node  # Keep updating under end of depth/level; assign right-most
                    queue.append(node.left)  # Add left child to process at next depth
                    queue.append(node.right)  # Add right
            if right_node:  # If not empty, record val of right-most node
                result.append(right_node.val)

        return result

# Time O(n)
# Space O(w), where w = max width of tree