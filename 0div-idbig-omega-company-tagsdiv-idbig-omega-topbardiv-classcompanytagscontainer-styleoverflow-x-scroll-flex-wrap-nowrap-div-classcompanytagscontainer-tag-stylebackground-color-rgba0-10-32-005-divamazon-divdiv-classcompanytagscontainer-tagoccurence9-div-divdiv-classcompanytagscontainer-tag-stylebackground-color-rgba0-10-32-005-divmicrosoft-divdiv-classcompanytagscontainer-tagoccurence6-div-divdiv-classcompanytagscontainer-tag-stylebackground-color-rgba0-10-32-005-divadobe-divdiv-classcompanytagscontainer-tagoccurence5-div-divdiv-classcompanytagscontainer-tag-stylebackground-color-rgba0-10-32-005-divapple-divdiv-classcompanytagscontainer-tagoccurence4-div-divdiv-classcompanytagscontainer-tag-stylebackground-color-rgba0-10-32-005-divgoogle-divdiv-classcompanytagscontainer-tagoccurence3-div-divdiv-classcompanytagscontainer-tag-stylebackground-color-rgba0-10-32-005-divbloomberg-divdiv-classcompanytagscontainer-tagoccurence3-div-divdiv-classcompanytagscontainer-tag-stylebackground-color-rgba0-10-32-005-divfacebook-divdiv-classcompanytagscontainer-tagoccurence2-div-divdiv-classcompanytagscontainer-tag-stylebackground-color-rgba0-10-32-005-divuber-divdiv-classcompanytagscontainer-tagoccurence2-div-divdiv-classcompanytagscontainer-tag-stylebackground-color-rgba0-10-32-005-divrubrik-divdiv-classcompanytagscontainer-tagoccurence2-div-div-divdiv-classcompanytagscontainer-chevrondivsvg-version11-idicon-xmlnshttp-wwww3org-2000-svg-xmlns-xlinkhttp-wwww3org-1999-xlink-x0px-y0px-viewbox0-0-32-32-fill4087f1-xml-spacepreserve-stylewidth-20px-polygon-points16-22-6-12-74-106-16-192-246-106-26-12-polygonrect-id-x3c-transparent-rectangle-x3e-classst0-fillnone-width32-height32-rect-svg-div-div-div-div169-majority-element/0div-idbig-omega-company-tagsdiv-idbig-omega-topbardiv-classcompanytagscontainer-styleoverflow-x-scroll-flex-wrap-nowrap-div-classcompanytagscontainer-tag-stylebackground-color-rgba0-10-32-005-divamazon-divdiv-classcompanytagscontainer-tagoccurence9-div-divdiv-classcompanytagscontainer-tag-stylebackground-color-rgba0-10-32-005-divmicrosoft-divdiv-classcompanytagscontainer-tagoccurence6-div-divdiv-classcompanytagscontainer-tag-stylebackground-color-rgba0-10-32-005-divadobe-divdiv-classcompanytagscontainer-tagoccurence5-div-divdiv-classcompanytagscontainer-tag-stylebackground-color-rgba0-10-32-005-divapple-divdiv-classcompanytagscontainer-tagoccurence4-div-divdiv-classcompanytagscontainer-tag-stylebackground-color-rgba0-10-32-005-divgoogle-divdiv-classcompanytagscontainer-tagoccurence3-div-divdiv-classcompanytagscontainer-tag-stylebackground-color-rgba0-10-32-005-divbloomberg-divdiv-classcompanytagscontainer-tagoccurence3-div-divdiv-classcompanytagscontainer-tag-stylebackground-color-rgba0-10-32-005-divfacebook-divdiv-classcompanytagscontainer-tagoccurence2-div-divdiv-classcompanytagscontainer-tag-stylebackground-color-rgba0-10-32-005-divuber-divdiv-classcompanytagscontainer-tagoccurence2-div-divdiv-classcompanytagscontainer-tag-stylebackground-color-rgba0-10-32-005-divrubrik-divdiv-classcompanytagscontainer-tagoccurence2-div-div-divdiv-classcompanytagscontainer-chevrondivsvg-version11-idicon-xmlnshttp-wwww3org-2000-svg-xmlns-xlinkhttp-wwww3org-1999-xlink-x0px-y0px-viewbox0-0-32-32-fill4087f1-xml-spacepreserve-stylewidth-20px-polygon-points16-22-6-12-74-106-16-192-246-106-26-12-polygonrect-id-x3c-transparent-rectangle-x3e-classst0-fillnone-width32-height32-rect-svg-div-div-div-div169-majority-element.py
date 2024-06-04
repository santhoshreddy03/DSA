class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashset={}
        for i in range(len(nums)):
            if nums[i] in hashset:
                hashset[nums[i]]+=1
            else:
                hashset[nums[i]]=1
        c=0
        k=0
        for i in hashset:
            if hashset[i]>c:
                
                c=hashset[i]
                k=i
        return k
            
        