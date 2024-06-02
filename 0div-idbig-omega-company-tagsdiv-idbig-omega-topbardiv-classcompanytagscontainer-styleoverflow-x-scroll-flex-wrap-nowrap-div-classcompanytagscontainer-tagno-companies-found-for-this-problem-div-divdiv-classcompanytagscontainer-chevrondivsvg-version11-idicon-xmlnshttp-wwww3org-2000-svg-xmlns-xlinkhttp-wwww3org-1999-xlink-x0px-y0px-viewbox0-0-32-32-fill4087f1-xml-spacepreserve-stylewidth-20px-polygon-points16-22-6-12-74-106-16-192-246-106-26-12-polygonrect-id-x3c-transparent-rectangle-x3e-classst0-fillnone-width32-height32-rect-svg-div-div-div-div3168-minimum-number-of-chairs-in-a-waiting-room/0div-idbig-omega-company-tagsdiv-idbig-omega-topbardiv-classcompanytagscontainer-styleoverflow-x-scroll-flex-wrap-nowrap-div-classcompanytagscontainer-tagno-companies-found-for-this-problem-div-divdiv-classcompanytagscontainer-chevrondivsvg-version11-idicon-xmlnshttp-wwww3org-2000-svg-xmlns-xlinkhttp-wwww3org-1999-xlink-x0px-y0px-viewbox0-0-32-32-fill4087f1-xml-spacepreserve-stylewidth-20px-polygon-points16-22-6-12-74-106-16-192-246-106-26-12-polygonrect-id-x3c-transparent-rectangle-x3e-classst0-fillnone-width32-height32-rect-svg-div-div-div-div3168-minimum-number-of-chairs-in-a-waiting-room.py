class Solution:
    def minimumChairs(self, s: str) -> int:
        sum=0
        maxi=float("-inf")
        for i in range(len(s)):
            if s[i]=="E":
                sum+=1
            else:
                sum-=1
            maxi=max(maxi,sum)
        return maxi
                