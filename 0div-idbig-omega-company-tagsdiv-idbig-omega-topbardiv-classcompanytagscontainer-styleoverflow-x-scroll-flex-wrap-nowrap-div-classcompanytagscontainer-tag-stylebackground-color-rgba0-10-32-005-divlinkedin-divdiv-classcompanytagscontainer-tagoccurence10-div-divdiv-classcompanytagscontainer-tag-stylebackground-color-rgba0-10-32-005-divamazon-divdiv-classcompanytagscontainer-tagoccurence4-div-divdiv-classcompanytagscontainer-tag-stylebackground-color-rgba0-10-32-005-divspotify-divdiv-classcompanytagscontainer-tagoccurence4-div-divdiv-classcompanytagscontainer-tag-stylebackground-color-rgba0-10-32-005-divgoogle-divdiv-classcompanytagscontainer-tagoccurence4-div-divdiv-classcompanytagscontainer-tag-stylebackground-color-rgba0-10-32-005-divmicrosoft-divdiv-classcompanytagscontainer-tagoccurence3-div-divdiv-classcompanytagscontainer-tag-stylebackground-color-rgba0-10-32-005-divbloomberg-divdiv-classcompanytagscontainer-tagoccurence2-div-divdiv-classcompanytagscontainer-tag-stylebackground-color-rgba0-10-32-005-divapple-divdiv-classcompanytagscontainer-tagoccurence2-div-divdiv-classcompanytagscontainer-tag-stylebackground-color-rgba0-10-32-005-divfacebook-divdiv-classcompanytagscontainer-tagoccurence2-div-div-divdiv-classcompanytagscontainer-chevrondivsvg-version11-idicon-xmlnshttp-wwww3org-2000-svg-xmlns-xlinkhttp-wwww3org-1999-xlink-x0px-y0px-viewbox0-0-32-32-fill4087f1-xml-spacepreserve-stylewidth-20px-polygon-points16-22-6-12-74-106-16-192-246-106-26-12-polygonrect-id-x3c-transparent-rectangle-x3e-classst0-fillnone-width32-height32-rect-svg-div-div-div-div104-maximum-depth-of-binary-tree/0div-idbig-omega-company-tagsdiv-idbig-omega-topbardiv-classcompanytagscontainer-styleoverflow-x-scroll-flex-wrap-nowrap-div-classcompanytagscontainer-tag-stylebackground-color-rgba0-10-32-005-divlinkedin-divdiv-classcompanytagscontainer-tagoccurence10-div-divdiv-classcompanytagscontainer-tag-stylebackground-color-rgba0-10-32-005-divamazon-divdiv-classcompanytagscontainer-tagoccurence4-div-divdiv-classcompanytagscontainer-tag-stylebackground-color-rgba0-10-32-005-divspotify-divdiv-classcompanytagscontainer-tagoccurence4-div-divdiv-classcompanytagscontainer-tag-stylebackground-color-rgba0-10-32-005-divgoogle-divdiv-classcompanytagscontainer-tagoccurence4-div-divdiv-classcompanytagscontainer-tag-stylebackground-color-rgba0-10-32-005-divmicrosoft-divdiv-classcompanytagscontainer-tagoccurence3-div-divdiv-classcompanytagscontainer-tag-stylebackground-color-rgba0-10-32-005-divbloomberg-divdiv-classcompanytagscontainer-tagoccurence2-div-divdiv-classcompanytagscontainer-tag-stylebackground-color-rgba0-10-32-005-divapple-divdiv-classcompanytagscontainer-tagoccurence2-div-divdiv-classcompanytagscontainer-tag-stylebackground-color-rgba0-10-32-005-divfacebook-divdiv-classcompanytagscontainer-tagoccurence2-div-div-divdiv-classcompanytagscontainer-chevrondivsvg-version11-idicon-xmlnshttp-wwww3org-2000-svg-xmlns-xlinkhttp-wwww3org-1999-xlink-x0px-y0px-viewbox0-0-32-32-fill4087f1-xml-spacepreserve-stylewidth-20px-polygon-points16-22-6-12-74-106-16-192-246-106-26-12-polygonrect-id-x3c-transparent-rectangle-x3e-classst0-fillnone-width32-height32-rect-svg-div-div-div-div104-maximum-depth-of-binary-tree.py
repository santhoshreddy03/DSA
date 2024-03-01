# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def rec(root,count):
            nonlocal ans
            if not root:
                ans = max(ans, count)
                return count
            rec(root.left,count+1)
            rec(root.right,count+1)
        rec(root, 0)
        return ans