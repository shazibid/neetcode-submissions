# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # !) depth left - depth right abs > 1 false
        # lvl by lvl if height l - r
        if not root:
            return True

        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            #hL - Hr abs < 2

            if left == -1 or right == -1:
                return -1
            if abs(left - right) >= 2:
                return -1
            else:
                return max(left, right) + 1
        
        answer = dfs(root)

        if answer == -1:
            return False
            
        return True
