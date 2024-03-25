class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a=len(nums)
        for i in range(a):
            nums.append(nums[i])
            
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         ans=[]
#         for i in range(2):
#             for i in range(len(nums)):
#                 ans.append(nums[i])
                
#         return ans
                
        