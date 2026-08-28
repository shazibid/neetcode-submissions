"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        newNode = {}

        def dfs(node):
            #with dfs, youre using a stack, push children onto stack and pop as you move towards root, tree is explored once stack is empty
            if node in newNode:
                return newNode[node]
            
            #get value and store into dictionary, node value is the key
            copy = Node(node.val)
            newNode[node] = copy

            for child in node.neighbors:
                copy.neighbors.append(dfs(child))
            return copy
        
        return dfs(node)
        
        