class Solution:
    def myAtoi(self, s: str) -> int:
        i=0
        res=0
        negative=1
        MaxInt=2**31-1
        MinInt=-2**31
        while i<len(s) and s[i]==" ":
            i+=1
        if i<len(s) and s[i]=="-":
            negative=-1
            i+=1
        if i<len(s) and s[i]=="+" and negative==-1:
            return 0
        if i<len(s) and s[i]=="+":
            i+=1
        checker=set("0123456789")
        while i<len(s) and s[i] in checker:
            res=res*10+int(s[i])
            i+=1
        res=res*negative
        if res <0:
            return max(res,MinInt)
        else:
            return min(res,MaxInt)
        
        