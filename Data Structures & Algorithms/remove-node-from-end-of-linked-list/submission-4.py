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

        # moving fast pointer to set gap bewteen slow and fast
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        
        # positioning the slow window relative to the dummy node
        prev.next = slow

        # move everything by 1 until fast reach end of linkedlist
        while fast:
            fast = fast.next
            slow = slow.next
            prev = prev.next
        
        # reordering to remove n-th node
        prev.next = prev.next.next
        
        # returning new head
        return dummyNode.next