class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=self.binarysearch(nums,target,True)
        right=self.binarysearch(nums,target,False)
        return [left,right]


    def binarysearch(self,nums,target,leftbias):
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            elif nums[m]>target:
                r=m-1
            elif nums[m]==target:
                i=m
                if leftbias:
                    r=m-1
                else:
                    l=m+1

        return i
        