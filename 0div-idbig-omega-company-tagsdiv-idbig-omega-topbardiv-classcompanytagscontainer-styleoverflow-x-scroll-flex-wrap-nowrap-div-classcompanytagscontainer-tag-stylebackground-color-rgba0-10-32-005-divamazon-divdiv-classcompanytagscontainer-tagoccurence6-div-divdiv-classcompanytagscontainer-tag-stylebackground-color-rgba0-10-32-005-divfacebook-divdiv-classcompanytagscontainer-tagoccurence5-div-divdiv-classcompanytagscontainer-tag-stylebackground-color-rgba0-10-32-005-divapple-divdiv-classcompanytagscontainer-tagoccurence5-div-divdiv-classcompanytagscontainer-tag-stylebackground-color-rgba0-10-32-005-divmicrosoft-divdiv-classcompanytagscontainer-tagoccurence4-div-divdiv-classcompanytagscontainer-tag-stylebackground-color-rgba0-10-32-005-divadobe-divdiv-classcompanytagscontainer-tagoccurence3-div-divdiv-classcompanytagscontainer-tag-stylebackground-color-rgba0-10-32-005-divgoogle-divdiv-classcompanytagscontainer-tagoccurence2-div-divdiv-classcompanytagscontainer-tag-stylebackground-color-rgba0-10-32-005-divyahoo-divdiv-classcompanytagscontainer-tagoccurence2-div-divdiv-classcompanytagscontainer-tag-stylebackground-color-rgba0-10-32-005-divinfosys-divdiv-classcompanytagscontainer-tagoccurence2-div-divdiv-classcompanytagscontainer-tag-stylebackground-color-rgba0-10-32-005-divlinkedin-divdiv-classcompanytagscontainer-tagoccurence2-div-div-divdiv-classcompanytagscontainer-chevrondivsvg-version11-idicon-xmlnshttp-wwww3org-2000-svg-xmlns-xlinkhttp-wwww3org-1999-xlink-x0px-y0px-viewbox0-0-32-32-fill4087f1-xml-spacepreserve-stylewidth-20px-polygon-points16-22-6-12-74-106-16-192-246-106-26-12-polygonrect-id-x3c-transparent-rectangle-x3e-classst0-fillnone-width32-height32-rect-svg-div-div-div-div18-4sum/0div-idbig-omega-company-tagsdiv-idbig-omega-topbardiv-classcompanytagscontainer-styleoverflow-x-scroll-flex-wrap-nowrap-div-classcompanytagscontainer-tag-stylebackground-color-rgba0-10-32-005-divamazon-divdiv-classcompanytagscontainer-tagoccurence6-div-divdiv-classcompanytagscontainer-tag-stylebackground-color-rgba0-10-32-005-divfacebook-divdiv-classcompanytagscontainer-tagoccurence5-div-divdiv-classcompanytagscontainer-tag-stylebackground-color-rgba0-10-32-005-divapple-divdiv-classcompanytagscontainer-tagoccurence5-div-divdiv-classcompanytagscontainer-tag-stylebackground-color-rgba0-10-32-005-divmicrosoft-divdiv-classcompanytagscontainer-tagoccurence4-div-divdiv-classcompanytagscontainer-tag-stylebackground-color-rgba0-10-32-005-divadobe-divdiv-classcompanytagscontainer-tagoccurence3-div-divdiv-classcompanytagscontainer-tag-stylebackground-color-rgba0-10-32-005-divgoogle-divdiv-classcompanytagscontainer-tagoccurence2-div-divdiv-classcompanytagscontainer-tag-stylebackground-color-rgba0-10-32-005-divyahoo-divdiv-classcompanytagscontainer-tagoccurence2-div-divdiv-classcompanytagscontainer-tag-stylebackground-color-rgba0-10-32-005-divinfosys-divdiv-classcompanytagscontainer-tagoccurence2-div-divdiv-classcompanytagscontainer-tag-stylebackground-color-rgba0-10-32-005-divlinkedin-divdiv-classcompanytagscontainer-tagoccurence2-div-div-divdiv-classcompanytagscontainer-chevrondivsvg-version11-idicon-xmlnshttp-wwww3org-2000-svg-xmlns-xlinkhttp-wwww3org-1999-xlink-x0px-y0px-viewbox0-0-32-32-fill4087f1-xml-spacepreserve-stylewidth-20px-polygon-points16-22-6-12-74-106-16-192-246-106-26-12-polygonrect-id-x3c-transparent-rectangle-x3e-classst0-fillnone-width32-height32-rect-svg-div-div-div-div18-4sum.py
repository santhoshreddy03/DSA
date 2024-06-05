class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                l,r=j+1,len(nums)-1
                while l<r:
                    sum=nums[i]+nums[j]+nums[l]+nums[r]
                    if sum==target:
                        res=[nums[i],nums[j],nums[l],nums[r]]
                        if res not in out:
                            out.append(res)
                            l+=1
                            r-=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                    elif sum>target:
                        r-=1
                    else:
                        l+=1
        return out
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#         out=[]
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 hash=set()
#                 for k in range(j+1,len(nums)):
#                     a=target-(nums[i]+nums[j]+nums[k])
#                     if a in hash:
#                         res=[a,nums[i],nums[j],nums[k]]
#                         res.sort()
#                         if res not in out:
#                             out.append(res)
                    
#                     hash.add(nums[k])
#         return out
                        
                    
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        