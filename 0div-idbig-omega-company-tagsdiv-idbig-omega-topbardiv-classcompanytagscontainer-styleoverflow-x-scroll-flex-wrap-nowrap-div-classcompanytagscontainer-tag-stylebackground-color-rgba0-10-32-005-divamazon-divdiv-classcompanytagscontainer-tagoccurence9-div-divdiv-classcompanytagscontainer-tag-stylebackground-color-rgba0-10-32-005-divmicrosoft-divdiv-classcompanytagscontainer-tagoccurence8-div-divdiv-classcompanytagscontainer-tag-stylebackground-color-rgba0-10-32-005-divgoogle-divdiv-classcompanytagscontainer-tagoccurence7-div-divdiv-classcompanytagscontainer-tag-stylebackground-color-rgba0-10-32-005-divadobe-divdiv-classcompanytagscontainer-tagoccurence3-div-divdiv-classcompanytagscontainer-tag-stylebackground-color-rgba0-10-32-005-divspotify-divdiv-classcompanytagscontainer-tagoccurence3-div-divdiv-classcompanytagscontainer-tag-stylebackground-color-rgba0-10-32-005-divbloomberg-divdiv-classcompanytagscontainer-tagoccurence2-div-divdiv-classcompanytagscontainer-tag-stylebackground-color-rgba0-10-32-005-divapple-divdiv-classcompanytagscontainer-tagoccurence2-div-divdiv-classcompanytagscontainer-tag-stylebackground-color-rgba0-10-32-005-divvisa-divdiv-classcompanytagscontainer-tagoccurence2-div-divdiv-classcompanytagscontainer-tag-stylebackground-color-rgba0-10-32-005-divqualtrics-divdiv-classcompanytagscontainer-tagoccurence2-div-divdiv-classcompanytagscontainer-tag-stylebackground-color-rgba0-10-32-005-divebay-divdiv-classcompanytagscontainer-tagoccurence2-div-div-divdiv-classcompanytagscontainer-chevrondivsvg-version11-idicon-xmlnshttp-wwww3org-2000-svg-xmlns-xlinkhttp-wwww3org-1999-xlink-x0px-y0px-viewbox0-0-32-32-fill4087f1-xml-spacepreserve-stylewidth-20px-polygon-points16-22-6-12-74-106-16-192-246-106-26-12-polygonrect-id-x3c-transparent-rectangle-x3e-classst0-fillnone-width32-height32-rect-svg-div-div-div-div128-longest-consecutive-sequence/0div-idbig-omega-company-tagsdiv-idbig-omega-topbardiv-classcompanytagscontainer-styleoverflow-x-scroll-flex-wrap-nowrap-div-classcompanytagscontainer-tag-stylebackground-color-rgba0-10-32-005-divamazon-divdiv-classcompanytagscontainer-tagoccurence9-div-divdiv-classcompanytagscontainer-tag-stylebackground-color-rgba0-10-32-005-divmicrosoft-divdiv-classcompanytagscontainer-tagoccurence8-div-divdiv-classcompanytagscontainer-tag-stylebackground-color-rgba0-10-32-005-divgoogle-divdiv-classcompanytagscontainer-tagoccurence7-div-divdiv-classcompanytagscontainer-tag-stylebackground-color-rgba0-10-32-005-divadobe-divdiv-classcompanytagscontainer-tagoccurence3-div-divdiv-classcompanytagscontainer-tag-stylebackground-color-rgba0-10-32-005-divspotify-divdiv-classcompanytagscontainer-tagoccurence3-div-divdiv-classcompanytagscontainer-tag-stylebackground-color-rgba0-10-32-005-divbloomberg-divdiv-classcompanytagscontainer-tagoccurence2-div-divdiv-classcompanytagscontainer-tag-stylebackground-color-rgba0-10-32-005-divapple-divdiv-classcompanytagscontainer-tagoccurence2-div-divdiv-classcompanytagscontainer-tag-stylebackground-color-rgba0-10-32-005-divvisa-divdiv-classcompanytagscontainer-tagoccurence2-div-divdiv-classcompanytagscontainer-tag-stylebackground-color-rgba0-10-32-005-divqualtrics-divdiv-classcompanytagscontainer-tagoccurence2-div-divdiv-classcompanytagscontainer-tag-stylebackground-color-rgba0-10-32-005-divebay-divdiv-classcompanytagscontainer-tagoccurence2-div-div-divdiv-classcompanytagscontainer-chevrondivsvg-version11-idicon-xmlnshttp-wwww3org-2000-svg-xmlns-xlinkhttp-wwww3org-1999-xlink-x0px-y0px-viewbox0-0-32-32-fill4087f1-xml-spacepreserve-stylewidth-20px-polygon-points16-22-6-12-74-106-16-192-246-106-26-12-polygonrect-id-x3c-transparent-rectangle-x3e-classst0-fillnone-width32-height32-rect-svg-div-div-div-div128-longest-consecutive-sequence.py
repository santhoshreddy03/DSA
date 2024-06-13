class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#         hashset=set()
#         res=0
#         for i in range(len(nums)):
#             if nums[i] not in hashset:
#                 hashset.add(nums[i])
#         for i in hashset:
#             if i-1 not in hashset:
#                 c=1
#                 while i+1 in hashset:
#                     i+=1
#                     c+=1
#                 res=max(c,res)
#         return res
        
        
               
        
        
        nums.sort()
        res=0
        c=1
        if len(nums)==1:
            return 1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                c+=1
            elif nums[i]+1!=nums[i+1] and nums[i]!=nums[i+1]:
                c=1
            res=max(c,res)
        return res
        