# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res=[]
        q=collections.deque()
        q.append(root)
        lev=[]
        while q:
            qlen=len(q)
            level=[]
            for i in range(qlen):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                
                a=0
                for i in range(len(level)):
                    a+=level[i]
                    
                    if i==len(level)-1:
                        a=a/len(level)
                        lev=a
                res.append(lev)
        return res