class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visit=set()
        count=0
        maxi=0
        def dfs(r,c):
            nonlocal count
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            count+=1
            directions=[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in directions:
                dfs(r+dr,c+dc)
            return count
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c]==1:
                    count=0
                    maxi=max(dfs(r,c),maxi)
          
        return maxi