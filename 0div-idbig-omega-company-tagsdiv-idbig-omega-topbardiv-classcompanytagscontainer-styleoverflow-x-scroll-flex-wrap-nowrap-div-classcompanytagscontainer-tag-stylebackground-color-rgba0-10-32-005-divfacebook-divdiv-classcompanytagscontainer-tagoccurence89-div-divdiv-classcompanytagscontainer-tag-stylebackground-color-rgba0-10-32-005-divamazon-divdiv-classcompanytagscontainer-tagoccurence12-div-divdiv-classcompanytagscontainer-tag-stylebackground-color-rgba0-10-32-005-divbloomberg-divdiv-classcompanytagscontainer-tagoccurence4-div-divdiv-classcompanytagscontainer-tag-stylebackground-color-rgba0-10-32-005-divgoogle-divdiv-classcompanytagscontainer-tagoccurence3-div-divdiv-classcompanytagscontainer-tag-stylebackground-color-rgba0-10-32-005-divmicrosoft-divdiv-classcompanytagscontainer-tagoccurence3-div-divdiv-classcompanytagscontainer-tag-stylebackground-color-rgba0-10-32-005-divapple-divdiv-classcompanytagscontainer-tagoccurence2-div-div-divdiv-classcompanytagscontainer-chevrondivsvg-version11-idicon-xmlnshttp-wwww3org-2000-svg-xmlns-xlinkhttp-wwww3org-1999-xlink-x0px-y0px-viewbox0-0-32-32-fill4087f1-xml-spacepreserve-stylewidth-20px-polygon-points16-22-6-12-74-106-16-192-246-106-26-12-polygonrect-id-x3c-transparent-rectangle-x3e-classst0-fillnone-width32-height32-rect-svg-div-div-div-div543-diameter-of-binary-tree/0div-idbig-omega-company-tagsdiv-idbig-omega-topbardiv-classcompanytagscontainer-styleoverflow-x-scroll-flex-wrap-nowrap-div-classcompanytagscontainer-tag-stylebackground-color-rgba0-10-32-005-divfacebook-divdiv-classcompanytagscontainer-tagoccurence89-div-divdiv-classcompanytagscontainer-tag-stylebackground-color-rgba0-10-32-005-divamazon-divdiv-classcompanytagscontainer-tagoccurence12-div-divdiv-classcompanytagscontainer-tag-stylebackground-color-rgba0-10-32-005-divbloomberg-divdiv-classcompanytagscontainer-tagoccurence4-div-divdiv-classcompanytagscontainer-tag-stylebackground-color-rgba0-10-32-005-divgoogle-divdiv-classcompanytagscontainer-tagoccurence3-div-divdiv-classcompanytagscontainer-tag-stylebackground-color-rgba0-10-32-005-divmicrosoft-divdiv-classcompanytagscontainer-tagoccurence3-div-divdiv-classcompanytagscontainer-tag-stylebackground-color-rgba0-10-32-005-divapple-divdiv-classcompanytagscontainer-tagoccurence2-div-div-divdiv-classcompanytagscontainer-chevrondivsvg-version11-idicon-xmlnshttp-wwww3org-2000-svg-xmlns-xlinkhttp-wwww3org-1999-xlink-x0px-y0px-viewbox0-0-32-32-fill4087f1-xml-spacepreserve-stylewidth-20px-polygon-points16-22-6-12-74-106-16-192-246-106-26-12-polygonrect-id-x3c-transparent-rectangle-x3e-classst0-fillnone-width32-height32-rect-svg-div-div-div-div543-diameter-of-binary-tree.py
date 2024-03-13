# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         ans=0
#         count=0
#         def maxi(root,count):
#             nonlocal ans
#             if not root:
#                 ans=max(ans,count)
#                 return
#             maxi(root.left,count+1)
#             maxi(root.right,count+1)
        
#         maxi(root,0)
        
#         return ans+count
        maxi=0
        def dpt(root):
            nonlocal maxi
            if not root:
                return 0
            if not root.left and  not root.right:
                return 1
            left=dpt(root.left)
            right = dpt(root.right)
            maxi=max(left+right,maxi)
            return 1+max(left,right)
            

        dpt(root)
        return maxi
        
        
            
        