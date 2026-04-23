# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs
        stack = []

        curr = root
        popCount = 0
        while curr or stack:
            # left append
            while curr:
                stack.append(curr)
                curr = curr.left
            # keep popping left until stack is empty
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            curr = node.right
            
            
