class Solution:
    def numberOfSteps(self, num: int) -> int:

        def rec(n,i):
            if n==0:
                return i
            if n%2==0:
                n=n//2
                
            else:
                n=n-1
            i=i+1
            return rec(n,i)
        return rec(num,0)
                
                
            
        