class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
        