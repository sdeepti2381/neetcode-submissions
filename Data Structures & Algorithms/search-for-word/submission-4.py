class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False
        seen = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, idx):
            nonlocal result

            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return 

            if board[r][c] != word[idx]:
                return 

            if board[r][c] == word[idx] and idx == len(word) - 1:
                result = True
                return

            if board[r][c] == word[idx]:
                seen.add((r, c))
                for i, j in directions:
                    nr, nc = r + i, c + j
                    if (nr, nc) not in seen:
                        dfs(nr, nc, idx + 1)
                        if result:
                            return True
                seen.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return result

            




        