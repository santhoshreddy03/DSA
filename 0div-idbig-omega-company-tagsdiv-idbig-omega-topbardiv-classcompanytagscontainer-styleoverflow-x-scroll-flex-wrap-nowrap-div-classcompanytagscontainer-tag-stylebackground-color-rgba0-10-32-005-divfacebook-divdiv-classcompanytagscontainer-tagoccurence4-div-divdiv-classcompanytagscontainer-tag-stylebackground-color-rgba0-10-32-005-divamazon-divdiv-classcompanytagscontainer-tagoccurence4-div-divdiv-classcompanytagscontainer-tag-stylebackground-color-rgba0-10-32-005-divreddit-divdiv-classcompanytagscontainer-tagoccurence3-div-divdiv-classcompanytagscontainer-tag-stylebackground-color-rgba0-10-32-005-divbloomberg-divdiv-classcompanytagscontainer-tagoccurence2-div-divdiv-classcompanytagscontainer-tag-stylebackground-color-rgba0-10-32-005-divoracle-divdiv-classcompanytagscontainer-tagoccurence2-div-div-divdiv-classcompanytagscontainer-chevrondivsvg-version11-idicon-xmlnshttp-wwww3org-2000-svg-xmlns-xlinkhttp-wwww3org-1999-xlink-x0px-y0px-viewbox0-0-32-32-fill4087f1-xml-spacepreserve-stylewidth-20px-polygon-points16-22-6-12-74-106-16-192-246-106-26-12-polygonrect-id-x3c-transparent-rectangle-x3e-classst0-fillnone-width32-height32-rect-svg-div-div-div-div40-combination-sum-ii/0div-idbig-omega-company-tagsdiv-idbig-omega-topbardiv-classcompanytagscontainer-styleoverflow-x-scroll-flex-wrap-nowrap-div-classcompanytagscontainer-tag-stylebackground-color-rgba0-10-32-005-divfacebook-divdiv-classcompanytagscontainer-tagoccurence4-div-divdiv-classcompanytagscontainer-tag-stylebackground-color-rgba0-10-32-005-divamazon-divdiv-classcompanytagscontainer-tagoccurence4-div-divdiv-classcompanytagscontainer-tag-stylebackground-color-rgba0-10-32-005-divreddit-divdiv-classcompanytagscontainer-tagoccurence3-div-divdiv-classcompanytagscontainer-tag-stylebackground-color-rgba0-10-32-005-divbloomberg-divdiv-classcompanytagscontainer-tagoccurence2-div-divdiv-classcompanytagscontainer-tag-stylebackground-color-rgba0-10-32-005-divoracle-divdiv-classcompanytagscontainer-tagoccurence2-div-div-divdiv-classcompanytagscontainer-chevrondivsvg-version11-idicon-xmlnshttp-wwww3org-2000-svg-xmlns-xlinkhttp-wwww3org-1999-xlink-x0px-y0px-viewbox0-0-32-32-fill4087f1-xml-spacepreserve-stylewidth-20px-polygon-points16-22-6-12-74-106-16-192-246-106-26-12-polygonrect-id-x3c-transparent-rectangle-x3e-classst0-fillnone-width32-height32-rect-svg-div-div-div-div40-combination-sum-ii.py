class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def csum2(i,curr,target):
            if target==0:
                res.append(curr.copy())
            
            for k in range(i,len(candidates)):
                if k>i and candidates[k]==candidates[k-1]:
                    continue
                if target<0:
                    break
                curr.append(candidates[k])
                csum2(k+1,curr,target-candidates[k])
                curr.pop()
                

        csum2(0,[],target)
        return res
            
        