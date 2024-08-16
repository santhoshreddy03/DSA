class Solution:
    def hammingWeight(self, n: int) -> int:
        bina=bin(n)
        count=0
        for i in range(2,len(bina)):
            if bina[i]=="1":
                count+=1
                
        return count