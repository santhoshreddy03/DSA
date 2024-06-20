class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        res=[]

        for i in range(len(x)-1,-1,-1):
            res.append(x[i])
        return " ".join(res)
        
            