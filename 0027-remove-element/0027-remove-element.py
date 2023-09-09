class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result=nums[:]
        for i in nums:
            if i==val:
                result.remove(i)
            
        nums[0:len(result)]=result
        return len(result)
                
        