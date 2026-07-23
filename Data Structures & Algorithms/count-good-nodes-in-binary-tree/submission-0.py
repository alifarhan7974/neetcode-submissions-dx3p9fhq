# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None: 
            return 0 

        count = 1 

        def dfs(biggest, node): 
            nonlocal count 
            if node == None: 
                return 

            # Good path 
            if node.val >= biggest: 
                count += 1 

            dfs(max(biggest, node.val), node.right)
            dfs(max(biggest, node.val), node.left)

        dfs(root.val, root.left)
        dfs(root.val, root.right)
        return count 



            
        