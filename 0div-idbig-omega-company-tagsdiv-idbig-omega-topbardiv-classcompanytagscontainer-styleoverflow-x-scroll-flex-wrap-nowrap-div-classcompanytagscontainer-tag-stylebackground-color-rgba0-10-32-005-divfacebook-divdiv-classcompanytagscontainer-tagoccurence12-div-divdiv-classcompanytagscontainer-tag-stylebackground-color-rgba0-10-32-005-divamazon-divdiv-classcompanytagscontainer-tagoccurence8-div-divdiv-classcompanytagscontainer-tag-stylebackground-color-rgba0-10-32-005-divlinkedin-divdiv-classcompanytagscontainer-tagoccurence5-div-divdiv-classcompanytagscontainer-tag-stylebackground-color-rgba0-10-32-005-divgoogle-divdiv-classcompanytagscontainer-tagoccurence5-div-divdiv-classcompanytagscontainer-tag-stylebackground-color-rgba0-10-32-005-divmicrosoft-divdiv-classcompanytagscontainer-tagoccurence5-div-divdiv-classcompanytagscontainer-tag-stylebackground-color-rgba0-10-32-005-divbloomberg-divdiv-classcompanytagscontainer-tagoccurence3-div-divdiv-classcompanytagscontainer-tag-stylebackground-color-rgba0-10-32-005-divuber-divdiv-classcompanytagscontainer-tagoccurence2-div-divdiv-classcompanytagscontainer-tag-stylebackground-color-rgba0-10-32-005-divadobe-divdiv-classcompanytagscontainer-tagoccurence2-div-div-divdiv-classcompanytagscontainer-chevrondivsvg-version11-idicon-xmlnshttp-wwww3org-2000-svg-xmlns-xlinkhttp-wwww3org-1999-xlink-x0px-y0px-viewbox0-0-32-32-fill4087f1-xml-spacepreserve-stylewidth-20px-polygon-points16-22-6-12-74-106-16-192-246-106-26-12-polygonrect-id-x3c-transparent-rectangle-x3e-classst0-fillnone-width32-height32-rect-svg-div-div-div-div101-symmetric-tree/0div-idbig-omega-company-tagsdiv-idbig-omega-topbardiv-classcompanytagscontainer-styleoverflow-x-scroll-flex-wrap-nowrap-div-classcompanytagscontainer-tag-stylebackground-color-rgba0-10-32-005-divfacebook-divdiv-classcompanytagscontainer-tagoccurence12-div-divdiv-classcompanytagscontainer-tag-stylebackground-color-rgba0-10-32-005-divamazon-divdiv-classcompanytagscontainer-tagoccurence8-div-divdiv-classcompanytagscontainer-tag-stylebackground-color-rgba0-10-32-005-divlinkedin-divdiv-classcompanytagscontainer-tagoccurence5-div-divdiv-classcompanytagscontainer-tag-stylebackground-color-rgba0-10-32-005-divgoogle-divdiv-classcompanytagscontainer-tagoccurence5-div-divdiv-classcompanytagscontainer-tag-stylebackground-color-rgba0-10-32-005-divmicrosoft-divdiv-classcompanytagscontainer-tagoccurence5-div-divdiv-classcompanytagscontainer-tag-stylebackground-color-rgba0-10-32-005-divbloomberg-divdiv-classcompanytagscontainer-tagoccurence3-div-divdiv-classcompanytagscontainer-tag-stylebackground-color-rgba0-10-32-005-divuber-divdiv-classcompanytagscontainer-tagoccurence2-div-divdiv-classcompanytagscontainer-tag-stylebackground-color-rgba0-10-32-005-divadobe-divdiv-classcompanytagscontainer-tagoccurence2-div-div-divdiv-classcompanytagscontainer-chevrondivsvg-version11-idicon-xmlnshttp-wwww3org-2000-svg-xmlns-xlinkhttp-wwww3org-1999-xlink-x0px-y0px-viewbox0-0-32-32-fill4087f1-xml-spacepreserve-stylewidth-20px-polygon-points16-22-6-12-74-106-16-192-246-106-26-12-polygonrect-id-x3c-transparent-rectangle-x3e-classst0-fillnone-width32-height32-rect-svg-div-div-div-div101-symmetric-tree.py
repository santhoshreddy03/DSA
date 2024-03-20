# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def inn(root):
            if not root:
                return 
            temp=root.left
            root.left=root.right
            root.right=temp
            inn(root.left)
            inn(root.right)
            return root
        def sym(p,q):
            if not p and not q:
                return True
            if p and not q:
                return False
            if not p and q:
                return False
            if p.val!=q.val:
                return False
            return sym(p.left,q.left) and sym(p.right,q.right)
        return sym(root.left,inn(root.right))
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#             if not root1.left and not root1.right and not root2.left and not root2.right:
#                 if root1.val==root2.val:
#                     return True
#                 return False

            
#             if root1.left and root2.right and root1.left.val==root2.right.val:
#                 return sym(root1.left,root2.right)
#             if root1.right and root2.left and root1.right.val==root2.left.val:
#                 return sym(root1.right,root2.left)
#             if (not root1.left and root2.right) or (not root1.right and root2.left):
#                 return False
#         return sym(root.left,root.right)
