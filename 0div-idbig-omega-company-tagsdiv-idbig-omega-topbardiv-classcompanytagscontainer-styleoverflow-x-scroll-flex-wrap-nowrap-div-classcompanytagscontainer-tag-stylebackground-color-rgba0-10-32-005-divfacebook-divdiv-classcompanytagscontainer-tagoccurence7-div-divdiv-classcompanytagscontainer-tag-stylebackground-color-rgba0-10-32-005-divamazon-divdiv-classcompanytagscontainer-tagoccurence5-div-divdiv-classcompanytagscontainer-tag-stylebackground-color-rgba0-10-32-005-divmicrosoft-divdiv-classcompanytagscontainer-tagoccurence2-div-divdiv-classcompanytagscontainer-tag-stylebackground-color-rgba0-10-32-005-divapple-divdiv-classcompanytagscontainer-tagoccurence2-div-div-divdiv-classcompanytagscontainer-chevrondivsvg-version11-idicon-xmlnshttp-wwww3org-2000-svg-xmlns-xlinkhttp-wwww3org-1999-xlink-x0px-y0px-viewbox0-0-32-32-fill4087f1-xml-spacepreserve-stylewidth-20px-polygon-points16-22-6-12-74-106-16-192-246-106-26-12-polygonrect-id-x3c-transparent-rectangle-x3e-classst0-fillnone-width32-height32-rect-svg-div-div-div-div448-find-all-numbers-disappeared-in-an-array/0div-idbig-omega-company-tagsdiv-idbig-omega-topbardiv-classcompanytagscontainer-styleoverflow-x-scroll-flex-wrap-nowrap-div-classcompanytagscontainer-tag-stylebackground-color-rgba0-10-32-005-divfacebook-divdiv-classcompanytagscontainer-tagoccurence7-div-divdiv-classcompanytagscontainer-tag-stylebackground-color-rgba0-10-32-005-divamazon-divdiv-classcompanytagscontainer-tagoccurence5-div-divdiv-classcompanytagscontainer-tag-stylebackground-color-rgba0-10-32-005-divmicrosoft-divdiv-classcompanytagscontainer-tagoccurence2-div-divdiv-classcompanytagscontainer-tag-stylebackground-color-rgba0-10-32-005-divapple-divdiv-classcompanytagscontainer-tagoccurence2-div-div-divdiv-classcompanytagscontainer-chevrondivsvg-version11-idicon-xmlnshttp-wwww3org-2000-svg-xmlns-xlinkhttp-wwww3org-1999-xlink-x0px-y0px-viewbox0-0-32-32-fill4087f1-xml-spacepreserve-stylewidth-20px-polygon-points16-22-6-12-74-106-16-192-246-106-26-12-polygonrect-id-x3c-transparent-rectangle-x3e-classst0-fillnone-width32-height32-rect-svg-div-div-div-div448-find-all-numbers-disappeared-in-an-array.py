class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1=set(range(1,len(nums)+1))
        for i in range(len(nums)):
            if nums[i] in set1:
                set1.remove(nums[i])
        return set1
                
                
            
        