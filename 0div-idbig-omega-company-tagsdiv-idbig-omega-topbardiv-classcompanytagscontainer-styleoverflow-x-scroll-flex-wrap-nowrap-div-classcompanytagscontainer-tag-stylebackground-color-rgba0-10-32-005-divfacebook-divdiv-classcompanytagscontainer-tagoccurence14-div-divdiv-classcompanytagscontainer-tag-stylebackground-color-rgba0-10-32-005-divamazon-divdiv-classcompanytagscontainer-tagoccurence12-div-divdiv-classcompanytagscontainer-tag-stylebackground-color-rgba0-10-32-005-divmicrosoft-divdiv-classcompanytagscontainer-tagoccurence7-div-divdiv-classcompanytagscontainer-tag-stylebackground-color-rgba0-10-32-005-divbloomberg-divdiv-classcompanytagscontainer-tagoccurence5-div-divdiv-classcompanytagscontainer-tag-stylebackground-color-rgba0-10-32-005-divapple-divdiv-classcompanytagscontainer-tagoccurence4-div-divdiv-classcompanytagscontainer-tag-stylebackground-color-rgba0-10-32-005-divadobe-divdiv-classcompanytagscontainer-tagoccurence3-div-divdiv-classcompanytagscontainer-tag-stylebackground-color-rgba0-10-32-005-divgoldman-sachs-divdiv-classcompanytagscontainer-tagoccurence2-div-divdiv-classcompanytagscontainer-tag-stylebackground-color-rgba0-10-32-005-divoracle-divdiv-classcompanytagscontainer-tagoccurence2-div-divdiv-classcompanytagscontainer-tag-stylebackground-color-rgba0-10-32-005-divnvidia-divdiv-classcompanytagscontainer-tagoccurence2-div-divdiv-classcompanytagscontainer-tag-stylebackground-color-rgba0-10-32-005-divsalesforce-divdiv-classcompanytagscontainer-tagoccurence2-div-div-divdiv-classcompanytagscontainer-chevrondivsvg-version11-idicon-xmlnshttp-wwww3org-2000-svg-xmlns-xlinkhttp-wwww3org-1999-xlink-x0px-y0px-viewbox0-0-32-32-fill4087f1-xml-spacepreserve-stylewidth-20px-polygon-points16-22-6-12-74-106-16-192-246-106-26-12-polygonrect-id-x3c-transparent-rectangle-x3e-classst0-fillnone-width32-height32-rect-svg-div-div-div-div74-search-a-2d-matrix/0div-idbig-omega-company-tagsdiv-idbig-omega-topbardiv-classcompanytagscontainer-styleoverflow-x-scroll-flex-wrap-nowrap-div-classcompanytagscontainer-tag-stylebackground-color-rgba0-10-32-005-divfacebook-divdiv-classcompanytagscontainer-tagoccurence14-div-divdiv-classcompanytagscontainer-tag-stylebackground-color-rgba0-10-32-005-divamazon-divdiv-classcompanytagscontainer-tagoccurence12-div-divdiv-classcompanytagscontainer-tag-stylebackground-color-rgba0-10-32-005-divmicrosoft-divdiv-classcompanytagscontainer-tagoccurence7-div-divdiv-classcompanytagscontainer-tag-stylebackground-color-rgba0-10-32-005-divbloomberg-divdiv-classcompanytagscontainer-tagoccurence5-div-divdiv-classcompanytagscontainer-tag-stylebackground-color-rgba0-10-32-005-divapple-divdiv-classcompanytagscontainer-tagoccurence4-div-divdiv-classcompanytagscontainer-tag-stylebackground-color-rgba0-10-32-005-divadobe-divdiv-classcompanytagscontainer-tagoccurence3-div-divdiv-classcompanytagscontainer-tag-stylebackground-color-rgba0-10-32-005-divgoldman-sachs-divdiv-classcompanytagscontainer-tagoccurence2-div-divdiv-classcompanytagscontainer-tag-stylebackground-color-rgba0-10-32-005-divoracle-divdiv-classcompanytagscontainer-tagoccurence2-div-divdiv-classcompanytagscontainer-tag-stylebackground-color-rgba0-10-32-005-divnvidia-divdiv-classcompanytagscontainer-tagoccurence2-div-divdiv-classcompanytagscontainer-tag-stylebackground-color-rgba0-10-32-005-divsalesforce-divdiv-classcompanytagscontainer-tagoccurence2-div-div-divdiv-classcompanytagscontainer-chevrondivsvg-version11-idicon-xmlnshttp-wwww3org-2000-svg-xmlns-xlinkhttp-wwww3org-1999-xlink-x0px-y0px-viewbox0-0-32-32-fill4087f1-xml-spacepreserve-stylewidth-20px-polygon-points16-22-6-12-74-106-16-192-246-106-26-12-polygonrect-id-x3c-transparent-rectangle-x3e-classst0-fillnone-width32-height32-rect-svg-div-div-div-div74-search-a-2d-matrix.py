class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target<=matrix[i][-1] and target>=matrix[i][0]:
                l,r=0,len(matrix[i])
                while l<=r:
                    m=(l+r)//2
                    if target==matrix[i][m]:
                        return True
                    if target>matrix[i][m]:
                        l=m+1
                    else:
                        r=m-1
        return False
        
        
        
        
        
        # for i in range(len(matrix)):
        #     if target<=matrix[i][-1] and target>=matrix[i][0]:
        #         for j in range(len(matrix[i])):
        #             if target==matrix[i][j]:
        #                 return True
        # return False
        
        
        
        
        
        
        
        
        
        
        
        # l,r=0,len(matrix)
        # while l<=r:
        #     m=(l+r)//2
        #     s,e=0,len(matrix[m])
        #     n=(s+e)//2
        #     if martrix[m][n]==target:
        #         return True
        #     elif matrix[m][n]>target

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==target:
#                     return True
#         return False
        