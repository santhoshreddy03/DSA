class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dictt=dict()
        for i in arr:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
        m=len(arr)/4
        for i in dictt:
            if dictt[i]>m:
                return i
            