# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursion
        
        # base case, not a valid node
        if not root:
            return None

        # inverting children nodes if node is valid
        root.left, root.right = root.right, root.left

        # recusive step, pass the children of left and right
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        

        
        