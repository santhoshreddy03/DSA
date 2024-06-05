class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        out=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                hash=set()
                for k in range(j+1,len(nums)):
                    a=target-(nums[i]+nums[j]+nums[k])
                    if a in hash:
                        res=[a,nums[i],nums[j],nums[k]]
                        res.sort()
                        if res not in out:
                            out.append(res)
                    
                    hash.add(nums[k])
        return out
                        
                    
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         output=[]
#         res=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 for k in range(j+1,len(nums)):
#                     for l in range(k+1,len(nums)):
#                         sum=nums[i]+nums[j]+nums[k]+nums[l]
#                         if sum==target:
#                             res=[nums[i],nums[j],nums[k],nums[l]]
#                             res.sort()
#                             if res not in output:

#                                 output.append(res)
#         return output
        