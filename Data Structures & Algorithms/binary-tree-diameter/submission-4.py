# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        #root: height of left subtree + right subtree
        #compare against max height

        self.maxH = 0

        def dfs(curr):
            if not curr:
                return 0
            
            leftH = dfs(curr.left)
            rightH = dfs(curr.right)

            dia = leftH + rightH

            if dia > self.maxH:
                self.maxH = dia
            
            return max(leftH, rightH) + 1
        
        dfs(root)

        return self.maxH
                