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
            visiting = set()
            visiting.add(node)
            if not self.dfs(node, visiting, adjList):
                return False
        return True 


    def dfs(self, node, visiting, adjList):
        for nei in adjList[node]:
            if nei in visiting:
                return False
            else:
                visiting.add(nei)
                if not self.dfs(nei, visiting, adjList):
                    return False
            visiting.remove(nei)
        return True 

            
            
        



            
            
            

            


        