class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        
        def sub(ind,curr):
            if ind>=len(nums):
                return res.append(curr[:])
            
            curr.append(nums[ind])
            sub(ind+1,curr)
            curr.pop()
            sub(ind+1,curr)
            
        sub(0,[])
        return res