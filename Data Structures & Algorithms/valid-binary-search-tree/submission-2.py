# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upper = float("inf")
        lower = float("-inf")
        return self.isValidBSTCheckBounds(root, upper, lower)
    
    def isValidBSTCheckBounds(self, root: Optional[TreeNode], upper, lower) -> bool:
        if not root:
            return True
        if not (lower < root.val < upper):
            return False
        return self.isValidBSTCheckBounds(root.left, root.val, lower) and self.isValidBSTCheckBounds(root.right, upper, root.val)

        