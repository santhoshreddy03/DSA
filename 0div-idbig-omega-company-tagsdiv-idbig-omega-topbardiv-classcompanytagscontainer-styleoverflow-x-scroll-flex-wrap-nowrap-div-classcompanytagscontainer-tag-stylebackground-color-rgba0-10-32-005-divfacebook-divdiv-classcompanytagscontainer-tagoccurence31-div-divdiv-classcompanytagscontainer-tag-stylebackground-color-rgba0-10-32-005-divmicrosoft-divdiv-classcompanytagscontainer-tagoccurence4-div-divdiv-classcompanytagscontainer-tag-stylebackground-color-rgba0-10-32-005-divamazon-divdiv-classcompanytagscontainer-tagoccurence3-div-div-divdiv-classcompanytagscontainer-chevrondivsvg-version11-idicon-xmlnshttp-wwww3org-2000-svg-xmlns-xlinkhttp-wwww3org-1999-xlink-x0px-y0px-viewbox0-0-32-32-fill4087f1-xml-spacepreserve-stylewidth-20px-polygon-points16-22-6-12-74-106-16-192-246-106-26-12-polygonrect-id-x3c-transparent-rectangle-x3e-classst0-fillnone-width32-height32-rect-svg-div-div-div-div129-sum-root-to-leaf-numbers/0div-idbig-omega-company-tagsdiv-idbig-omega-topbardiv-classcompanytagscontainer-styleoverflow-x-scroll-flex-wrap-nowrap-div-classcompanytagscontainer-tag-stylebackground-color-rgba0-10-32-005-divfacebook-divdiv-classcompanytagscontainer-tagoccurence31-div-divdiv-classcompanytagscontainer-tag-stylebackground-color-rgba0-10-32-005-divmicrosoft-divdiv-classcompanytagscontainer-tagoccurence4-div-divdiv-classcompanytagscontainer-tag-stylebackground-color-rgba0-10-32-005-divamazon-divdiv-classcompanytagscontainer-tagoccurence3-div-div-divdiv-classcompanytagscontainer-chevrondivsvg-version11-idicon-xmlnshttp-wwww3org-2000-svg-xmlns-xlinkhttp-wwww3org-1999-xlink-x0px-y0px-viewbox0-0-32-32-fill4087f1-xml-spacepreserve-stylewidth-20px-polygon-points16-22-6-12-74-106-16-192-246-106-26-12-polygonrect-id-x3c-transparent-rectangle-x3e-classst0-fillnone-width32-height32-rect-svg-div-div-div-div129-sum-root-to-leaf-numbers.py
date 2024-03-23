# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        count=0
        val=0
        def summ(root,val):
            nonlocal count
            if not root.left and not root.right:
                count+=val*10+root.val
                return
            if root.left:
                
                summ(root.left,val*10+root.val)
            if root.right:
                summ(root.right,val*10+root.val)
        summ(root,0)
        return count
        