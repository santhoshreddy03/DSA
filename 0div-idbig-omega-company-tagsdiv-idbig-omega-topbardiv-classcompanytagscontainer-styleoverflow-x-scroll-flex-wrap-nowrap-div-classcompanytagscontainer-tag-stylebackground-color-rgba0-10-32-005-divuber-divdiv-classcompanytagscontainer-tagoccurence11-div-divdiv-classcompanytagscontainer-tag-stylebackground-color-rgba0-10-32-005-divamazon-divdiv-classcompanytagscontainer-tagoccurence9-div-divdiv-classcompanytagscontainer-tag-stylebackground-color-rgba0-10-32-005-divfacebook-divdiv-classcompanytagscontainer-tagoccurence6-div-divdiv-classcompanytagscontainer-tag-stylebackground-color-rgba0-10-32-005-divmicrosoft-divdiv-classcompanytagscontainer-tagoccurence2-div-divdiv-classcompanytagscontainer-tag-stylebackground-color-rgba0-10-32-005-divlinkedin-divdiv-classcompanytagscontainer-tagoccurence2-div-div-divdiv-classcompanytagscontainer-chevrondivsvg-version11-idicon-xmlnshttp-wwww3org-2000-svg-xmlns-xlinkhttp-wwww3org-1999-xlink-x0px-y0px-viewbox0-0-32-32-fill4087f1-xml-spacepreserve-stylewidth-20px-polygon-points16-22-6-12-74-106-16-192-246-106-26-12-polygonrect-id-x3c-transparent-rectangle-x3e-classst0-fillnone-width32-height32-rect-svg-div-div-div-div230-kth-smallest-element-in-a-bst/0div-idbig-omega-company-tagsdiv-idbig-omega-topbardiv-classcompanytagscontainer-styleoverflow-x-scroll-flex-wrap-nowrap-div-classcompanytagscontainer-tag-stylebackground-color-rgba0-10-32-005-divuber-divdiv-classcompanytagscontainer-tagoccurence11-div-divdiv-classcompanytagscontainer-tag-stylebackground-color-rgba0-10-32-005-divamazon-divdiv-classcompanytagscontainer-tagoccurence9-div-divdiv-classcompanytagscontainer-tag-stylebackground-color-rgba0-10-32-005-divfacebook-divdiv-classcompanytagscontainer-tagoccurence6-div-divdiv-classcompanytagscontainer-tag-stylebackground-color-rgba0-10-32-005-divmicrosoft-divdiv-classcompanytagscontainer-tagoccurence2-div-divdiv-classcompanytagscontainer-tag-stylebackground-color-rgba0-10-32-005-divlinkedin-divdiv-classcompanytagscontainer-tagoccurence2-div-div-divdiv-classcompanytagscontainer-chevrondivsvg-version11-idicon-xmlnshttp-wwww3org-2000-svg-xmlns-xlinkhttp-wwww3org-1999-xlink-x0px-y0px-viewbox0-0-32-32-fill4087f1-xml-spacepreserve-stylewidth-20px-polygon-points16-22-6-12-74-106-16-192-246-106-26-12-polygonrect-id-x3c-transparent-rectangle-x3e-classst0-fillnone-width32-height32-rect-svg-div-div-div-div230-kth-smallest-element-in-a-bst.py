# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        a=0
        def kk(root):
            nonlocal a,count
            
            if not root:
                return
            kk(root.left)
            count+=1
            if count==k:
                a= root.val
            kk(root.right)
            
        kk(root)
        return a
        
        
        
        
        
        
        
        
        
        
#         nums=[]
#         def kk(root):
#             nonlocal nums
#             if not root:
#                 return
#             kk(root.left)
#             nums.append(root.val)

#             kk(root.right)
#             return nums
#         kk(root)

#         return nums[k-1]
