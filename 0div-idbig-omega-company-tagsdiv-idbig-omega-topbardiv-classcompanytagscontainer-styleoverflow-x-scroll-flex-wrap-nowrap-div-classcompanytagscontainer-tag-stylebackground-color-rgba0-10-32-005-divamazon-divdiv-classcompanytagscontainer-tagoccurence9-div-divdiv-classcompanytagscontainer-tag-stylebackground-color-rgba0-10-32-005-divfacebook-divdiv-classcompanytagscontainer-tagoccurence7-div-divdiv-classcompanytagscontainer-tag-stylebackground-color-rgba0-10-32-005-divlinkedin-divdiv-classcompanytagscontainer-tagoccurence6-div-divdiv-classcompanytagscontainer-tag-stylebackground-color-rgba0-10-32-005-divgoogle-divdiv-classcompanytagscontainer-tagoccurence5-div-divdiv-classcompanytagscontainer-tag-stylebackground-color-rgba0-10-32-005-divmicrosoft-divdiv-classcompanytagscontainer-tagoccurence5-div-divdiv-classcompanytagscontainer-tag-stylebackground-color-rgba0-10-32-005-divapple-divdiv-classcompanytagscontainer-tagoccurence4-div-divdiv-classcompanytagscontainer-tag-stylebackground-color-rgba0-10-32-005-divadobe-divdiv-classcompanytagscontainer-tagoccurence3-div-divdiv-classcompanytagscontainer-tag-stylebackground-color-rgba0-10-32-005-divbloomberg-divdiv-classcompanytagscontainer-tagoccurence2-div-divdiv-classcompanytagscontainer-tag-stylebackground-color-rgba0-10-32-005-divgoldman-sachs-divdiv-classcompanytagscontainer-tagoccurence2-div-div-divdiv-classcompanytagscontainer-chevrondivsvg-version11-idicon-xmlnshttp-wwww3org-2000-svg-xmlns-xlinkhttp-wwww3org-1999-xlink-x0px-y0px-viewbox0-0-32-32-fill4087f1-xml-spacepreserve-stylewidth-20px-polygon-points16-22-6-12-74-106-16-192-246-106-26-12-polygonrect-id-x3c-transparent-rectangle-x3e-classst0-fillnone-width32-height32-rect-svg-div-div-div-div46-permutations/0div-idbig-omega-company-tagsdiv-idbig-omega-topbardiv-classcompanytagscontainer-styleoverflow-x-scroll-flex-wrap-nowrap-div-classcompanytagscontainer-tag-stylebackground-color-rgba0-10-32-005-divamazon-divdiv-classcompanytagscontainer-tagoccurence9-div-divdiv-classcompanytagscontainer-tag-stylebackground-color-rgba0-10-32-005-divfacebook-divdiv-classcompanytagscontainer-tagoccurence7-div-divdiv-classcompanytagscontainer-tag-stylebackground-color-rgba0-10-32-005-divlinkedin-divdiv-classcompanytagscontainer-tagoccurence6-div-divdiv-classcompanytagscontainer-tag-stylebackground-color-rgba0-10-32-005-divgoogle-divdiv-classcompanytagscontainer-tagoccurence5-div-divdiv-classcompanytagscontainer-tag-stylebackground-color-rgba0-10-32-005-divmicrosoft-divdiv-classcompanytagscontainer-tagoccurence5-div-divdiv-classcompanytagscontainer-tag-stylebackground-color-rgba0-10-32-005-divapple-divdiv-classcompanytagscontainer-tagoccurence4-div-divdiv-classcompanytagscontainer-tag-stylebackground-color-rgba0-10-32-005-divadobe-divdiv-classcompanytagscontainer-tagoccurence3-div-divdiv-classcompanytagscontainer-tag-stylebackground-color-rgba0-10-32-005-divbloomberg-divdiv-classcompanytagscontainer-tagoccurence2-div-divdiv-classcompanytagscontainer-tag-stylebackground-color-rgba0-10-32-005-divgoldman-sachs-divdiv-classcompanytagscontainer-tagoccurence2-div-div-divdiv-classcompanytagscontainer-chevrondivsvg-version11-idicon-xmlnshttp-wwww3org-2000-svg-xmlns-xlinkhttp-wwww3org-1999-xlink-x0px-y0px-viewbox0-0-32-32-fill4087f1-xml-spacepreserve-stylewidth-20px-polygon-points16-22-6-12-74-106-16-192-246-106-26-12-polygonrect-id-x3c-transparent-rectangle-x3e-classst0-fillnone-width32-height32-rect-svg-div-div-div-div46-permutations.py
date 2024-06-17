class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(index,nums,ans):
            if index==len(nums):
                ans.append(nums.copy())
                return
            for i in range(index,len(nums)):
                nums[index],nums[i]=nums[i],nums[index]
                recur(index+1,nums,ans)
                nums[index],nums[i]=nums[i],nums[index]
        ans=[]
        recur(0,nums,ans)
        return ans
                