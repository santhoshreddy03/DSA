class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        m1=0
        m2=0
        for i in range(len(nums)):
            if nums[i]>=m1:
                m2=m1
                m1=nums[i]
            elif nums[i]>=m2:
                m2=nums[i]
                
            
                
        return (m2-1) * (m1-1)
                
        
        