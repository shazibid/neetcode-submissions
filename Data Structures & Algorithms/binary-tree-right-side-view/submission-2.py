# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = []
        q = deque()
        q.append(root)

        while q:
            lvl = []
            length = len(q)


            for i in range(length):
                node = q.popleft()
                lvl.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            if lvl:
                levels.append(lvl)
        
        res = []

        for i in levels:
            res.append(i[-1])
        
        return res