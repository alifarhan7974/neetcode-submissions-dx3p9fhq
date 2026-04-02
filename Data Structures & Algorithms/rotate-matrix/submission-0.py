class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Rotate Steps: 
        # 1) Transpose a matrix 
        # 2) Reverse the rows 
        n = len(matrix)
        
        for i in range(n): 
            for j in range(i, n): 
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix: 
            row.reverse() 
