class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c) -> int:
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == "0":
                return 0
            else:
                grid[r][c] = "0"
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
            

        islands = 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[r])):
                islandSize = dfs(r, c)
                if islandSize > 0:
                    islands += 1
        
        return islands


        