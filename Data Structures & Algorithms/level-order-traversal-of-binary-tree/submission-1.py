# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = deque()
        q.append(root)
        
        while q:
            qlen = len(q) #makes sure we're going by level
            level = []

            for i in range(qlen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if level: res.append(level)
        
        return res
                
