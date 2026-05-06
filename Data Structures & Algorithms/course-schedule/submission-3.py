class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(node):
            for nei in adjList[node]:
                if nei in safe:
                    continue
                if nei in visiting:
                    return False
                else:
                    visiting.add(nei)
                    if not dfs(nei):
                        return False
                    visiting.remove(nei)
                safe.add(nei)
            return True 
        
        adjList = defaultdict(list)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        visiting = set()
        safe = set()

        # perform DFS on the graph. If we hit a cycle, then we can not
        # take all the courses.
        for course in range(numCourses):
            visiting.add(course)
            if not dfs(course):
                return False
            visiting.remove(course)
            safe.add(course)
            
        return True 

            
            
        



            
            
            

            


        