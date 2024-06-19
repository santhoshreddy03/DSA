class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        # o(m+n)
        nums1idx={}
        stack=[]
        res=[-1]*len(nums1)
        for i in range(len(nums1)):
            nums1idx[nums1[i]]=i
        for i in range(len(nums2)):
            while stack and nums2[i]>stack[-1]:
                val=stack.pop()
                idx=nums1idx[val]
                res[idx]=nums2[i]
            if nums2[i] in nums1idx:
                stack.append(nums2[i])
        return res
        
#         o(m*n)
#         nums1idx={}
#         res=[-1]*len(nums1)
#         for i in range(len(nums1)):
#             nums1idx[nums1[i]]=i
        
#         for i in range(len(nums2)):
#             if nums2[i] not in nums1idx:
#                 continue
#             for j in range(i+1,len(nums2)):
#                 if nums2[j]>nums2[i]:
#                     idx=nums1idx[nums2[i]]
#                     res[idx]=nums2[j]
#                     break
#         return res