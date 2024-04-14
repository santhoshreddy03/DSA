class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum=0
        for i in range(1,n+1):
            sum=sum+i
            if sum>n:
                return i-1
            elif sum==n:
                return i