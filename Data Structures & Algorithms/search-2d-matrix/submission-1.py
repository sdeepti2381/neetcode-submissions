class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for r in range(len(matrix)):
            if target >= matrix[r][0] and target <= matrix[r][-1]:
                i, j = 0, len(matrix[r])
                while i <= j:
                    mid = (i + j) // 2
                    if matrix[r][mid] == target:
                        return True
                    elif matrix[r][mid] > target:
                        j = mid - 1
                    elif matrix[r][mid] < target:
                        i = mid + 1
                # for c in range(len(matrix[r])):
                #     if matrix[r][c] == target:
                #         return True 

        return False