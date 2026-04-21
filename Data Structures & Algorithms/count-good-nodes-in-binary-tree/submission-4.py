# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # counter good nodes
        nodeCount = 0

        # BFS deque, get curr val and check if its greater than max value of prev nodes, increment counter if true
        queue = deque([(root, root.val)])
        while queue:
            node, curr_max = queue.popleft()
            print(node.val, curr_max)
            if node.val >= curr_max:
                nodeCount +=1
            curr_max = max(curr_max, node.val)
            if node.left:
                queue.append((node.left, curr_max))
            if node.right:
                queue.append((node.right, curr_max))
            
        # return counter 
        return nodeCount
        