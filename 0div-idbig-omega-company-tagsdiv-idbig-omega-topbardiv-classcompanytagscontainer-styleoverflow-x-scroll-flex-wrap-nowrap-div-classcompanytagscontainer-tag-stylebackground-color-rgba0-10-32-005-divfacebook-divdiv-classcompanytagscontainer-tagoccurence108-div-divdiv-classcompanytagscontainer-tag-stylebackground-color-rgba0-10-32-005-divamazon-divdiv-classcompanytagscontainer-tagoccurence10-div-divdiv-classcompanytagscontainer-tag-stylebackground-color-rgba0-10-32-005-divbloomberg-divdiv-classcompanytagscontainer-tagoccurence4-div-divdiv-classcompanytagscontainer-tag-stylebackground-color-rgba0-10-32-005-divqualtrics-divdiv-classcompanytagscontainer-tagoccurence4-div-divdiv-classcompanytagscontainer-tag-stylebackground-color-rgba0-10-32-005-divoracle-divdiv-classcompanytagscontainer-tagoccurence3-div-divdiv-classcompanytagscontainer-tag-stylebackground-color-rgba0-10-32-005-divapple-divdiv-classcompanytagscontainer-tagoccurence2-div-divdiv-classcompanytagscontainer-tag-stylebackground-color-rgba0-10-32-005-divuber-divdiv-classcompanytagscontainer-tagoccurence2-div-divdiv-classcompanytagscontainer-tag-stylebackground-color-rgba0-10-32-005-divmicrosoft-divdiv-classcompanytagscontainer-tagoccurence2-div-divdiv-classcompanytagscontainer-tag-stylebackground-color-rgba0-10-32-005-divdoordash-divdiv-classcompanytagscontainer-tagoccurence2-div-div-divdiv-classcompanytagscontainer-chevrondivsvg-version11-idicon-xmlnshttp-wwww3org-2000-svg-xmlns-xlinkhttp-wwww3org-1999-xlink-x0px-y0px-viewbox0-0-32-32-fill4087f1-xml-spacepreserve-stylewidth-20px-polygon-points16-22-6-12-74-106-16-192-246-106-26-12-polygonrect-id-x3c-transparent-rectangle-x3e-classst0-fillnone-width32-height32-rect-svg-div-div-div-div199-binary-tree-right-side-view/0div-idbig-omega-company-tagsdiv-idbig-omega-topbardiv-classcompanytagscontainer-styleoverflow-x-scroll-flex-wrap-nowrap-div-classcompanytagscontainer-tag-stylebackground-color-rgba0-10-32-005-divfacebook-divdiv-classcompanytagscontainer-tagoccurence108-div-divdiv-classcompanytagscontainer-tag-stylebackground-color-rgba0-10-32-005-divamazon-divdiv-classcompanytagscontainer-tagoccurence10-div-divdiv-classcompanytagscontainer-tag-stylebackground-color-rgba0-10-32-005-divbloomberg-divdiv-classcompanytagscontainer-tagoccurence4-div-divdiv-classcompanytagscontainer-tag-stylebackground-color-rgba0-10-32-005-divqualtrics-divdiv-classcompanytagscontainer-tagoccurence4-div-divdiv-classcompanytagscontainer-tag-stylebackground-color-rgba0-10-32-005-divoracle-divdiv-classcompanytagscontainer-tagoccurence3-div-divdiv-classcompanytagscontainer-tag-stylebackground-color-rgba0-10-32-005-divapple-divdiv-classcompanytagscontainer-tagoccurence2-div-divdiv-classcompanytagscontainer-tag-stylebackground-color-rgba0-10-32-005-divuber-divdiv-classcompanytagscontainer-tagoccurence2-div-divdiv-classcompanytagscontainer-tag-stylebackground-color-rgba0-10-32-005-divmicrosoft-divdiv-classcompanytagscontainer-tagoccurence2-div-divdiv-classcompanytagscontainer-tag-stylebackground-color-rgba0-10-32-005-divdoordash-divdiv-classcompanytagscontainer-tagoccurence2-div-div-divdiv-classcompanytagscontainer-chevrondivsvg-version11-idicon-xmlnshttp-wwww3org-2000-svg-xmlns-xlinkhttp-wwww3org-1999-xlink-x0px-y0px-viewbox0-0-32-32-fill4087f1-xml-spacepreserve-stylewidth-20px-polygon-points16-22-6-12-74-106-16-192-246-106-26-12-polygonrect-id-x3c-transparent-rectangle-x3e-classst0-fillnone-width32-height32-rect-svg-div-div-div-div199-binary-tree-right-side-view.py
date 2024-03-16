# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=collections.deque()
        q.append(root)
        while q:
            qlen=len(q)
            level=[]
            rightside=None
            for i in range(qlen):
                node=q.popleft()
                if node:
                    rightside=node
                    q.append(node.left)
                    q.append(node.right)
            if rightside:
                res.append(rightside.val)
#                 if node:
#                     level.append(node.val)
#                     q.append(node.left)
#                     q.append(node.right)
#             if level:
    
#                 res.append(level[len(level)-1])
        return res
                    