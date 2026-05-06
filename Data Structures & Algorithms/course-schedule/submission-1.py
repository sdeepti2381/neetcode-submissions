class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adjList = defaultdict(list)
        for src, dst in prerequisites:
            adjList[src].append(dst)
            if dst not in adjList:
                adjList[dst] = []

        # perform DFS on the graph. If we hit a cycle, then we can not
        # take all the courses.
        
        for node in adjList:
            visited = set()
            visited.add(node)
            if not self.dfs(node, visited, adjList):
                return False
        return True 


    def dfs(self, node, visited, adjList):
        for nei in adjList[node]:
            if nei in visited:
                return False
            else:
                visited.add(nei)
                if not self.dfs(nei, visited, adjList):
                    return False
            visited.remove(nei)
        return True 

            
            
        



            
            
            

            


        