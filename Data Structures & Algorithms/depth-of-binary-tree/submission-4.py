# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0
        
        stack = [[root, 1]]

        maxDep = 0

        while stack:
            node, depth = stack.pop()
            maxDep = max(maxDep, depth)

            currDepth = depth+1
            if node.left:
                stack.append([node.left, currDepth])
            if node.right:
                stack.append([node.right, currDepth])
        
        return maxDep
                    
