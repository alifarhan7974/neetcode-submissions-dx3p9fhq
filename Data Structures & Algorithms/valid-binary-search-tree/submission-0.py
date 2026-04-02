# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pos_inf = float('inf')
        neg_inf = float('-inf')

        def helper(node, min_val, max_val): 
            if node == None: 
                return True 
            valid = min_val < node.val < max_val
            return valid \
            and helper(node.left, min_val, node.val) \
            and helper(node.right, node.val, max_val)


        return helper(root, neg_inf, pos_inf)
            