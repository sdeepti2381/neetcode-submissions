class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        i = 0 
        j = len(matrix) - 1
        targetRow = -1

        # find the row to search
        while i <= j:
            mid = (i + j) // 2
            if target == matrix[mid][0]:
                return True
            elif target > matrix[mid][0] and target <= matrix[mid][-1]:
                targetRow = mid
                break
            elif target < matrix[mid][0]:
                j = mid - 1
            elif target > matrix[mid][-1]:
                i = mid + 1
        
        if targetRow == -1:
            return False

        # find the target in the target row
        i = 0
        j = len(matrix[targetRow]) - 1
        while i <= j:
            mid = (i + j) // 2
            if matrix[targetRow][mid] == target:
                return True
            elif target > matrix[targetRow][mid]:
                i = mid + 1
            else:
                j = mid - 1 
        
        if i > j:
            return False




                
