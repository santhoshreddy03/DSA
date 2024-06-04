class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ele=None
        for i in range(len(nums)):
            if cnt==0:
                cnt=1
                ele=nums[i]
            elif nums[i]==ele:
                cnt+=1
            else:
                cnt-=1
                
        return ele
                
        
        
        
        
        
        
        
        
        
        return False#         hashset={}
#         for i in range(len(nums)):
#             if nums[i] in hashset:
#                 hashset[nums[i]]+=1
#             else:
#                 hashset[nums[i]]=1
#         c=0
#         k=0
#         for i in hashset:
#             if hashset[i]>c:
                
#                 c=hashset[i]
#                 k=i
#         return k
            
        