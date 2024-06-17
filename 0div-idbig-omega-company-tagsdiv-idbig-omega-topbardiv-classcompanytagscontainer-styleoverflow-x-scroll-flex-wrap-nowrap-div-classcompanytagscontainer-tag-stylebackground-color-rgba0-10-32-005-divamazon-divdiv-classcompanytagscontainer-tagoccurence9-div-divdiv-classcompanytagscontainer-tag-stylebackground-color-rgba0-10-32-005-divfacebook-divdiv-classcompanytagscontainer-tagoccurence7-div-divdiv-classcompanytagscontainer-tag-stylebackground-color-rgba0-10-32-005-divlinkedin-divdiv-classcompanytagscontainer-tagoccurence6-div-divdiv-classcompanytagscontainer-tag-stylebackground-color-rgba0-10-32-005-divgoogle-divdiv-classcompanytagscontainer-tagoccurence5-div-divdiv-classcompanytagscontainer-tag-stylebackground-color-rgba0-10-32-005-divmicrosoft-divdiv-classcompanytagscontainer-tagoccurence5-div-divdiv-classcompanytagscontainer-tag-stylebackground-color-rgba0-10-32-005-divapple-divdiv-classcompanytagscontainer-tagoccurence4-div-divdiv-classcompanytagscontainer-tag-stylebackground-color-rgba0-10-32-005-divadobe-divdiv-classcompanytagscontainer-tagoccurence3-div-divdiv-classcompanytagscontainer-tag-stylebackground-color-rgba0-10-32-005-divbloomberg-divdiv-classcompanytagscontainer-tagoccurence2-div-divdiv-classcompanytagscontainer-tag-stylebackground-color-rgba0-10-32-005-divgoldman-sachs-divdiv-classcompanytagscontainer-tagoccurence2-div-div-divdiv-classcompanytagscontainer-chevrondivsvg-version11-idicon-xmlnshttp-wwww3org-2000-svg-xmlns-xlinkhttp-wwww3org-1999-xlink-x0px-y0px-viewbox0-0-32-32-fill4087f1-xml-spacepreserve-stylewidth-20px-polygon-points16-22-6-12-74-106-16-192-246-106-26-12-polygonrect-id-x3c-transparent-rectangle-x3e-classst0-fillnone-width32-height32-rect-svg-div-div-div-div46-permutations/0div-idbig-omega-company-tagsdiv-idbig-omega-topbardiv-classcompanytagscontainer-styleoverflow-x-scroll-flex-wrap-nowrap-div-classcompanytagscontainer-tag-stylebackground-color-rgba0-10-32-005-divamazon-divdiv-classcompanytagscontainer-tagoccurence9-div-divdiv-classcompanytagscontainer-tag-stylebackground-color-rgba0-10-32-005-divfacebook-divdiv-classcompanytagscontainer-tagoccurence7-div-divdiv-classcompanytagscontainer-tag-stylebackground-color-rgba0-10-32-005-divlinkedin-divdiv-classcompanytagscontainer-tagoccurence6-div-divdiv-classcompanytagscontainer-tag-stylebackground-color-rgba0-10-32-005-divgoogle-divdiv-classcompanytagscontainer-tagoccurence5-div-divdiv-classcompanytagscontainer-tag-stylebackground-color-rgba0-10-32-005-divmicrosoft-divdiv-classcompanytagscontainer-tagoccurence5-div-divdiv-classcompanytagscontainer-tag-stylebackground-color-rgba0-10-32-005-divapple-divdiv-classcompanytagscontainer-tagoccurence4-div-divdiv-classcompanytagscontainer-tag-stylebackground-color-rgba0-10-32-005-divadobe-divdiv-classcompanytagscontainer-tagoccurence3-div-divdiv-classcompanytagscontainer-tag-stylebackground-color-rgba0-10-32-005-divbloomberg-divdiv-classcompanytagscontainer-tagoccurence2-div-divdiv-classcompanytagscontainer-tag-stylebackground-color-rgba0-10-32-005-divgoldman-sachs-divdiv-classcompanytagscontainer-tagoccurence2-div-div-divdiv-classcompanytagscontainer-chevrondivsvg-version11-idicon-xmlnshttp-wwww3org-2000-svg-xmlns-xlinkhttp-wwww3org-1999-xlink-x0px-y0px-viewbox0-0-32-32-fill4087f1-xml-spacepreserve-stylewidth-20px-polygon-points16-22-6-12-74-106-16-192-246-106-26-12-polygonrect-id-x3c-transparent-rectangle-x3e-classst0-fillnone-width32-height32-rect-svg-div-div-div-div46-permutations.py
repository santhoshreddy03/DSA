class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(nums,freq,ds):
            if len(ds)==len(nums):
                self.ans.append(ds.copy())
                return 
            for i in range(len(nums)):
                if not freq[i]:
                    ds.append(nums[i])
                    freq[i]=1
                    recur(nums,freq,ds)
                    freq[i]=0
                    ds.pop()
        self.ans=[]
        ds=[]
        freq=[0]*len(nums)
        recur(nums,freq,ds)
        return self.ans