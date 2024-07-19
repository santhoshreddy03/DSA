# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root==None:
#             return 0
#         return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

        depth=0
        q=deque()
        if not root:
            return depth
        q.append(root)
        
        while q:
            for i in range(len(q)):
                
                node=q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            
            depth+=1
        return depth













# #         c=0

# #         q=deque()
# #         if not root:
# #             return c

# #         q.append(root)
# #         while q:

            
# #             for i in range(len(q)):
# #                 node=q.popleft()

# #                 if node.left:
# #                     q.append(node.left)
# #                 if node.right:
# #                     q.append(node.right)

# #             c+=1
# #         return c
        