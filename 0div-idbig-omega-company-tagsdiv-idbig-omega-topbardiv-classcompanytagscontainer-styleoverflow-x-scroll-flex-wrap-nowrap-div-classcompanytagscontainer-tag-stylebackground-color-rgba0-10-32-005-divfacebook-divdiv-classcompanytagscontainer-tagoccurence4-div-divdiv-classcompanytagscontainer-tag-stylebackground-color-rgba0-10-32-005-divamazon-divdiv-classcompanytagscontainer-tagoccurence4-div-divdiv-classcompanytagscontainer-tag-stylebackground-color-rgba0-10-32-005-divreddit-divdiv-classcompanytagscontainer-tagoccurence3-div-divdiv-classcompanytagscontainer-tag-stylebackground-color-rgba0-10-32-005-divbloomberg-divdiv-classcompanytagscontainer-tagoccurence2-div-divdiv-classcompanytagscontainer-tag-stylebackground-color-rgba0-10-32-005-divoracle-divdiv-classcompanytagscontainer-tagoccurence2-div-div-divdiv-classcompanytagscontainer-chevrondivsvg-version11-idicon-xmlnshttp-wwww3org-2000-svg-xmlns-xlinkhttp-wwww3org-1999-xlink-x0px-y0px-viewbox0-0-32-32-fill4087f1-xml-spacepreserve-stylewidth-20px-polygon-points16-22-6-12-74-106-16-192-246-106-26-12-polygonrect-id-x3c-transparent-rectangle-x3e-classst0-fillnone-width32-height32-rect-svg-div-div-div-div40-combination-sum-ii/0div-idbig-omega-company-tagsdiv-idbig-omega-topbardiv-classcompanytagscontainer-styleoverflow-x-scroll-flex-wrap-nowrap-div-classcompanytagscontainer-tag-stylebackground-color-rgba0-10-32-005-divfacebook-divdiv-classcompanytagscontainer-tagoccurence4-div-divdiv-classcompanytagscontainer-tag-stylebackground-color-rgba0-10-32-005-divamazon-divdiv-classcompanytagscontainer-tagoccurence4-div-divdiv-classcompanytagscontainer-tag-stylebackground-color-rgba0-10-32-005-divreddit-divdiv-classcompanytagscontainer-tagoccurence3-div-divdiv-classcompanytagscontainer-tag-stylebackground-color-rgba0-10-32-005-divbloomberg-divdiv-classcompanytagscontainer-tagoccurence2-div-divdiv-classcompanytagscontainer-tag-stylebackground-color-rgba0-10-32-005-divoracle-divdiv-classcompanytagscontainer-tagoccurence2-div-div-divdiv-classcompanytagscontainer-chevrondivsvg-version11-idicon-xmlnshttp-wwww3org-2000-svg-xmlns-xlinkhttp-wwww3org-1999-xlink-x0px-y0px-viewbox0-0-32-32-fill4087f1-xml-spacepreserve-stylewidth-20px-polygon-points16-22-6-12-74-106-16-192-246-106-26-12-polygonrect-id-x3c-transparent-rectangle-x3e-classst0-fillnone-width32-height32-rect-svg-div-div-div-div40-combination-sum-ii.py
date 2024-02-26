class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(curr,i,target):
            if target==0:
                res.append(curr.copy())
                return
            if target <0 or i>=len(candidates):
                return
            
            for k in range(i, len(candidates)):
                if k>i and candidates[k]==candidates[k-1]:
                    continue
                if target<0:
                    break
                curr.append(candidates[k])
                backtrack(curr,k+1,target-candidates[k])
                curr.pop()
        backtrack([],0,target)
        return res
            
                
        