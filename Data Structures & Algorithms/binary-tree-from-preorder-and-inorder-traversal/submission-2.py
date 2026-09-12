# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val : i for i, val in enumerate(inorder)}
        preorder_index = 0 

        def build(inorder_left, inorder_right): 
            nonlocal preorder_index

            if inorder_left > inorder_right: 
                return None

            # Find curr root 
            root_val = preorder[preorder_index]
            preorder_index += 1 

            # find inorder mid index 
            mid = inorder_map[root_val]

            # Create node 
            node = TreeNode(root_val)
            
            node.left = build(inorder_left, mid - 1)
            node.right = build(mid + 1, inorder_right)

            return node

        return build(0, len(inorder) - 1)
