class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def csum(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return 
            if total>target or i==len(candidates):
                return
            curr.append(candidates[i])
            csum(i,curr,total+candidates[i])
            curr.pop()
            csum(i+1,curr,total)
        csum(0,[],0)
        return res
        