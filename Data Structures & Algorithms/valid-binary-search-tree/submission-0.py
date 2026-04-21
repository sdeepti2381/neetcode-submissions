# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], low, high) -> bool:
            if not root:
                return True

            left = dfs(root.left, low, root.val)
            right = dfs(root.right, root.val, high)

            
            if not (low < root.val < high) or not left or not right:
                return False
            else:
                return True

            

        return dfs(root, float('-inf'), float('inf'))
        