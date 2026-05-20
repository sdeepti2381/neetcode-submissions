class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(r, c, idx):

            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0:
                return False

            if board[r][c] != word[idx]:
                return False

            if board[r][c] == word[idx] and idx == len(word) - 1:
                return True

            if board[r][c] == word[idx]:
                seen.add((r, c))
                for i, j in directions:
                    nr, nc = r + i, c + j
                    if (nr, nc) not in seen:
                        if dfs(nr, nc, idx + 1):
                            return True
                seen.remove((r, c))
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False

            




        