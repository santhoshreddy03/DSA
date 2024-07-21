# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.sub(root,subRoot)
        
    def sub(self,root,subroot):
        if not root:
            return False
        if not subroot:
            return True
        if root.val==subroot.val and self.sam(root,subroot):
            return True
        return self.sub(root.left,subroot) or self.sub(root.right,subroot)
        
    def sam(self,p,q):
        if not p and not q:
            return True
        if p and not q:
            return False
        if not p and q:
            return False
        if p.val!=q.val:
            return False
        return self.sam(p.left,q.left) and self.sam(p.right,q.right)