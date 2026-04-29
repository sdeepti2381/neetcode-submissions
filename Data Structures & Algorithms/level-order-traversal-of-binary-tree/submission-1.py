# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        levels = defaultdict(list)
        queue = deque()
        level = 0
        queue.append((root, level))
        
        while len(queue) > 0:
            node, level = queue.popleft()
            if node:
                levels[level].append(node.val)
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        
        return list(levels.values())



        
        