class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def subset(i,arr):

            if i==len(nums):
                if arr not in res:
                    res.append(arr.copy())
                return
            arr.append(nums[i])
            subset(i+1,arr)
            arr.pop()
            subset(i+1,arr)
        subset(0,[])
        return res
            
        