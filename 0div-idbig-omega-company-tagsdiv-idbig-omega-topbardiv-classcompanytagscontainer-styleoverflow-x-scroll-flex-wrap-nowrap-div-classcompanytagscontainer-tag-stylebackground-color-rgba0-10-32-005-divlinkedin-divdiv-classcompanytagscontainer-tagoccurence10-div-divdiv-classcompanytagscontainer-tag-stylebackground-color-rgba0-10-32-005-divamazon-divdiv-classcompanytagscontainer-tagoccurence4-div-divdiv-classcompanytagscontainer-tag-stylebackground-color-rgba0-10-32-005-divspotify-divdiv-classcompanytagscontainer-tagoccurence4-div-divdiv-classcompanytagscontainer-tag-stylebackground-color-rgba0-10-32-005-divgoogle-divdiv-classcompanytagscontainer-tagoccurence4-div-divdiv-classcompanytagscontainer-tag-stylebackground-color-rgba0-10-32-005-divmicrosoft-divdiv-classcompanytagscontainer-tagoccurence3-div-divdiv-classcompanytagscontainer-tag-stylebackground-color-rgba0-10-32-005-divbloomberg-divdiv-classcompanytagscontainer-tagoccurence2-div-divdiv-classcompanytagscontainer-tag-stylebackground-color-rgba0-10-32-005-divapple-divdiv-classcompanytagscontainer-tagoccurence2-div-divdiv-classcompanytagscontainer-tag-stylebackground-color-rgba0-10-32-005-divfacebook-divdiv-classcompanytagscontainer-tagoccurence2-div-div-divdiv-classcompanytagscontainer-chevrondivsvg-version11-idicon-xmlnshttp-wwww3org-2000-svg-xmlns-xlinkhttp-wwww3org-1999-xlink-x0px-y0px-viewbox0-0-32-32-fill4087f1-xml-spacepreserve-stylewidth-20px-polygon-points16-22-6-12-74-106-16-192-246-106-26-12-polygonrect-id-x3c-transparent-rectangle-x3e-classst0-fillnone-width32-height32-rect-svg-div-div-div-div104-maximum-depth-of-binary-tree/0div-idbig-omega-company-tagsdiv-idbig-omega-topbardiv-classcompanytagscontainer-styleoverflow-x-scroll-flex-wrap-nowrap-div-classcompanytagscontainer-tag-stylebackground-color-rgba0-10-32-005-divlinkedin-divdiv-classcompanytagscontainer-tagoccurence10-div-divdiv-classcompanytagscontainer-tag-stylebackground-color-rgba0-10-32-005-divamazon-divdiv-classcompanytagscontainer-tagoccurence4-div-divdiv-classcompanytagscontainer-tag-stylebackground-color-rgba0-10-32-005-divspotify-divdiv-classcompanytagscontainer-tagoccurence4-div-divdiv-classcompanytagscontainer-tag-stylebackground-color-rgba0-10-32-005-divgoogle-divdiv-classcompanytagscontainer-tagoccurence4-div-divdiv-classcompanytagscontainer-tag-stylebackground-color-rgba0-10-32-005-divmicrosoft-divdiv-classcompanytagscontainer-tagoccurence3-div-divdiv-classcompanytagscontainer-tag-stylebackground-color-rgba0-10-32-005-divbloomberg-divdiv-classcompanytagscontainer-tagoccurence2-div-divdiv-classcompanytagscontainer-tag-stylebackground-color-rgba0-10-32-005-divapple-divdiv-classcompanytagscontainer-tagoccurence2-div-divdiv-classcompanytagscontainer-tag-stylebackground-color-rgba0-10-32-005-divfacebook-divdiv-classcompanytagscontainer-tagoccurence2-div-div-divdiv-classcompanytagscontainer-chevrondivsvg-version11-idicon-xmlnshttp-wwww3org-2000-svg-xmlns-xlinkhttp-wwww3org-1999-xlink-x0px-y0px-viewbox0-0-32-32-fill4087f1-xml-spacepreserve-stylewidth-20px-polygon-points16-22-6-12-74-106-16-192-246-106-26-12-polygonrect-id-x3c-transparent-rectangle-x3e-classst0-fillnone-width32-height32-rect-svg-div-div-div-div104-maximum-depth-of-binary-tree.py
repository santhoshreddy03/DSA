# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        c=0

        q=deque()
        if not root:
            return c

        q.append(root)
        while q:

            
            for i in range(len(q)):
                node=q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            c+=1
        return c
        