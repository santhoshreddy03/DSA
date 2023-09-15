class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,maxcount=0,0
        dict={}
        c=0
        for i in nums:
            dict[i]= dict.get(i,0)+1
            if dict[i]>maxcount:
                res=i
                maxcount=dict[i]
        return res
                
  
