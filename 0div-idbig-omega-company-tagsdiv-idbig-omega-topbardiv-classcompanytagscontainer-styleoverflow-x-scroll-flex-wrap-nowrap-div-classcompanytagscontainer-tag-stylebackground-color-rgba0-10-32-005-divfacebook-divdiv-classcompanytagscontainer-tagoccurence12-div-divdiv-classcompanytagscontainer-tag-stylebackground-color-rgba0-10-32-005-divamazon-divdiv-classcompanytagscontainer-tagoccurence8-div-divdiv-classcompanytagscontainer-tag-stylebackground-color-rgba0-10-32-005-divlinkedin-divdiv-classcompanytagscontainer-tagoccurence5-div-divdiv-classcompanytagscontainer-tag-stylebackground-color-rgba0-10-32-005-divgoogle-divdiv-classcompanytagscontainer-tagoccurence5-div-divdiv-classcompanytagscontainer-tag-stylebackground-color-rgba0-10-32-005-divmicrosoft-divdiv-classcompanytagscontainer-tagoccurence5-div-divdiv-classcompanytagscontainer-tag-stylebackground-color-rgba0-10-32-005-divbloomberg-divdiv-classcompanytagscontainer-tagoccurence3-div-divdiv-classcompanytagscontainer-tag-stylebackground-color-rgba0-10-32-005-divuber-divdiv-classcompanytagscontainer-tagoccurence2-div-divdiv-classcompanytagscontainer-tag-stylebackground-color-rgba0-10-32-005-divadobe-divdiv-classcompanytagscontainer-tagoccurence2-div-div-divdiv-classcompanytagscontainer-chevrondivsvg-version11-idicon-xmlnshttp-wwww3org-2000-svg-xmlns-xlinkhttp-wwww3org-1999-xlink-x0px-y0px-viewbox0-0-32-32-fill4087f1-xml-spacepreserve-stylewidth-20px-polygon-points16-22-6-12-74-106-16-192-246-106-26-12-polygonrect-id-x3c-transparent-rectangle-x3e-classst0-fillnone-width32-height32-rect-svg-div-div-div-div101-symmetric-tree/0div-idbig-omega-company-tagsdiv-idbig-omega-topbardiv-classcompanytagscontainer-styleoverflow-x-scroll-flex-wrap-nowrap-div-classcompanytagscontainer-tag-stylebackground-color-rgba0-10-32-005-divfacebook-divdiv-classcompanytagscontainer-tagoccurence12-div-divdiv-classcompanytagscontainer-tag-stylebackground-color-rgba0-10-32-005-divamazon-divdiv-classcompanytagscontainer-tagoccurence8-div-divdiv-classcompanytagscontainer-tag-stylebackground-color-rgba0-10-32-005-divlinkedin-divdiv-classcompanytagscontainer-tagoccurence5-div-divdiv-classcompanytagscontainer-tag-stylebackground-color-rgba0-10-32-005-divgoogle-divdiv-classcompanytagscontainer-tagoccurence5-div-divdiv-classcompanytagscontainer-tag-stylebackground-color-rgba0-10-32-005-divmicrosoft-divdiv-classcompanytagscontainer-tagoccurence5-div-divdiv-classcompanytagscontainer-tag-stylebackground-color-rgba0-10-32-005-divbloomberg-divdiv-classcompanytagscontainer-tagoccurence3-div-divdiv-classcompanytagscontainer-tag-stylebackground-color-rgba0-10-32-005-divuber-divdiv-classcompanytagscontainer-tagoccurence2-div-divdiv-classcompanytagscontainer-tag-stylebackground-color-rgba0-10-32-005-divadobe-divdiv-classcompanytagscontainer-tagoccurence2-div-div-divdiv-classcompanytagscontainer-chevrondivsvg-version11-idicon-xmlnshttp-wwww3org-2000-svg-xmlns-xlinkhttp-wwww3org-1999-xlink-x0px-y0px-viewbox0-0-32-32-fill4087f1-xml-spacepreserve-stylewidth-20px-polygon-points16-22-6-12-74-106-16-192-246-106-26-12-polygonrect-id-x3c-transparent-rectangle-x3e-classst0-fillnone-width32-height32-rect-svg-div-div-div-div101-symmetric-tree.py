# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check(root.left,root.right)
        
    def check(self,rleft,rright):
        if rleft==None or rright==None:
            return rleft==rright
        if rleft.val!=rright.val:
            return False
        return self.check(rleft.left,rright.right) and self.check(rleft.right,rright.left)
        
        