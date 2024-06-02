class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    for m in range(len(matrix[0])):
                        if matrix[i][m]!=0:
                            
                            matrix[i][m]=565
                    for k in range(len(matrix)):
                        if matrix[k][j]!=0:
                            matrix[k][j]=565
                            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==565:
                    matrix[i][j]=0

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         x=matrix
#         for i in range(len(x)):
#             for j in range(len(x[0])):
#                 if x[i][j]==0:
#                     for m in range(len(x[0])):
#                         matrix[i][m]=0
#                     for k in range(len(x)):
#                         matrix[k][j]=0


                    