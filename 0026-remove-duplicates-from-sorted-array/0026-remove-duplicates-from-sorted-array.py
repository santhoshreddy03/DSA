class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result= []
        for i in nums:
            if i not in result:
                result.append(i)
        nums[0:len(result)]= result
        return len(result)
        
            