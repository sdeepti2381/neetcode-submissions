class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c) -> int:
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        largestIsland = float("-inf")
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                largestIsland = max(largestIsland, dfs(r, c))
        
        return largestIsland

        
        