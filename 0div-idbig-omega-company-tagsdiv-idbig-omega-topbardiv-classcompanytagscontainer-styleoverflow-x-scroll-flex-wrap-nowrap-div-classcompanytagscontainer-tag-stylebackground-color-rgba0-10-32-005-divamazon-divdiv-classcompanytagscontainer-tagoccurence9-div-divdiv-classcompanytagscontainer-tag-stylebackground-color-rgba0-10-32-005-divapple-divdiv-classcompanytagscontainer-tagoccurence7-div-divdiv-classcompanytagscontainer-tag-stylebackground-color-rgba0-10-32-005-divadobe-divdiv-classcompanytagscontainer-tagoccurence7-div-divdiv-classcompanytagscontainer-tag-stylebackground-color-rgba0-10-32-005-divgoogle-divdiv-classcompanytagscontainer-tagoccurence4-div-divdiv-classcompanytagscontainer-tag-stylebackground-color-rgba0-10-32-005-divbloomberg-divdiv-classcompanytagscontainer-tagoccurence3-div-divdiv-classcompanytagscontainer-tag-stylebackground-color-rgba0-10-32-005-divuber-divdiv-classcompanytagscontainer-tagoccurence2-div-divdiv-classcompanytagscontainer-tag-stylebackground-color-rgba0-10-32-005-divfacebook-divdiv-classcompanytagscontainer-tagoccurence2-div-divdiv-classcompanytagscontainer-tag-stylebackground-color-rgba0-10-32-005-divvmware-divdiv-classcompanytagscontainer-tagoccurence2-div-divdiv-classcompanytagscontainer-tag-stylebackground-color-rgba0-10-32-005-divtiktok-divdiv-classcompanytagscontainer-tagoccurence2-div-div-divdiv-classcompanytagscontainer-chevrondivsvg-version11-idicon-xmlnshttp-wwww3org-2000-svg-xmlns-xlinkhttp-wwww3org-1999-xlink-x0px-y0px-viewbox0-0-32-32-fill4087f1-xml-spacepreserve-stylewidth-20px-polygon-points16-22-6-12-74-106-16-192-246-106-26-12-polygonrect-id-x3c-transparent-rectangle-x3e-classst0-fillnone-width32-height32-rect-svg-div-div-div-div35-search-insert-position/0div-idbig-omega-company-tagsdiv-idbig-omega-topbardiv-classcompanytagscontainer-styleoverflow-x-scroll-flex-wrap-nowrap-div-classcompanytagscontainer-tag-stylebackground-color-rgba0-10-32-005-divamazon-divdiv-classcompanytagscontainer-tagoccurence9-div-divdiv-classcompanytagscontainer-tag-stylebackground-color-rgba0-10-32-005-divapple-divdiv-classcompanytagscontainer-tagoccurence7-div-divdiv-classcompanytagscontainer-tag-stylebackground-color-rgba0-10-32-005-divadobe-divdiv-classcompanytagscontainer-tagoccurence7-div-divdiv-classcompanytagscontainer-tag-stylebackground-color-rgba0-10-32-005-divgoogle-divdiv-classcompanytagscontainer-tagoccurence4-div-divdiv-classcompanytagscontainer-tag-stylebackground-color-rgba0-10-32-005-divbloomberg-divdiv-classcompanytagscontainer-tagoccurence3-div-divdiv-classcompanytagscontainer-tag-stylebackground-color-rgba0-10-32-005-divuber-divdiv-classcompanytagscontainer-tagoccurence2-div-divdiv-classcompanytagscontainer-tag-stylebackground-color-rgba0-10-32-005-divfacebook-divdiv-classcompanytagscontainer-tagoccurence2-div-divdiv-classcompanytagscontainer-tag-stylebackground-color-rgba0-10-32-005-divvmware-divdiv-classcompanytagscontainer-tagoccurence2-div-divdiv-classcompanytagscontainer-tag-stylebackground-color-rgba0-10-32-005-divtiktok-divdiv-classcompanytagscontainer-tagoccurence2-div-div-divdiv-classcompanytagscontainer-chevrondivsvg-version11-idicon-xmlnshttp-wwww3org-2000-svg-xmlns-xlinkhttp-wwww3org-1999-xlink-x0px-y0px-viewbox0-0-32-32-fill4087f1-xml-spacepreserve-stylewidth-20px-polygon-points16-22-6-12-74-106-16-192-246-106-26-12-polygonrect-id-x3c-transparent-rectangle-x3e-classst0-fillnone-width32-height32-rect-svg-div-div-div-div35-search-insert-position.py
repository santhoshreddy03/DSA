class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        ans=0
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m           
            if nums[m]>target:
                r=m-1
            if nums[m]<target:
                ans=m
                l=m+1
        if nums[ans]>target:
            return ans
        else:
            return ans+1
