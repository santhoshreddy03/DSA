# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def path(root,summ):
            if not root:
                return 
            summ+=root.val
            if not root.left and not root.right:
                if targetSum==summ:
                    return True
                else:
                    summ-=root.val
                    return

            return (path(root.left,summ) or
                    path(root.right,summ))
            
        return path(root,0)
            
        