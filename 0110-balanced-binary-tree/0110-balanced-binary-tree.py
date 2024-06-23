# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        return self.height(root)!=-1
        
    def height(self,root):
        if not root:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)


        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1


        return 1+max(left,right)

        
        
#         if not root:
#             return True
        
        
#         leftheight=self.height(root.left)
#         rightheight=self.height(root.right)
#         if abs(leftheight-rightheight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
#             return True
#         return False
    
#     def height(self,root):
#         if not root:
#             return 0
#         return 1+max(self.height(root.left),self.height(root.right))