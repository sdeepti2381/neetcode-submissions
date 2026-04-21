class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            if target >= matrix[r][0] and target <= matrix[r][-1]:
                for c in range(len(matrix[r])):
                    if matrix[r][c] == target:
                        return True 

        return False