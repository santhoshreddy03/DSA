# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # ans=0
        # def maxi(root,count):
        #     nonlocal ans
        #     if not root:
        #         ans=max(ans,count)
        #         return
        #     maxi(root.left,count+1)
        #     maxi(root.right,count+1)
        # maxi(root,0)
        # return ans