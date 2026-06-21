"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {} # original : copy Node 

        def dfs(node): 
            if node in created: 
                return created[node]

            copy = Node(node.val)
            created[node] = copy # started processing this node

            for nei in node.neighbors: 
                copy.neighbors.append(dfs(nei))
                    
            return copy 
            
        return None if not node else dfs(node) 
        
        