class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=m+n-2
        r=n-1
        res=1
        for i in range(1,r+1):
            res=res*(N-r+i)//i
        return res     
        # def countpaths(i,j,m,n):
        #     if i>m or j>n:
        #         return 0
        #     if i==m-1 and j==n-1:
        #         return 1
        #     else:
        #         return countpaths(i+1,j,m,n)+countpaths(i,j+1,m,n)
        # return countpaths(0,0,m,n)