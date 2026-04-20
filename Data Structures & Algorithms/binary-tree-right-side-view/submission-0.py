# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # res list
        res = []

        # BFS deque, append right val at every height until right is none and then append right of left side
        queue = deque([root])
        while queue:
            level = len(queue)

            for i in range(level):
                print(i)
                curr = queue.popleft()
                if i == level-1:
                    res.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
        return res