class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # to get indexes 
        # To get row // by rows 
        # to get col % row len 
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1 

        while left <= right: 
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols

            if target < matrix[r][c]: 
                right = mid - 1 

            elif target > matrix[r][c]:
                left = mid + 1 

            else: 
                return True 


        return False 
            
