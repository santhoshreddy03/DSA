# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ans=0
        def count(root,cnt):
            nonlocal ans
            if not root:
                ans=max(ans,cnt)
                return 
            count(root.left,cnt+1)
            count(root.right,cnt+1)

        count(root,0)
        return ans
        
        