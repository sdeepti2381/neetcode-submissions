# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        detectedMatches = []

        # detect potential match 
        def findSubtree(node, detectedMatches):
            if not node:
                return
            
            if node.val == subRoot.val:
                detectedMatches.append(node)
            
            findSubtree(node.left, detectedMatches)
            findSubtree(node.right, detectedMatches)
        
        findSubtree(root, detectedMatches)

        print(detectedMatches)

        def checkIfTreesMatch(node1, node2) -> bool:
            if (not node1 and node2) or (not node2 and node1):
                return False
            if not node1 and not node2:
                return True
            if node1.val != node2.val:
                return False
            if node1.val == node2.val:
                return checkIfTreesMatch(node1.left, node2.left) and checkIfTreesMatch(node1.right, node2.right)
        
        for matchDetected in detectedMatches:
            if checkIfTreesMatch(matchDetected, subRoot):
                return True

        return False


                