# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums=[]
        def kk(root):
            nonlocal nums
            if not root:
                return
            nums.append(root.val)
            kk(root.left)
            kk(root.right)
            return nums
        kk(root)
        nums.sort()

        return nums[k-1]
