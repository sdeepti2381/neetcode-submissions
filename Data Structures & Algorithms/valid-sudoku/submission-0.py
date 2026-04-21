class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        i = 0
        while i < len(board):
            j = 0
            while j < len(board[i]):
                if board[i][j] == ".":
                    j += 1
                    continue
                if board[i][j] in rows[i]:
                    return False
                else:
                    rows[i].add(board[i][j])
                
                if board[i][j] in cols[j]:
                    return False
                else:
                    cols[j].add(board[i][j])
                # box check
                box_x = i//3
                box_y = j//3
                if board[i][j] in boxes[(box_x,box_y)]:
                    return False
                else:
                    boxes[(box_x,box_y)].add(board[i][j])

                j += 1

            i += 1

        # valid sudoko board 
        return True








