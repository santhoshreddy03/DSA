class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(nums,freq):
            if len(self.ds)==len(nums):
                self.ans.append(self.ds.copy())
                return 
            for i in range(len(nums)):
                if not freq[i]:
                    self.ds.append(nums[i])
                    freq[i]=1
                    recur(nums,freq)
                    freq[i]=0
                    self.ds.pop()
        self.ans=[]
        self.ds=[]
        freq=[0]*len(nums)
        recur(nums,freq)
        return self.ans