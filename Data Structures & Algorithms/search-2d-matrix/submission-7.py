class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #while target is larger than last in row, next row
        #bs in row
        #if not in row, dne
        r = 0

        while r < len(matrix) and matrix[r][-1] < target:
            r += 1
        
        if r >= len(matrix):
            return False
        
        left = 0
        right = len(matrix[r]) - 1

        while left <= right:
            m = (right + left) // 2

            if matrix[r][m] == target:
                return True
            elif matrix[r][m] > target:
                right = m - 1
            else:
                left = m + 1
            
        return False        
