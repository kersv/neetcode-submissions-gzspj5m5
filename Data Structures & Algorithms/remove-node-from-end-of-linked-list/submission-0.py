# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # for this question
        # get length of list for index
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        print(length, head.val)

        
        # index to remove = len - n 
        rmIdx = length - n

        if rmIdx == 0:
            return head.next
        # iterate through and skip value at index to remove
        curr = head
        idx = 0
        while idx < rmIdx-1:
            curr = curr.next
            idx += 1
        curr.next = curr.next.next
        return head

            

        