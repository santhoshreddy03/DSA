class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rows,cols=len(matrix),len(matrix[0])
        row=[]
        col=[]

        for r in range(rows):
            minn=float("inf")
            for c in range(cols):
                minn=min(minn,matrix[r][c])
                
            row.append(minn)
        for c in range(cols):
            maxx=float("-inf")
            for r in range(rows):
                maxx=max(maxx,matrix[r][c])
                
            col.append(maxx)
        for i in row:
            if i in col:
                return [i]
                