class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dictt=dict()
        m=len(arr)/4
        for i in arr:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i]=1
            if dictt[i]>m:
                    return i
       
            