# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS 

        # empty tree nothing to invert
        if not root: 
            return root
        
        # queue to store the nodes
        queue = deque([root])
        
        # swap each node's left and right child 
        while queue:
            curr = queue.popleft()
            curr.left, curr.right = curr.right, curr.left
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        # return the root after inverting all children nodes
        return root

        







        