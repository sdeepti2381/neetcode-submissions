class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        if len(edges) == 0:
            return True
        
        adjList = defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        

        def dfs(parent, node, visited):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjList[node]:    
                if nei == parent:
                    continue
                if not dfs(node, nei, visited):
                    return False
            return True
        
        for node in adjList:
            if not dfs(node, adjList[node][0], set()):
                return False
        
        return True

        
        