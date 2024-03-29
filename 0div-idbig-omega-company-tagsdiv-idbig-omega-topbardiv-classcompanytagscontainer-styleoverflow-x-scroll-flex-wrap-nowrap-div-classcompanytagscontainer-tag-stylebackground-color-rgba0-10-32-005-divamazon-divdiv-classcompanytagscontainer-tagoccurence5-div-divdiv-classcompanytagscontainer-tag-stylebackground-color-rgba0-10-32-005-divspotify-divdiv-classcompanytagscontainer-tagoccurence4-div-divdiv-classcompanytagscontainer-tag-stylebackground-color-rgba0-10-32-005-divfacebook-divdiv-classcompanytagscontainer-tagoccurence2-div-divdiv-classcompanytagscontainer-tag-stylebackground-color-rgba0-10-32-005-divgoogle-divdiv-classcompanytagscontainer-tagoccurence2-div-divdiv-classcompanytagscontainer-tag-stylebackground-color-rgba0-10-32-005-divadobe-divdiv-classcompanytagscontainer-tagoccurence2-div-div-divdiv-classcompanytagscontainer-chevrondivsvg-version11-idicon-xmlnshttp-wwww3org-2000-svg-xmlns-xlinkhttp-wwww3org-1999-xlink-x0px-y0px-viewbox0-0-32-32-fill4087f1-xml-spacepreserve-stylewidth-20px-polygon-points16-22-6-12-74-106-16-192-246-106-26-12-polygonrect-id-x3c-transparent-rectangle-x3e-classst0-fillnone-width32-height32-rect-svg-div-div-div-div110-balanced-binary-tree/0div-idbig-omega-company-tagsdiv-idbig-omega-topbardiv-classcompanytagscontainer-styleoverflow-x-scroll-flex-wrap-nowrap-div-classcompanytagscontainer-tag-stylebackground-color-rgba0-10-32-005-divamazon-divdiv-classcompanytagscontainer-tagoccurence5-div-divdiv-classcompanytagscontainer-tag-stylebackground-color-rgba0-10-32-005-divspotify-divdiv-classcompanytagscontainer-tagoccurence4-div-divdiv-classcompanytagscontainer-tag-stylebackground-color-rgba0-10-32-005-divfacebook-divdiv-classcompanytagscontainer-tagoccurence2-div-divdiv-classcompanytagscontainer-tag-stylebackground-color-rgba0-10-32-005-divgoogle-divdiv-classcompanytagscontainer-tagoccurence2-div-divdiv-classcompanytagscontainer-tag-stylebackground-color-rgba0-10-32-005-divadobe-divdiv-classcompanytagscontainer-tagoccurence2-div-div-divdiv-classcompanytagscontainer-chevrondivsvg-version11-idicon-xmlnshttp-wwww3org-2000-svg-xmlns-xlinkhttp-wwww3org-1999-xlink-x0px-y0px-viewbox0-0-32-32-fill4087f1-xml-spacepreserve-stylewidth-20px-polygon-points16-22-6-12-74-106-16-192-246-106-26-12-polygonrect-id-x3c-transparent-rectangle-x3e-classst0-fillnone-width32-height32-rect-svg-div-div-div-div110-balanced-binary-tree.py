# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def dif(root):
            nonlocal ans
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            left=dif(root.left)
            right=dif(root.right)
            if abs(left-right)>1:
                ans=False
            
            return 1+max(left,right)
        dif(root)
        return ans
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def d(root):
#             if not root:
#                 return True
#             a=d(root.left)
#             if abs(dif(root.left)-dif(root.right)) >1:
#                 print(root.val)
#                 return False
#             b=d(root.right)
#             return a and b
            
#         def dif(root):
#             if not root:
#                 return 0
#             if not root.left and not root.right:
#                 return 1
#             return max(dif(root.left),dif(root.right))+1
        
#         return d(root)

            
