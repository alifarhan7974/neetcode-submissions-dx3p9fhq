# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = [0] 
        # Calculate height of left, right nodes update global 

        def dfs(node): 
            if node == None: 
                return 0 

            left = dfs(node.left)
            right = dfs(node.right)

            d[0] = max(d[0], left + right)

            return max(1 + left, 1 + right)

        dfs(root)
        return d[0]





        