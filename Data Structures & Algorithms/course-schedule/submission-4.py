class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node):
            if node in safe:
                return True 
            if node in visiting:
                return False

            visiting.add(node)

            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            safe.add(node)
            return True 
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visiting = set()
        safe = set()

        # perform DFS on the graph. If we hit a cycle, then we can not
        # take all the courses.
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True 

            
            
        



            
            
            

            


        