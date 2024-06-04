class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=0
        cnt2=0
        el1=None
        el2=None
        co1=0
        co2=0
        list=[]
        for i in range(len(nums)):
            if cnt1==0 and el2!=nums[i]:
                el1=nums[i]
                cnt1=1
            elif cnt2==0 and el1!=nums[i]:
                el2=nums[i]
                cnt2=1
            elif el1==nums[i]:
                cnt1+=1
            elif el2==nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        for i in range(len(nums)):
            if el1==nums[i]:
                co1+=1
            elif el2==nums[i]:
                co2+=1
        print(el1,el2)
        if co1>len(nums)/3:
            list.append(el1)
        if co2>len(nums)/3:
            list.append(el2)
        return list
        