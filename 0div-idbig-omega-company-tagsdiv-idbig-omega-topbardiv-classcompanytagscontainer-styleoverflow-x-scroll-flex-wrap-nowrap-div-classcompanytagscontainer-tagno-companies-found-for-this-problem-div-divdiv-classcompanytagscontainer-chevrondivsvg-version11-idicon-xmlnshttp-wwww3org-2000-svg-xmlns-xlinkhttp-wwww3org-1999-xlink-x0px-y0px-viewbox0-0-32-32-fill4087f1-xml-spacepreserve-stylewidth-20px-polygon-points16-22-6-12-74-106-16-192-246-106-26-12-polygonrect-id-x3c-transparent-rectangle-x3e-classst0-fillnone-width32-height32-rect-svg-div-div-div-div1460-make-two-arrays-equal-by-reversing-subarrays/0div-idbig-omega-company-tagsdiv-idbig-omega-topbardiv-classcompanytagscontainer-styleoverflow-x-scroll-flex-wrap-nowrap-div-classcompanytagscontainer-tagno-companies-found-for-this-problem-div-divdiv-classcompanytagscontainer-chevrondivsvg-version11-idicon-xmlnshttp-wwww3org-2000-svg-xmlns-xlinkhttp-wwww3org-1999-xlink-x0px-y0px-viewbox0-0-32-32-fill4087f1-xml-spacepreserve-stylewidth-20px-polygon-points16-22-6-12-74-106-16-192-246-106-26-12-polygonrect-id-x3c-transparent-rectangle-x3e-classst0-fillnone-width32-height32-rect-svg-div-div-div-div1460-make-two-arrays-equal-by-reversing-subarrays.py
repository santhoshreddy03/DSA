class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tar={}
        ar={}
        for i in target:
            if i in tar:
                
                tar[i]+=1
            else:
                tar[i]=1
        for i in arr:
            if i in ar:
                
                ar[i]+=1
            else:
                ar[i]=1
        return tar==ar