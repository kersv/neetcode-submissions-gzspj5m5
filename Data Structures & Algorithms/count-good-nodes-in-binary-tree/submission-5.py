# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Recursive DFS
        self.nodeCount = 0

        def dfs(curr, maxVal):
            if not curr:
                return 0
            if curr.val >= maxVal:
                self.nodeCount +=1
                maxVal = max(maxVal, curr.val)

            
            if curr.left:
                dfs(curr.left, maxVal)
            if curr.right:
                dfs(curr.right, maxVal)

        dfs(root, root.val)

        return self.nodeCount

