# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left) #height of left subtree
            right = dfs(curr.right) #height of right subtree

            self.res = max(self.res, left + right) #if our current root node has larger diameter or if an existing one already does

            return 1 + max(left, right) #traverse up a parent
        
        dfs(root)

        return self.res

