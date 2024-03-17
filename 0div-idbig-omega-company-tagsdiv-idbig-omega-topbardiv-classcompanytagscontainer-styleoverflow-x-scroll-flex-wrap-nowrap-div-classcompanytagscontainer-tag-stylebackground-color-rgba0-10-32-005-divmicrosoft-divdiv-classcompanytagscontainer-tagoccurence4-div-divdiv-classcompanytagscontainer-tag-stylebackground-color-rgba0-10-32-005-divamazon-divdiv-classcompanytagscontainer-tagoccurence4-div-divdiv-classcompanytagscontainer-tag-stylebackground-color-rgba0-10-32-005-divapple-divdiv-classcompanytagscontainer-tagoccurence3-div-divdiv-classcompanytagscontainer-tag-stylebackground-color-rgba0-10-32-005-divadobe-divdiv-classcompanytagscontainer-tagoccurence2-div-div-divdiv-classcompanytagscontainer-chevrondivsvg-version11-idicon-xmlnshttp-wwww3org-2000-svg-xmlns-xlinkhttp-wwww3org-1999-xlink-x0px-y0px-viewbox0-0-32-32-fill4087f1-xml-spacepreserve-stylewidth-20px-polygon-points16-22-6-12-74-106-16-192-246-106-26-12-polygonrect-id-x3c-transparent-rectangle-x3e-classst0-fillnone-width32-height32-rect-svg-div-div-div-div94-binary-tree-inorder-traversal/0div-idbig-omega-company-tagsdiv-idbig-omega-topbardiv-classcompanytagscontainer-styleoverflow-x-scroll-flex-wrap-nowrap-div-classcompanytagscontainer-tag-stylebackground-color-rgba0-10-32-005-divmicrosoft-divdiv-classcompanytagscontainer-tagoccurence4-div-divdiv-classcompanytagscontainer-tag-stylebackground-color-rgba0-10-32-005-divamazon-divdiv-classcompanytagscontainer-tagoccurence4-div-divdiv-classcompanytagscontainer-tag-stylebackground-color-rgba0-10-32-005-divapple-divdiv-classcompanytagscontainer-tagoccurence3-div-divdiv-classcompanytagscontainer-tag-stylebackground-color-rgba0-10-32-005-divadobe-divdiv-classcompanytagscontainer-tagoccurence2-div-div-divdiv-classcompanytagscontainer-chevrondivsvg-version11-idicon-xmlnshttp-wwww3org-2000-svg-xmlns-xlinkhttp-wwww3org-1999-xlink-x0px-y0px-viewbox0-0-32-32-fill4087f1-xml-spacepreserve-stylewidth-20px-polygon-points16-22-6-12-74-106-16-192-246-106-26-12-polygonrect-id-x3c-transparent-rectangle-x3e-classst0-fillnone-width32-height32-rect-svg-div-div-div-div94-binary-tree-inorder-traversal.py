# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def ino(root):

            if not root:
                return
            ino(root.left)
            res.append(root.val)
            ino(root.right)
            return res

        return ino(root)
        