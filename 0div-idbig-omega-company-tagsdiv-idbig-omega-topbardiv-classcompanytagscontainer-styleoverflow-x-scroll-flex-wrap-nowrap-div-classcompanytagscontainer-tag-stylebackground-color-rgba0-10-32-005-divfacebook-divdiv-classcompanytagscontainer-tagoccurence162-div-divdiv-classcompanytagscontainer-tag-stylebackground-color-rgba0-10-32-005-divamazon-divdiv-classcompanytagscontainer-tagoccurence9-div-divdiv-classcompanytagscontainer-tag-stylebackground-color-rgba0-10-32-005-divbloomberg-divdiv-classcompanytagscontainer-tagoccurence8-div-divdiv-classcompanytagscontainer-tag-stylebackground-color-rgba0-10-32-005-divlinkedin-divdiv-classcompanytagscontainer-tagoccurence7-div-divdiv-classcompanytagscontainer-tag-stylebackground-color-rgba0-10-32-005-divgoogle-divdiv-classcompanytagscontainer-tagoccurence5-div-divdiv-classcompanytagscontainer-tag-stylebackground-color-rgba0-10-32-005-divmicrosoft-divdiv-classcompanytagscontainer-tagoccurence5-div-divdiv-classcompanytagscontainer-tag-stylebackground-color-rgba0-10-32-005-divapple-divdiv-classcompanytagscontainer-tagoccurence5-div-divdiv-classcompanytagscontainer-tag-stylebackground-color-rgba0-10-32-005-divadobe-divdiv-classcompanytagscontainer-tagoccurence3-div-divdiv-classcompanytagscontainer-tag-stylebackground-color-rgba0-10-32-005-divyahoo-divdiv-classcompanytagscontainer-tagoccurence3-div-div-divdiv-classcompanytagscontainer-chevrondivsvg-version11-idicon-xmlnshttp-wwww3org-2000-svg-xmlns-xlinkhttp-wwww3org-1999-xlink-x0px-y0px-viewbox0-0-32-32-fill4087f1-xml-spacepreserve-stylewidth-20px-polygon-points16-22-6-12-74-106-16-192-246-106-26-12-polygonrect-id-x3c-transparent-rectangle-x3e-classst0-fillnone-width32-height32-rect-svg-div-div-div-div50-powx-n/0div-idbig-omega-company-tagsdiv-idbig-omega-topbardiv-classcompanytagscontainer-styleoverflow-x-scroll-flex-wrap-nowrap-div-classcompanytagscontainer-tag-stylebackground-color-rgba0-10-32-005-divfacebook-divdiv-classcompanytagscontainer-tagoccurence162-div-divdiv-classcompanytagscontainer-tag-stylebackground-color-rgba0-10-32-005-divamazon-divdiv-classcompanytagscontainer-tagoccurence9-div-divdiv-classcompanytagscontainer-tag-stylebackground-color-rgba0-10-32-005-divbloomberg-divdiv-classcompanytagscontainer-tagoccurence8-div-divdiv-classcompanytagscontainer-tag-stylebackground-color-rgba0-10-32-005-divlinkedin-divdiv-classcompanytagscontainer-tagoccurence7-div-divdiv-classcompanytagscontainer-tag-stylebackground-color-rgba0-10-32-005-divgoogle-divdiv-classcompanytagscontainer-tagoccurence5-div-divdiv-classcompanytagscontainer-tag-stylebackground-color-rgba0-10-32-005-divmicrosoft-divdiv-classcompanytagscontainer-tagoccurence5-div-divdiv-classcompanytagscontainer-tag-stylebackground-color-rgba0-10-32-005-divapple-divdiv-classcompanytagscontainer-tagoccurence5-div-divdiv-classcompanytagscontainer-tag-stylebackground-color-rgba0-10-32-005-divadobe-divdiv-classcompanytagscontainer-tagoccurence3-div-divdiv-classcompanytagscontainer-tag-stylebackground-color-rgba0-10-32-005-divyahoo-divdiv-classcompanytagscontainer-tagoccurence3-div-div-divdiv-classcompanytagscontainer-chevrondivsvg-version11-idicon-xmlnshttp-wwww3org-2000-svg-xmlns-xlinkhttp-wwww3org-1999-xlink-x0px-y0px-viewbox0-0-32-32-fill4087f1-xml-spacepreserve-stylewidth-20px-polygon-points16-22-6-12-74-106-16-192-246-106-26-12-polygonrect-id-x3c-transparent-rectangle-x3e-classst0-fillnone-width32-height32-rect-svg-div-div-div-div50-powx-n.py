class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        a=n
        if n<0:
            n=-1*n
        while n:
            if n%2==0:
                x=x*x
                n=n/2
            else:
                ans=ans*x
                n-=1
        if a<0:
            ans=1/ans
        return ans
        