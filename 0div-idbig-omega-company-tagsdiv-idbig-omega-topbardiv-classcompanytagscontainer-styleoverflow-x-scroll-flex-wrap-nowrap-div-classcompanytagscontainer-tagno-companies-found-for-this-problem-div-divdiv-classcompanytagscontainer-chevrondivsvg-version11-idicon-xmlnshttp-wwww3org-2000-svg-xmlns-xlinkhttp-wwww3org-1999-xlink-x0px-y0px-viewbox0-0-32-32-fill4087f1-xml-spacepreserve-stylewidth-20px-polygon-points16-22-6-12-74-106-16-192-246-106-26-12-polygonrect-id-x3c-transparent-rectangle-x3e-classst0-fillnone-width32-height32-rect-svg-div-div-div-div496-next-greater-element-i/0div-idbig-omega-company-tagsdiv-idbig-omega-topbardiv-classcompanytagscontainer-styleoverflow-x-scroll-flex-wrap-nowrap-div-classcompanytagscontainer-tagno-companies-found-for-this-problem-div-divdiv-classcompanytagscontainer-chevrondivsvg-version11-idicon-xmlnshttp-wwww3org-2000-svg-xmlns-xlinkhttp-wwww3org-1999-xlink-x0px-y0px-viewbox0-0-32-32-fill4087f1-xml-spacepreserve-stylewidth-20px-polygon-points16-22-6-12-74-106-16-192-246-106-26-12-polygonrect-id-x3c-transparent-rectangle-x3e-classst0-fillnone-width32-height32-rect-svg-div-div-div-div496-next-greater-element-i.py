class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inde1={n:i for i , n in enumerate(nums1)}
        res=[-1] * len(nums1)
        
        for i in range(len(nums2)):
            if nums2[i] not in inde1:
                continue
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    ind1=inde1[nums2[i]]
                    res[ind1]=nums2[j]
                    break
        return res
        