class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
       # iterate through rows
       for r in board:
        seen = set()
        for c in r:
            if c == ".":
                continue
            if c in seen:
                return False
            seen.add(c)
                

       # iterate through columns
       for c in range(len(board)):
        seen = set()
        for r in range(len(board)):
            if board[r][c] == ".":
                continue
            if board[r][c] in seen:
                return False
            seen.add(board[r][c])

       # iterate by boxes
       seen = defaultdict(set)
       for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == ".":
                continue
            box = (r//3, c//3)
            if board[r][c] in seen[box]:
                return False
            seen[box].add(board[r][c])

        
        

       return True
        