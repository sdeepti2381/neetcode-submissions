"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        old_to_new = {}

        self.dfs(node, old_to_new)

        for curr,clone in old_to_new.items():
            for nei in curr.neighbors:
                clone.neighbors.append(old_to_new[nei])
        
        return old_to_new[node]

    def dfs(self, node, old_to_new):
        if node in old_to_new:
            return 
        old_to_new[node] = Node(node.val)
        for nei in node.neighbors:
            self.dfs(nei, old_to_new)
        



        
        
        

        

    

        
        


        
        