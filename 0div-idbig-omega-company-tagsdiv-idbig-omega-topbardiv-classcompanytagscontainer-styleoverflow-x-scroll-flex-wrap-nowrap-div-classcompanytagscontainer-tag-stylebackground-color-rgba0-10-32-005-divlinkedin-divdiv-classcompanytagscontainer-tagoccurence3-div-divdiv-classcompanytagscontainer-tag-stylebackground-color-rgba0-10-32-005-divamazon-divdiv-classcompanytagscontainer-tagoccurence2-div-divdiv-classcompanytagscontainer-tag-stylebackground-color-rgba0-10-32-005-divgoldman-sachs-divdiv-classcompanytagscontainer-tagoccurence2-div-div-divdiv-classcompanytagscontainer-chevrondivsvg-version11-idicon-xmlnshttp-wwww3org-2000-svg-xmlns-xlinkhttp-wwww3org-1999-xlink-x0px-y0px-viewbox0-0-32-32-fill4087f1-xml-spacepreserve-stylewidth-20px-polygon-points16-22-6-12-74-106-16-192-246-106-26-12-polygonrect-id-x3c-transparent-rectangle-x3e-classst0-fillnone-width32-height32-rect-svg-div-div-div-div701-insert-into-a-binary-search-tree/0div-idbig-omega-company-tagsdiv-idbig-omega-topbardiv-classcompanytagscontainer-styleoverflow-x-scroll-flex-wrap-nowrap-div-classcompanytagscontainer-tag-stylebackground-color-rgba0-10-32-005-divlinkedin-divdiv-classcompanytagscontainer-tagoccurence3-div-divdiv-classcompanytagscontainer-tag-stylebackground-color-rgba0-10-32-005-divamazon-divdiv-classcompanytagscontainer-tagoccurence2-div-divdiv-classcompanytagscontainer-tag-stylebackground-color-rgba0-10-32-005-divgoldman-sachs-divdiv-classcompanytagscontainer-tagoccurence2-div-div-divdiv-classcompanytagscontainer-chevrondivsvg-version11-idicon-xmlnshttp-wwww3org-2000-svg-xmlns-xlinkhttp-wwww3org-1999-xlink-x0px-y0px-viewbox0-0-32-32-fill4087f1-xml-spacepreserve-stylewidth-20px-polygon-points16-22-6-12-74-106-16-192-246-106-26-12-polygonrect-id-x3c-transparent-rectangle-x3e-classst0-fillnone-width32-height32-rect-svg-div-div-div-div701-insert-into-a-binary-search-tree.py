# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def inst(root):
            if not root:
                return TreeNode(val)

            if not root.left and val<root.val:
                root.left=TreeNode(val)
            if not root.right and val>root.val:
                root.right=TreeNode(val)
            if val<root.val:
                inst(root.left)
            if val>root.val:
                inst(root.right)
            return 
        if inst(root):
            return inst(root)

        return root

        