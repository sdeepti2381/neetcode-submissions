class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(r, c):
            if r >= len(image) or c >= len(image[0]) or r < 0 or c < 0 or image[r][c] == color or image[r][c] != originalColor:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        originalColor = image[sr][sc]
        dfs(sr, sc)

        return image
        
        
         
