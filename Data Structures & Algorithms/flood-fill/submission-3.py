class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(r:int, c:int, originalColor:int):
            if r >= len(image) or c >= len(image[0]) or r < 0 or c < 0 or image[r][c] != originalColor or (r,c) in visited:
                return 
            visited.add((r,c))
            image[r][c] = color
            dfs(r + 1, c, originalColor)
            dfs(r - 1, c, originalColor)
            dfs(r, c + 1, originalColor)
            dfs(r, c - 1, originalColor)
            
        originalColor = image[sr][sc]
        visited = set()
        dfs(sr, sc, originalColor)

        return image


    

            



            
        