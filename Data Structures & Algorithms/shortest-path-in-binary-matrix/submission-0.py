class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        levels = 0
        visited = set((0,0))
        queue = deque()
        queue.append((0,0))
        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

        while queue:
            for _ in range(len(queue)):
                cr, cc = queue.popleft()
                if (cr, cc) == (len(grid) - 1, len(grid[0]) - 1):
                    return levels + 1
                for dr,dc in directions:
                    (nr,nc) = (dr + cr, dc + cc)
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            levels += 1
        

        return -1 
        