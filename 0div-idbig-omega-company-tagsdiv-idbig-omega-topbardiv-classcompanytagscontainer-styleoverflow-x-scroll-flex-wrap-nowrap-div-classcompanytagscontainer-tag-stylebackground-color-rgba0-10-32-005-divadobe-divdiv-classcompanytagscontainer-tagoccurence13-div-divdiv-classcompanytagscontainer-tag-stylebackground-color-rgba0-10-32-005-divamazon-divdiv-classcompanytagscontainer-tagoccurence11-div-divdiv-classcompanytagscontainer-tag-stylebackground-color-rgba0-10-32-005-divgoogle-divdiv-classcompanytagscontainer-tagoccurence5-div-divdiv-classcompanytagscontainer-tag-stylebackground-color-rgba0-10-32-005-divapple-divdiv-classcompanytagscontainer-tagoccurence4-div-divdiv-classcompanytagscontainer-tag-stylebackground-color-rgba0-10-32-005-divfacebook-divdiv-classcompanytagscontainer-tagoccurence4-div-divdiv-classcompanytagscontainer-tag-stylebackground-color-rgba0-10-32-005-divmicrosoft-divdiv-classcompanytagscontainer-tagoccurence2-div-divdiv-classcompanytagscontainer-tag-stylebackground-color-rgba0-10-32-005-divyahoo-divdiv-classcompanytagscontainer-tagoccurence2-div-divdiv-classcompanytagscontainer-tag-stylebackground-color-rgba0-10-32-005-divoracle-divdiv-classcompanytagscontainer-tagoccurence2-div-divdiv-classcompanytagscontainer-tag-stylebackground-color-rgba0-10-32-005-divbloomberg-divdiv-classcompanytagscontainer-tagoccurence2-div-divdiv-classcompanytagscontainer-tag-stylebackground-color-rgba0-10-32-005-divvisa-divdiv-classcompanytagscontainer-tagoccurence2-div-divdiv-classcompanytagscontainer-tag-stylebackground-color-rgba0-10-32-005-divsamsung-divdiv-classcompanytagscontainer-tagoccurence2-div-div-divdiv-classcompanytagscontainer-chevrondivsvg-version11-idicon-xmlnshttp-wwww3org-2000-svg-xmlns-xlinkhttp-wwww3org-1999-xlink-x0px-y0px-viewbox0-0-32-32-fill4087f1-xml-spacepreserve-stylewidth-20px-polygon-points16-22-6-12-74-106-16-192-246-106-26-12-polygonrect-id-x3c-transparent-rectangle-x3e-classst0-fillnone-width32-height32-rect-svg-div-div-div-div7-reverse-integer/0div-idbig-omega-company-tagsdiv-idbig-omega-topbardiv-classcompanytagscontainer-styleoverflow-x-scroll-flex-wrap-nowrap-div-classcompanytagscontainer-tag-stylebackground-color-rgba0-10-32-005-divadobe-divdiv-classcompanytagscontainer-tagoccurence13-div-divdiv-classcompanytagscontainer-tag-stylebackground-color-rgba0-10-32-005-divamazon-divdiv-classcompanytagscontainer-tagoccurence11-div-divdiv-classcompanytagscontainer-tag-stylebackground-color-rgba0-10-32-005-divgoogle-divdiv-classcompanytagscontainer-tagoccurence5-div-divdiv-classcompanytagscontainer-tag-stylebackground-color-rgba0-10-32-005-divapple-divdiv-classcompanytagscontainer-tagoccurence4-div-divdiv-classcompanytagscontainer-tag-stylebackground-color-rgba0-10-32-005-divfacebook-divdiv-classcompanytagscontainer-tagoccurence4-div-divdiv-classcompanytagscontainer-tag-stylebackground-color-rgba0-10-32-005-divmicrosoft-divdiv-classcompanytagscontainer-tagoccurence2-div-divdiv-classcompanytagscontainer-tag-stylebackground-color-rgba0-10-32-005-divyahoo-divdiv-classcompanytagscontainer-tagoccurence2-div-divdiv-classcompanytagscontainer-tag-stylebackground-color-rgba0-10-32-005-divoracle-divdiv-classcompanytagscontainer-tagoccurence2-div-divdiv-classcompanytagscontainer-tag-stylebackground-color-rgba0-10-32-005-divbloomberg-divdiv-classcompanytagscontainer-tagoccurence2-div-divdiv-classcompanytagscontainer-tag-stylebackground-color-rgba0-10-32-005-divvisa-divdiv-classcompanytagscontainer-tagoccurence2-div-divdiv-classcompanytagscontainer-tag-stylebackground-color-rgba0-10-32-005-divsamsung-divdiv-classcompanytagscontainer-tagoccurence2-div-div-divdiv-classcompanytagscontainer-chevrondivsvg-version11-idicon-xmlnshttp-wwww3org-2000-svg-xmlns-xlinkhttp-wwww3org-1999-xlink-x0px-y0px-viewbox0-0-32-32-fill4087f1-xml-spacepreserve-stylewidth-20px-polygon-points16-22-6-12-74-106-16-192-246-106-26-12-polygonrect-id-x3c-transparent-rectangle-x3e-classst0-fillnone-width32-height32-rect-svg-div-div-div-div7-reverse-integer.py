class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        negative=1
        res=0
        MinInt=-2**31
        MaxInt=2**31-1
        for i in range(len(x)-1,-1,-1):
            if x[i]=="-":
                negative=-1
                continue
            res=res*10+int(x[i])
        res=res*negative
        if res<MinInt or res >MaxInt:
            return 0
        return res
            