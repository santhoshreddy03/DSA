class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=1
        res=0
        if len(nums)==1 and nums[0]==1:
            return 1
        if sum(nums)==0:
            return 0
        for i in range(len(nums)-1):
            if nums[i]==1 and nums[i+1]==nums[i]:
                c+=1
            
            else:
                c=1
            res=max(res,c)
        return res
                
        