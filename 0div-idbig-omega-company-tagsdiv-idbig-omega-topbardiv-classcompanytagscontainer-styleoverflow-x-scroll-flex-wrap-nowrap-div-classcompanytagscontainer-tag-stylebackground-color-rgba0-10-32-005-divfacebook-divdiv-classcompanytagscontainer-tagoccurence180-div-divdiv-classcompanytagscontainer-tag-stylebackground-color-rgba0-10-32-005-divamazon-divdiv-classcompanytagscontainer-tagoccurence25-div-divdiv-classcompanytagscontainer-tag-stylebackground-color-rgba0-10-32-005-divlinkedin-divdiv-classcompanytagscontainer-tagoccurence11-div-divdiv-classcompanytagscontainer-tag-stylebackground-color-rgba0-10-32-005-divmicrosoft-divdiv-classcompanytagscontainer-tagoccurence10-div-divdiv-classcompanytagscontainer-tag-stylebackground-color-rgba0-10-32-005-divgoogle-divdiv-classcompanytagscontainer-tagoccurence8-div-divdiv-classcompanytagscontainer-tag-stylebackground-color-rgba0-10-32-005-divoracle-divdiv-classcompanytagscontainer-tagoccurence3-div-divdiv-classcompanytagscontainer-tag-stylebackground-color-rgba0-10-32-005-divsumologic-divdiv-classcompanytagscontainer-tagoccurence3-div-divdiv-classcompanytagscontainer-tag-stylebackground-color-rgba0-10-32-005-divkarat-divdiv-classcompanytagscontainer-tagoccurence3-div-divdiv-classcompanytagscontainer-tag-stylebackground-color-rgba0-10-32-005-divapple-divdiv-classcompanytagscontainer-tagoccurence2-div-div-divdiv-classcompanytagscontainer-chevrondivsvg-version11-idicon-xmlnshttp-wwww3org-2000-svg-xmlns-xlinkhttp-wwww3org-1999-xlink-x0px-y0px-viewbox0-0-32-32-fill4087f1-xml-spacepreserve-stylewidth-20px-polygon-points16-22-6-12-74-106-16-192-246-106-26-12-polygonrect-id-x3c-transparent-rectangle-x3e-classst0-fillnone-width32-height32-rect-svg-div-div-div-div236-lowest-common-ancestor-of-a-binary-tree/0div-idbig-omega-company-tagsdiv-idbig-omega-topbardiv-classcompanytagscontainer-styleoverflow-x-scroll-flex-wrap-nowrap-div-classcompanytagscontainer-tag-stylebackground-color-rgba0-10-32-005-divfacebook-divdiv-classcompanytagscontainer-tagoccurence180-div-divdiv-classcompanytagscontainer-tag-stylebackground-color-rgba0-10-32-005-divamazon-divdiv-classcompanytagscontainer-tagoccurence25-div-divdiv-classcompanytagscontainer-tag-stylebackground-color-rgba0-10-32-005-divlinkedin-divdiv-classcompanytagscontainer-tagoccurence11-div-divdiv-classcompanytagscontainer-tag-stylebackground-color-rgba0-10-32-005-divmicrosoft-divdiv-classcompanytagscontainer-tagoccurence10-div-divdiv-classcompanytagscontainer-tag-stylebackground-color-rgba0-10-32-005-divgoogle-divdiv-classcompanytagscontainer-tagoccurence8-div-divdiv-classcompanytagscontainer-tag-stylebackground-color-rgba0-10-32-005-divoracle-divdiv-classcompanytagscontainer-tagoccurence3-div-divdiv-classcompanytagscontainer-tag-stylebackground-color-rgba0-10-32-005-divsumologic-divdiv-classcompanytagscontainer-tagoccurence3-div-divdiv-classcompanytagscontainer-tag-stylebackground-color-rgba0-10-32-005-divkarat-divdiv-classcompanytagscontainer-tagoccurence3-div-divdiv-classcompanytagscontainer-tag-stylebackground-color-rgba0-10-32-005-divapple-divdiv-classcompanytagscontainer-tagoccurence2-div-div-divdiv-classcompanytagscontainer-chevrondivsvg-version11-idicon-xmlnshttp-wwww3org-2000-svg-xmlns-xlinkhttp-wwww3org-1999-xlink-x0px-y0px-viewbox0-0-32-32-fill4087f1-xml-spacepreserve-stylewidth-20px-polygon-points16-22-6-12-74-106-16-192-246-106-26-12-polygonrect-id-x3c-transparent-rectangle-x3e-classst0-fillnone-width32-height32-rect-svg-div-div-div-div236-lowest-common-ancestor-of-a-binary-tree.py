# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.lca(root,p,q)
    def lca(self,root,p,q):
        if not root:
            return None
        if root==p or root==q:
            return root
        left=self.lca(root.left,p,q)
        right=self.lca(root.right,p,q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None
    
        
        
            
            
        
        
        