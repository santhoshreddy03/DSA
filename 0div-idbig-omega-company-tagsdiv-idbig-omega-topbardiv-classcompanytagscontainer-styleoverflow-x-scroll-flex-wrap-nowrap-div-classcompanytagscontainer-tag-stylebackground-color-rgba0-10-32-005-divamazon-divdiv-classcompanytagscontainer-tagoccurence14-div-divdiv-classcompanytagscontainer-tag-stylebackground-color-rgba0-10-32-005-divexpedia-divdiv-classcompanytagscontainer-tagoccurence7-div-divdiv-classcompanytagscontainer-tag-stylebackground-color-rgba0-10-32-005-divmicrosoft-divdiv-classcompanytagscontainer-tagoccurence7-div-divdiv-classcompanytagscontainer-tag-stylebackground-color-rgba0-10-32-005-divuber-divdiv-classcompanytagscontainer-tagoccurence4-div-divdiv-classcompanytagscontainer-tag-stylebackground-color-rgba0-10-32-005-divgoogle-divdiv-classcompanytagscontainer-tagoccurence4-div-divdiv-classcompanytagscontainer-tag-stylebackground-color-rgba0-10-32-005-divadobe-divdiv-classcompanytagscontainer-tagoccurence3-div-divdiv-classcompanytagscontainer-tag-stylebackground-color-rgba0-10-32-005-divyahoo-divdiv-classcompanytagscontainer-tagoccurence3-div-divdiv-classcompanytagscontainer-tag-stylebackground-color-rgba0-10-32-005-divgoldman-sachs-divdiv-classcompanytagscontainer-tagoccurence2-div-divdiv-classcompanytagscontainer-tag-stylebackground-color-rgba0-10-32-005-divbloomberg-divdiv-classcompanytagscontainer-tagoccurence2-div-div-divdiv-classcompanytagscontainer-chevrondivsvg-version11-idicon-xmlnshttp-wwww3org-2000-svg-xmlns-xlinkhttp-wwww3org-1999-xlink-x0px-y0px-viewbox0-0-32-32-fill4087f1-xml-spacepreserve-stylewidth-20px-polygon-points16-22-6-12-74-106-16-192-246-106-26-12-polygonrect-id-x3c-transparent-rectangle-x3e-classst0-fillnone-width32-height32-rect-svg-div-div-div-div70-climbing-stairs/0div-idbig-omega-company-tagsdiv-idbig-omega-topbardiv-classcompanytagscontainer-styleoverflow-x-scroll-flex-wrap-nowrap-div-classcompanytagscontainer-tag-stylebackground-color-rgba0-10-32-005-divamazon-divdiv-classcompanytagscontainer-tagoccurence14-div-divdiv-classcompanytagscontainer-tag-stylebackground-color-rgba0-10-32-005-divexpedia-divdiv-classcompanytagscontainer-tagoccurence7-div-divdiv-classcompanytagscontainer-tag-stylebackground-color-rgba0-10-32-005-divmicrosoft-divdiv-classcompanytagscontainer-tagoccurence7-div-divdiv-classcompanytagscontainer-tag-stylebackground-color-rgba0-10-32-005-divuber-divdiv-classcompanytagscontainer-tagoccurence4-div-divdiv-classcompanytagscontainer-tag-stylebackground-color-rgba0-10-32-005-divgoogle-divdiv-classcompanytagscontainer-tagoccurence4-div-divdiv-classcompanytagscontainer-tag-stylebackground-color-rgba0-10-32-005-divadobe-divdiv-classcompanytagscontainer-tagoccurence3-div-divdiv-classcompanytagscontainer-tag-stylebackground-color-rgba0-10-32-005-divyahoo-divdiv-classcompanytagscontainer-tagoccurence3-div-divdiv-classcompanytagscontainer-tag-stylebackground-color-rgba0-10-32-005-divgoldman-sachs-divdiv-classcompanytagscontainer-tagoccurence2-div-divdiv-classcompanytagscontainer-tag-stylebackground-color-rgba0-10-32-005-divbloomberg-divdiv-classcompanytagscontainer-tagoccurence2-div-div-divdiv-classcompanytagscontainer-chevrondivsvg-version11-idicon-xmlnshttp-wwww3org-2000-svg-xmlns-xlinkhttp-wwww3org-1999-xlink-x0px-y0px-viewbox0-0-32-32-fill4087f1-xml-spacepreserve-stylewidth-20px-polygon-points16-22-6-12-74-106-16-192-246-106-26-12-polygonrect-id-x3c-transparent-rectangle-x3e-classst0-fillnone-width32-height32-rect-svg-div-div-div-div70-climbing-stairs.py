class Solution:
    def climbStairs(self, n: int) -> int:
        dpp=[-1] * (n+1)
        print(dpp)
        def dp(n,dpp):
            if n==1 or n==0:
                return 1
            if dpp[n]!=-1:
                return dpp[n]
            dpp[n]=dp(n-1,dpp)+dp(n-2,dpp)
            return dpp[n]
        
        return dp(n,dpp)