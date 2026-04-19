# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursive DFS
        if not root:
            return True

        # no node
        
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left == -1:
                return -1
            if right == -1:
                return -1
            diff = abs(left - right)
            
            if diff > 1:
                return -1
            
            return 1+ max(left,right)
        
        # recursively get height of left and right side, and compare at curr node if it is balanced 
        res = dfs(root)
        if res == -1:
            return False
        # compare left and right height and return True if they are within 1 height differance or equal
        return True