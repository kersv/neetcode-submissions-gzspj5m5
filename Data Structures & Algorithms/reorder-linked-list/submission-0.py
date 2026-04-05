# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # get middle and last node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

    
        # reverse mid to end list
        prev = None
        curr = slow.next
        slow.next = prev
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # zip through and point to head.next to fast and back to original next
        first = head
        second = prev
        while first and second:
            nxt = first.next
            secNxt = second.next
            first.next = second
            second.next = nxt
            first = nxt
            second = secNxt
        
        

            
            
