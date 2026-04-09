"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # hashmap to save value
        nodeMap = {}

        # reference to head
        curr = head

        # first pass, create new node with new address
        while curr:
            nodeMap[curr] = Node(curr.val)
            curr = curr.next

        # reset curr to head
        curr = head

        # second pass, relink both next and random pointer
        nodeMap[None] = None
        dummy = nodeMap[curr]
        while curr :
            currNode = nodeMap[curr]
            currNode.next = nodeMap[curr.next]
            currNode.random = nodeMap[curr.random]
            curr = curr.next

        return dummy
        
        

        
