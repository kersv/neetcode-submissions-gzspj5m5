# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS, at each node check left and right if left is less than curr node and right is greated than curr node

        def dfs(curr, minVal, maxVal):
            if not curr:
                return True

            if curr.val >= maxVal or curr.val <= minVal:
                return False
        
            return dfs(curr.left, minVal, curr.val) and dfs(curr.right, curr.val, maxVal)

        if root and not root.left and not root.right:
            return True
 
        


        return dfs(root,float('-inf'),float('inf'))
        
       
