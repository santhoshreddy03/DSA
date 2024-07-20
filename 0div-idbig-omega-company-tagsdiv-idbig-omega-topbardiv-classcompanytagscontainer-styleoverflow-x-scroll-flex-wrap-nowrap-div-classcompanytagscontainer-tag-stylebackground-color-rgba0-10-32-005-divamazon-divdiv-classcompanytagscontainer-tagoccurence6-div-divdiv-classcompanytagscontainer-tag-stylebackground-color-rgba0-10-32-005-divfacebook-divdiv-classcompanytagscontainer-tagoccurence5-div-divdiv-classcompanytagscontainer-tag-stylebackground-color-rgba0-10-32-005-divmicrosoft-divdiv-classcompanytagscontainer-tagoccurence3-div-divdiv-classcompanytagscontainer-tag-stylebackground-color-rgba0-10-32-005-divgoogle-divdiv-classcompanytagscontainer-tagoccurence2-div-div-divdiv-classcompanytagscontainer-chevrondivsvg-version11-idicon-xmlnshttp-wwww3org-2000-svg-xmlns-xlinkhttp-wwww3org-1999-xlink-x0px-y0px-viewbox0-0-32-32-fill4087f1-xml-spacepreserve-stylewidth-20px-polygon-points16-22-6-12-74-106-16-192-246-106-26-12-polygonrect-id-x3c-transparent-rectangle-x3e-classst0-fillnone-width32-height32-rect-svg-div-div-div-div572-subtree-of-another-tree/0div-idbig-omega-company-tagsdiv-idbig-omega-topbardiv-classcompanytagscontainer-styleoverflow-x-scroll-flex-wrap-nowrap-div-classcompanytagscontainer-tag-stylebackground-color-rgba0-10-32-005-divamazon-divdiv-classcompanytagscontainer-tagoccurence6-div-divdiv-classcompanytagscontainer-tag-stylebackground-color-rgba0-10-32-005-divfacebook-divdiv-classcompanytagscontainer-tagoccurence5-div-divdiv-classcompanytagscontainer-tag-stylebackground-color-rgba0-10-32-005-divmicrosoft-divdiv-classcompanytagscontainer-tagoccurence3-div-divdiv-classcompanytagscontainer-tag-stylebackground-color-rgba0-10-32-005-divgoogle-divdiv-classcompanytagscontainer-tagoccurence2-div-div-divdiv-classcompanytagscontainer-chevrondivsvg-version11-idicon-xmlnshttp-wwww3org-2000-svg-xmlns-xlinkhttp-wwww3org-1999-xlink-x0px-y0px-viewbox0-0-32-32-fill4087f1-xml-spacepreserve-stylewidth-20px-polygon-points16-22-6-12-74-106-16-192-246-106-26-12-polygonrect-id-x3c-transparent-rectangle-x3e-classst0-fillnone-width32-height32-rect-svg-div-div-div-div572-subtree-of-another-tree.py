# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root,subRoot)
    def traverse(self,root,subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.sam(root,subRoot):
            return True
        return self.traverse(root.left,subRoot) or self.traverse(root.right,subRoot)
        
        
        
        
        
    def sam(self,p,q):
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False
        if p.val!=q.val:
            return False
        return self.sam(p.left,q.left) and self.sam(p.right,q.right)
        
        
        
        
        
        
        
#         def sub(root,subRoot):
#             if not subRoot:
#                 return True
#             if not root:
#                 return False
#             if sam(root,subRoot):
#                 return True
#             return sub(root.left,subRoot) or sub(root.right,subRoot)
        
#         def sam(p,q):
#             if not p and not q:
#                 return True
#             if not p and q:
#                 return False
#             if p and not q:
#                 return False
#             if p.val!=q.val:
#                 return False
#             return sam(p.right,q.right) and sam(p.left,q.left)
        
#         sub(root,subRoot)
#         return sub(root,subRoot)