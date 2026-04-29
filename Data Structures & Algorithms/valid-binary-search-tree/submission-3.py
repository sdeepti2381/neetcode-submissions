# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = float("-inf")
        upper = float("inf")
        return self.isValidBSTCheckBounds(root, lower, upper)
    
    def isValidBSTCheckBounds(self, root: Optional[TreeNode], lower, upper) -> bool:
        if not root:
            return True
        if not (lower < root.val < upper):
            return False
        return self.isValidBSTCheckBounds(root.left, lower, root.val) and self.isValidBSTCheckBounds(root.right, root.val, upper)

        