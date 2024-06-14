class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt,maxi=0,0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            maxi=max(maxi,cnt)
        return maxi
    
    
    
    
    
#         c=1
#         res=0
#         if len(nums)==1 and nums[0]==1:
#             return 1
#         if sum(nums)==0:
#             return 0
#         for i in range(len(nums)-1):
#             if nums[i]==1 and nums[i+1]==nums[i]:
#                 c+=1
            
#             else:
#                 c=1
#             res=max(res,c)
#         return res
                
        