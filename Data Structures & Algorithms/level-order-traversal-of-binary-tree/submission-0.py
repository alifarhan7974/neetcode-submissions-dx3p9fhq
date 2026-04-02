# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root): 
            if root is None: 
                return [] 

            queue = [root]
            level_order = []

            while queue: 
                #print([node.val for node in queue])
                curr_level = []
                
                for _ in range(len(queue)): 
                    node = queue.pop(0)
                    curr_level.append(node.val)
                    if node.left: 
                        queue.append(node.left)
                        #curr_level.append(node.left.val)
                    if node.right: 
                        queue.append(node.right)
                        #curr_level.append(node.right.val)
                
                level_order.append(curr_level)

            return level_order

        return bfs(root)