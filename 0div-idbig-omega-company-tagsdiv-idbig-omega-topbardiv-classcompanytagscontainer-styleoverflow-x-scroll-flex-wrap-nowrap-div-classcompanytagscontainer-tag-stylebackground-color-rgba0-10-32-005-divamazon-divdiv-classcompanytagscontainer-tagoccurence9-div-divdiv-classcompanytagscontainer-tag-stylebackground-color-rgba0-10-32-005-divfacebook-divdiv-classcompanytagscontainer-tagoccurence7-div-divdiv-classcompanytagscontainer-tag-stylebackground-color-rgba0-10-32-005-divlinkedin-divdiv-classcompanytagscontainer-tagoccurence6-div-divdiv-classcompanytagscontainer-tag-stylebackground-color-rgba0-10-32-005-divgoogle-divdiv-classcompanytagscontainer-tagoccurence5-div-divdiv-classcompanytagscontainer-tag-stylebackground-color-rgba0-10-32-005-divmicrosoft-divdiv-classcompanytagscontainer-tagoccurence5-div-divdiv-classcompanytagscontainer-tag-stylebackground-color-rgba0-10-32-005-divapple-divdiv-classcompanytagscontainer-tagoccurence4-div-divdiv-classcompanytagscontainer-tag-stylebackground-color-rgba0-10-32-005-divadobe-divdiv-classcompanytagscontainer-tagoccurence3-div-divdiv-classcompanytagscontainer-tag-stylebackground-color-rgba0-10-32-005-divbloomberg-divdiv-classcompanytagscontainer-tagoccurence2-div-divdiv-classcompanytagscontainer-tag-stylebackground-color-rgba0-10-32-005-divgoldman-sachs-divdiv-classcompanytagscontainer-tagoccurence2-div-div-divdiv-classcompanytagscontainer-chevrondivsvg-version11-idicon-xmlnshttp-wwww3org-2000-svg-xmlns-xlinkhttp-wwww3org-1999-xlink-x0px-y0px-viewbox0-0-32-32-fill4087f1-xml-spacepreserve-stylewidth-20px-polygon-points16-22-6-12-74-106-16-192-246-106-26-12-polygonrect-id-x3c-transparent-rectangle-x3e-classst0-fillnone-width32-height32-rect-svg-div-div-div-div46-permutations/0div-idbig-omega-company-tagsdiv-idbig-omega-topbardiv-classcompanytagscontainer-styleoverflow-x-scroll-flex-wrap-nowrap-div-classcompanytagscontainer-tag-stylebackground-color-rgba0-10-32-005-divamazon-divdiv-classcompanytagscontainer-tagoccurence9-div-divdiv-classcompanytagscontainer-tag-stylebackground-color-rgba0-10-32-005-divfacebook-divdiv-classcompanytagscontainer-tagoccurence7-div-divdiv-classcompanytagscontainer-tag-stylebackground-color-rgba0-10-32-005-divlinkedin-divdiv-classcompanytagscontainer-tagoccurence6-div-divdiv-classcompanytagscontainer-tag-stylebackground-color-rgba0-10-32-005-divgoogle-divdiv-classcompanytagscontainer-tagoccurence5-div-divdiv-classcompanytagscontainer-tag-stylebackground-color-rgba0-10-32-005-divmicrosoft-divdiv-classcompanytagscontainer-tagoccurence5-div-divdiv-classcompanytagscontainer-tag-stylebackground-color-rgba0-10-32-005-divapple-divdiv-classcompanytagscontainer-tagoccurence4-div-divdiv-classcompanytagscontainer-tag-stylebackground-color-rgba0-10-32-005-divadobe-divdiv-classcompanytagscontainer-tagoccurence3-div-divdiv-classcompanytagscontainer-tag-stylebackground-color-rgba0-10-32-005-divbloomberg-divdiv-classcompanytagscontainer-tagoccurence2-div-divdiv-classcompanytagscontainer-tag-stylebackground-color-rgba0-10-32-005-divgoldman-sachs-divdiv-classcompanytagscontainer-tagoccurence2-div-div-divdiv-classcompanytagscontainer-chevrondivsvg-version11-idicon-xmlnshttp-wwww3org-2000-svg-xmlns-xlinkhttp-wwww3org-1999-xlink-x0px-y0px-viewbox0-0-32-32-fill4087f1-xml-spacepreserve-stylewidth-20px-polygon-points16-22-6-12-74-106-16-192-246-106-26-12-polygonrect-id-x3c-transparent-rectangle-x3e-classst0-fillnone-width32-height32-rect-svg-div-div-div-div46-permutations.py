class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(temp,sub):
            if len(sub)==0:
                res.append(temp)
                return
            for i in range (len(sub)):
                backtrack(temp+[sub[i]],sub[:i]+sub[i+1:])
                
        backtrack([],nums)
        return res
                
        