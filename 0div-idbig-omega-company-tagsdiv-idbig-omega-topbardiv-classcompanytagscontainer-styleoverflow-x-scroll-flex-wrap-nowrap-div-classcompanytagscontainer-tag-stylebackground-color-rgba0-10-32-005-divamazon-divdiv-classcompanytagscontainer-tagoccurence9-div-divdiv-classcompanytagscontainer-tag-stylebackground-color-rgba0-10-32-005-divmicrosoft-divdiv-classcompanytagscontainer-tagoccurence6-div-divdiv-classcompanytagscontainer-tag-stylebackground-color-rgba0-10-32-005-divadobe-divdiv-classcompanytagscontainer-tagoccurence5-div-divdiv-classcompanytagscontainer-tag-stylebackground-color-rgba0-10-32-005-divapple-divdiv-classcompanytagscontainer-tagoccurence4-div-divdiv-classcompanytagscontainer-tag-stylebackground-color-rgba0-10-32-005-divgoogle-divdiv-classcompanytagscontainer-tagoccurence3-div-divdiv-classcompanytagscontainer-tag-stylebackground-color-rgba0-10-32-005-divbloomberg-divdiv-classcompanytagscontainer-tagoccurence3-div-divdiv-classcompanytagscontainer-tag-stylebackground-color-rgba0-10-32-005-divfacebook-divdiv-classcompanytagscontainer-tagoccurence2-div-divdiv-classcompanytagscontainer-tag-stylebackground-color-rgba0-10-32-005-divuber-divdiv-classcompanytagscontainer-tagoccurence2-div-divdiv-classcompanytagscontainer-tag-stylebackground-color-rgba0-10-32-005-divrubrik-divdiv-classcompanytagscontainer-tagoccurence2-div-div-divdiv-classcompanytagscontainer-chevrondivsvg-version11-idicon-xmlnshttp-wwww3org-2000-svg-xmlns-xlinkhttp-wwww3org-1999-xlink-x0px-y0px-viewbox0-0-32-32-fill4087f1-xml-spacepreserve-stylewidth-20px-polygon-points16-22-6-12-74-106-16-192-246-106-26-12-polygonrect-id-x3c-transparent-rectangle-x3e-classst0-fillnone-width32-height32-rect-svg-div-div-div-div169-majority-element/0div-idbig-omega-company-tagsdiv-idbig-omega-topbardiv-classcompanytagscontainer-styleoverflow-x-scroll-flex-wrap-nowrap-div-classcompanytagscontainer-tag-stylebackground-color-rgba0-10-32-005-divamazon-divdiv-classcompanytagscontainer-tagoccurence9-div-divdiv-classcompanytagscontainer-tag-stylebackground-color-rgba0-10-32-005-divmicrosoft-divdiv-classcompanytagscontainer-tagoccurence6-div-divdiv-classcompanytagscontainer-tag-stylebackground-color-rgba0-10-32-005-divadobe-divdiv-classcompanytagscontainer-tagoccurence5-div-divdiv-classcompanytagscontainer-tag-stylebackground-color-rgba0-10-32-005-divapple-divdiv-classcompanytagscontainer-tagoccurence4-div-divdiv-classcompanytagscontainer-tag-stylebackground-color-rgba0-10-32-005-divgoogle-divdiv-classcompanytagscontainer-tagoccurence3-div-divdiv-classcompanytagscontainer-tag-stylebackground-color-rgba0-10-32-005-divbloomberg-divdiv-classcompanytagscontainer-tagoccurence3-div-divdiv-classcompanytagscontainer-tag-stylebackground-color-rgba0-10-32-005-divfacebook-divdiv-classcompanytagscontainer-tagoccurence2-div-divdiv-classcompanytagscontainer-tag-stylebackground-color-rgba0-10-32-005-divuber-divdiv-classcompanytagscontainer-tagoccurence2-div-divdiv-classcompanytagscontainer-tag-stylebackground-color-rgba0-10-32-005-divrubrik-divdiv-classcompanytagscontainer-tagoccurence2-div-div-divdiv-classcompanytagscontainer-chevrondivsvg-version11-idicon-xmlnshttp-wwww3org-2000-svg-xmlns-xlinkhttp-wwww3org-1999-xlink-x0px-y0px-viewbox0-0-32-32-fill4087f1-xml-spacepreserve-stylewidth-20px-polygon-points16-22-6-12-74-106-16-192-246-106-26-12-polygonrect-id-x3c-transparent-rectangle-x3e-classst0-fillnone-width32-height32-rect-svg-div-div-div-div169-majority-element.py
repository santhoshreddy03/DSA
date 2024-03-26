class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=[]
        hmap={}
        for i in nums:
            hmap[i]=1+hmap.get(i,0)
        print(hmap)
        for i in hmap:
            print(i)
            if hmap[i]>len(nums)//2:
                res.append(i)
        print(res)
        return max(res)
            