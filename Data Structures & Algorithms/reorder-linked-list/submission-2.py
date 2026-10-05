# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head
        slow=head

        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        curr=second
        prev=None   
        while curr is not None:
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        head1=head
        mid1=prev
        while  mid1 is not None:
            data=head1.next
            tmp2=mid1.next

            head1.next=mid1
            mid1.next=data

            head1=data
            mid1=tmp2
