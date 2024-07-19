# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.sam(p,q)
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
    
    
        
        
        
        # def sam(p,q):
        #     if not p and not q:
        #         return True
        #     if p and not q:
        #         return False
        #     if q and not p:
        #         return False
        #     if p.val!=q.val:
        #         return False
        #     return sam(p.left,q.left) and sam(p.right,q.right)
        # return sam(p,q)
        
        # def sam(p,q):
        #     if not p and not q:
        #         return True
        #     if not p and q:
        #         return False
        #     if p and not q:
        #         return False
        #     if p.val!=q.val:
        #         return False
        #     return sam(p.left,q.left) and sam(p.right,q.right)
        # return sam(p,q)