class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #if target > max in row, go to next row
        #bst on the row
        
        r = 0

        while r < len(matrix) and target > matrix[r][-1]:
            r += 1
        
        if r >= len(matrix):
            return False
        if target > matrix[r][-1]:
            return False
        if target < matrix[r][0]:
            return False
        
        left = 0
        right = len(matrix[r]) - 1

        while left <= right:
            m = left + ((right - left) // 2)

            if target == matrix[r][m]:
                return True
            elif target < matrix[r][m]:
               right = m - 1
            else:
                left = m + 1
        
        return False
