class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        if len(nums)==1:
            return nums[0]
        while l<=r:
            m=(l+r)//2
            if (m>0 and nums[m] !=nums[m-1]) and (m<len(nums)-1 and nums[m]!=nums[m+1]):
                    return nums[m]
            if m==len(nums)-1 and nums[m] !=nums[m-1] or m==0 and nums[m]!=nums[m+1]:
                return nums[m]
            if m%2!=0:
                
                if nums[m]!=nums[m+1]:
                    l=m+1
                else:
                    r=m-1
            else:
                if nums[m]!=nums[m+1]:
                    r=m-1
                else:
                    l=m+1
 
