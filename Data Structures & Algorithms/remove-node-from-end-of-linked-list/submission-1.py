# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        counter=0
        while current is not None:
            counter=counter+1
            current=current.next
        pointer=head
        if counter==n:
            return head.next
        for i in range (0,counter-n-1):
            print(pointer.val)
            pointer=pointer.next
        if pointer.next is not None:
            pointer.next=pointer.next.next

        return head
