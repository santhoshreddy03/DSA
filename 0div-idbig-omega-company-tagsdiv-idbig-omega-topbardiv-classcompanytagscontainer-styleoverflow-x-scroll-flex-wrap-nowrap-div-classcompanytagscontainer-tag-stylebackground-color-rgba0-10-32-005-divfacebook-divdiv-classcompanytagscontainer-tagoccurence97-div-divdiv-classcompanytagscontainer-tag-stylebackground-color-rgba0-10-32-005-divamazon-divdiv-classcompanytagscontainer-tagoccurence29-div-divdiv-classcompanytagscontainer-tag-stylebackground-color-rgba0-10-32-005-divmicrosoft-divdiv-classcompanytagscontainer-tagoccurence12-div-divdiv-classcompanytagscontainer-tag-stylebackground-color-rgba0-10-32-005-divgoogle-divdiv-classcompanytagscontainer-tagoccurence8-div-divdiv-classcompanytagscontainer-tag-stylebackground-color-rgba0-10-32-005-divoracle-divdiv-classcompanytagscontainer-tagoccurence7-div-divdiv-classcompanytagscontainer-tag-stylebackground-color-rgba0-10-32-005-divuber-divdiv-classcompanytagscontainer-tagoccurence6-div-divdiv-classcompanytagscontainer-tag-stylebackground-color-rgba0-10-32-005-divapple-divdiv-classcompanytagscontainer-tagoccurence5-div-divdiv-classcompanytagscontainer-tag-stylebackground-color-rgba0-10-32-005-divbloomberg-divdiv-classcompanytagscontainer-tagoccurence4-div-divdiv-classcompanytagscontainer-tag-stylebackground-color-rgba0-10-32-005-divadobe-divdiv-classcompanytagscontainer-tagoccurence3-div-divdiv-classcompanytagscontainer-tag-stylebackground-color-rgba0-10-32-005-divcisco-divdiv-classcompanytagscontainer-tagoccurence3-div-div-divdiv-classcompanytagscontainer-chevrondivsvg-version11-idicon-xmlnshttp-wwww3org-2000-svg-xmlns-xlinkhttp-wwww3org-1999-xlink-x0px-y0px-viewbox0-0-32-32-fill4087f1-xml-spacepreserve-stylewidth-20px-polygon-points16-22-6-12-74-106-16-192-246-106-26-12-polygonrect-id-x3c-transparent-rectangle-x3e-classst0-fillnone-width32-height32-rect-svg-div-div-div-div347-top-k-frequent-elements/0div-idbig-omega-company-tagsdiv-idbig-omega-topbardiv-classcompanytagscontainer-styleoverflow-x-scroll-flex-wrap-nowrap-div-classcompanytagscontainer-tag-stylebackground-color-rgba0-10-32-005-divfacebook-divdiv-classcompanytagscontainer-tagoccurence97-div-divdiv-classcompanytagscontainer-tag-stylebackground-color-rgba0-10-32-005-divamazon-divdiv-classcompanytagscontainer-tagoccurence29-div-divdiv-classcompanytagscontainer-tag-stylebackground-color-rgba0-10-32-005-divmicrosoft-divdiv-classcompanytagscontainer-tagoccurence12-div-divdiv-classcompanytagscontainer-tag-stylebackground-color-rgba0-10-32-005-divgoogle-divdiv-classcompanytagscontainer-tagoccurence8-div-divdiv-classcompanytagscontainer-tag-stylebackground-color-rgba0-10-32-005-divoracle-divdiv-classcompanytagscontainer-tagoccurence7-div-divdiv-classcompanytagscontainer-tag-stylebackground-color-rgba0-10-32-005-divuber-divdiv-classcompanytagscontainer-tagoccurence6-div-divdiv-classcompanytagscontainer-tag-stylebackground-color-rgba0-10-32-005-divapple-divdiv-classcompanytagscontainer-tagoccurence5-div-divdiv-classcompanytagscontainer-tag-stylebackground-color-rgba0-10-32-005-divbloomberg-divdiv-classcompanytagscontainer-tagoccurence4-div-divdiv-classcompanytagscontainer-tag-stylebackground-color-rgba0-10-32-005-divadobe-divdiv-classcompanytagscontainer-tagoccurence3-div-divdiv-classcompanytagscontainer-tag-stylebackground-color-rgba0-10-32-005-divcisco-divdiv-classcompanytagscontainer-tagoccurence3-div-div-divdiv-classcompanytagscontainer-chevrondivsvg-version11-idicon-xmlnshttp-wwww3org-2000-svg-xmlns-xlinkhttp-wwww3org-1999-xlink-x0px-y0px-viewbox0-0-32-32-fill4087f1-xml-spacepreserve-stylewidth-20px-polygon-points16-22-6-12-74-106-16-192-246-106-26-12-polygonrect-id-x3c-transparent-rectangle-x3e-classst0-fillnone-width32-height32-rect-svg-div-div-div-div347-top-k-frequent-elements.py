class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        res=[]
        freq=[[] for i in range(len(nums)+1)]

        for i in nums:
            count[i]=1+count.get(i,0)
            
        for i,n in count.items():
            freq[n].append(i)
            
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
            
            
        