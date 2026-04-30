class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        noFreshOranges = True

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    noFreshOranges = False
        
        if noFreshOranges:
            return 0

        
        if len(queue) == 0:
            return -1 

        while queue:
            
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        grid[nr][nc] = 2
            if queue:
                minutes += 1
            
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1 
        
        return minutes
        








        