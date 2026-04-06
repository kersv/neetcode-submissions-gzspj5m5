# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # single pass 

        # dummynode 
        dummyNode = ListNode()
        prev = dummyNode

        slow = fast = head
        gap = 0
        while gap < n:
            fast = fast.next 
            gap +=1
        
        prev.next = slow

        while fast:
            fast = fast.next
            slow = slow.next
            prev = prev.next
        
        prev.next = prev.next.next

        return dummyNode.next