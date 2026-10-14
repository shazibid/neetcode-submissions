# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #tail end of the lvl order

        if not root:
            return []

        levels = []
        q = deque()
        q.append(root)

        while q:
            length = len(q)
            lvl = []

            for i in range(length):
                curr = q.popleft()
                lvl.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            
            if lvl:
                levels.append(lvl)

            #append left and right children
            #append to the level left then right child
        
        res = []

        for i in levels:
            res.append(i[-1])

        return res