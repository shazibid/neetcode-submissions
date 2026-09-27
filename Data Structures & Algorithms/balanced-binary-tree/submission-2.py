# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #dfs
        #checking the difference of heights of left and right subtrees is <= 1
        def dfs(curr): #track heights
            if not curr:
                return 0 #we have hit the end of that tree
            
            #calculate our heights of l and r subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:
                return -1000
            
            return max(left, right) + 1
        
        num = dfs(root)

        if num < 0:
            return False
        return True
        
        
            