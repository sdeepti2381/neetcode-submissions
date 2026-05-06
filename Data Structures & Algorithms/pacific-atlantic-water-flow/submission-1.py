class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS = len(heights)
        COLS = len(heights[-1])
        
        def dfs(r, c, visited):
            reaches_pacific = False
            reaches_atlantic = False

            if r == 0 or c == 0:
                reaches_pacific = True
            if r == len(heights) - 1 or c == len(heights[0]) - 1:
                reaches_atlantic = True
            if reaches_pacific and reaches_atlantic:
                return True, True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                    visited.add((r, c))
                    child_pacific, child_atlantic = dfs(nr, nc, visited)
                    reaches_pacific = reaches_pacific or child_pacific 
                    reaches_atlantic = reaches_atlantic or child_atlantic
        
            return reaches_pacific , reaches_atlantic 
    
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                visited = set()
                reaches_pacific, reaches_atlantic = dfs(r, c, visited)
                if reaches_pacific and reaches_atlantic:
                    result.append([r, c])
        
        return result
        
            
            

        