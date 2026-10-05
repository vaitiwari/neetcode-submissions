# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1=l1
        c2=l2
        list1=""
        list2=""
        dummyNode=ListNode(0)
        tail=dummyNode
        while c2 is not None:
            list2=list2+str(c2.val)
            c2=c2.next
        while c1 is not None:
            list1=list1+str(c1.val)
            c1=c1.next
        list2=int(list2[::-1])
        list1=int(list1[::-1])
        result=list1+list2
        print(str(result))
        for char in (str(result)[::-1]):
            tail.next=ListNode(int(char))
            tail=tail.next
        return dummyNode.next

