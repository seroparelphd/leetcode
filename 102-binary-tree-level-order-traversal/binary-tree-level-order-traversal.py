# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If tree empty
        if not root: 
            return []

        # Result to return
        result = []

        # Initialize deque with root
        que = deque([root])

        while que:
            level_size = len(que)
            current_level_vals = []

            # Process nodes only on current level
            for iter in range(level_size):
                # Pop node from left
                popped = que.popleft()
                # Add its val to current level
                current_level_vals.append(popped.val)
                # Add children to queue for next level 
                if popped.left:
                    que.append(popped.left)
                if popped.right:
                    que.append(popped.right)
            
            # Add completed level to result list
            result.append(current_level_vals)

        return result
