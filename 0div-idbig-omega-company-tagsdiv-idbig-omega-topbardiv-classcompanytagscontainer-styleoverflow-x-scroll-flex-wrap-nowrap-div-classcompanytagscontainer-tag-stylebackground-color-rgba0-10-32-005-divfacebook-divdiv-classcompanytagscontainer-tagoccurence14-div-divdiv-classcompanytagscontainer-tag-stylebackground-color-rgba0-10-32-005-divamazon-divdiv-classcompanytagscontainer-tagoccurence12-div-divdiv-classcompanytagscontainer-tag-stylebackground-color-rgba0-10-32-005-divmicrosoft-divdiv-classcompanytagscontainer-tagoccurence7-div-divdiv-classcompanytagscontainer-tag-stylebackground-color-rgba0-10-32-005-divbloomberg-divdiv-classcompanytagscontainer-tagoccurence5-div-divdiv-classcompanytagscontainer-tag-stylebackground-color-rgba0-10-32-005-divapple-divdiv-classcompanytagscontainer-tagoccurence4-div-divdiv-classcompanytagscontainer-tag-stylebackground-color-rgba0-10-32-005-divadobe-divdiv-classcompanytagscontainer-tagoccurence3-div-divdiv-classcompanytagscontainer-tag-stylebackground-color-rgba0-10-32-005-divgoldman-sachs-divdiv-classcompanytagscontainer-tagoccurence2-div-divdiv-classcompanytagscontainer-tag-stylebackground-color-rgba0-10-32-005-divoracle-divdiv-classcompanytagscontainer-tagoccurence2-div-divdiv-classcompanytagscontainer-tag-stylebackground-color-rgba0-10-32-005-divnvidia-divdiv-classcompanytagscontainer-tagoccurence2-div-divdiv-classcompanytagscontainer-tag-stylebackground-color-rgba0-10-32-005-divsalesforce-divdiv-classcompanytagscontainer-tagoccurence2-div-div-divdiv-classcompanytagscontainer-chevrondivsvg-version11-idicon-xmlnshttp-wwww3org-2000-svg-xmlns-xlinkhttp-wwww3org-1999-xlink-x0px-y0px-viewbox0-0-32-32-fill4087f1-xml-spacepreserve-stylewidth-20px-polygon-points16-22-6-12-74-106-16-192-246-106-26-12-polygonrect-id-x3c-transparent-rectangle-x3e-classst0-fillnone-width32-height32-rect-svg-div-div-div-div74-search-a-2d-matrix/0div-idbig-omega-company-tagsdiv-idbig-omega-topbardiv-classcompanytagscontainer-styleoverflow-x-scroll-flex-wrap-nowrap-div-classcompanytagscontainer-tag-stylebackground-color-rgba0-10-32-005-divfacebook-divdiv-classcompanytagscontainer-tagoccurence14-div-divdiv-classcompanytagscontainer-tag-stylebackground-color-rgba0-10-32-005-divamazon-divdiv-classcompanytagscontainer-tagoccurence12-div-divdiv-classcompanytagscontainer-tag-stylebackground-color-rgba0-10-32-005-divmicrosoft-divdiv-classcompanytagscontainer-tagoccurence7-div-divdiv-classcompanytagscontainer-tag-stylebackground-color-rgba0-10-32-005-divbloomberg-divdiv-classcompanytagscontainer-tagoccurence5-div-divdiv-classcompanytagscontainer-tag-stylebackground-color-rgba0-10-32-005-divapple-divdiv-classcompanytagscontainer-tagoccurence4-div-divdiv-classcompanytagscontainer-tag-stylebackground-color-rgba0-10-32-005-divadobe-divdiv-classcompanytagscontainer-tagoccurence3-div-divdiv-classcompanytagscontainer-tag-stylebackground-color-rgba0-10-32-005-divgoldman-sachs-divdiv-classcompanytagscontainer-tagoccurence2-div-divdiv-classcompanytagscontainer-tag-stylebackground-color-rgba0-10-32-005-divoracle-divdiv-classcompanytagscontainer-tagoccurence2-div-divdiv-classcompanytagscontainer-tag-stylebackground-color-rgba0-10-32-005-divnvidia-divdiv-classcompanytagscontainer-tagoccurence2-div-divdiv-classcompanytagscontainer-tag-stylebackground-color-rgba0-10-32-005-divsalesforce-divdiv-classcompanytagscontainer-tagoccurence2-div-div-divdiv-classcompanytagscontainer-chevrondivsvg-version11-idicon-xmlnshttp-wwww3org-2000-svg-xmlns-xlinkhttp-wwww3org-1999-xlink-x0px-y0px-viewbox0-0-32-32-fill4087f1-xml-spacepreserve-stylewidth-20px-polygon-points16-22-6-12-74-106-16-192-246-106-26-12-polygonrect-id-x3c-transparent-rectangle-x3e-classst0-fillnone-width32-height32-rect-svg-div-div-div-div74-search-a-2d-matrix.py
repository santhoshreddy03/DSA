class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # l,r=0,len(matrix)*len(matrix[0])-1
        # while l<=r:
        #     m=(l+r)//2
        #     if matrix[m//len(matrix[0])][m%len(matrix[0])]==target:
        #         return True
        #     elif matrix[m//len(matrix[0])][m%len(matrix[0])]>=target:
        #         r=m-1
        #     else:
        #         l=m+1
        # return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j]==target:
#                     return True
#         return False
        