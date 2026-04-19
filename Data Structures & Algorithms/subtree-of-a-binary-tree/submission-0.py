# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs recursive

        # dfs function, search for subroot start
        def dfsSearch(curr1, curr2):
            if not curr1:
                return False
            
            if curr1.val == curr2.val:
                if isSameTree(curr1, curr2):
                    return True

            return dfsSearch(curr1.left, curr2) or dfsSearch(curr1.right, curr2)

        # dfs 2nd function, compare values of subroot and root and positions
        def isSameTree(curr1, curr2):
            if not curr1 and not curr2:
                return True
            if not curr1 or not curr2:
                return False 
            if curr1.val != curr2.val:
                return False

            return isSameTree(curr1.left, curr2.left) and isSameTree(curr1.right, curr2.right)

        
        # return res of dfs    
        return dfsSearch(root, subRoot)
    