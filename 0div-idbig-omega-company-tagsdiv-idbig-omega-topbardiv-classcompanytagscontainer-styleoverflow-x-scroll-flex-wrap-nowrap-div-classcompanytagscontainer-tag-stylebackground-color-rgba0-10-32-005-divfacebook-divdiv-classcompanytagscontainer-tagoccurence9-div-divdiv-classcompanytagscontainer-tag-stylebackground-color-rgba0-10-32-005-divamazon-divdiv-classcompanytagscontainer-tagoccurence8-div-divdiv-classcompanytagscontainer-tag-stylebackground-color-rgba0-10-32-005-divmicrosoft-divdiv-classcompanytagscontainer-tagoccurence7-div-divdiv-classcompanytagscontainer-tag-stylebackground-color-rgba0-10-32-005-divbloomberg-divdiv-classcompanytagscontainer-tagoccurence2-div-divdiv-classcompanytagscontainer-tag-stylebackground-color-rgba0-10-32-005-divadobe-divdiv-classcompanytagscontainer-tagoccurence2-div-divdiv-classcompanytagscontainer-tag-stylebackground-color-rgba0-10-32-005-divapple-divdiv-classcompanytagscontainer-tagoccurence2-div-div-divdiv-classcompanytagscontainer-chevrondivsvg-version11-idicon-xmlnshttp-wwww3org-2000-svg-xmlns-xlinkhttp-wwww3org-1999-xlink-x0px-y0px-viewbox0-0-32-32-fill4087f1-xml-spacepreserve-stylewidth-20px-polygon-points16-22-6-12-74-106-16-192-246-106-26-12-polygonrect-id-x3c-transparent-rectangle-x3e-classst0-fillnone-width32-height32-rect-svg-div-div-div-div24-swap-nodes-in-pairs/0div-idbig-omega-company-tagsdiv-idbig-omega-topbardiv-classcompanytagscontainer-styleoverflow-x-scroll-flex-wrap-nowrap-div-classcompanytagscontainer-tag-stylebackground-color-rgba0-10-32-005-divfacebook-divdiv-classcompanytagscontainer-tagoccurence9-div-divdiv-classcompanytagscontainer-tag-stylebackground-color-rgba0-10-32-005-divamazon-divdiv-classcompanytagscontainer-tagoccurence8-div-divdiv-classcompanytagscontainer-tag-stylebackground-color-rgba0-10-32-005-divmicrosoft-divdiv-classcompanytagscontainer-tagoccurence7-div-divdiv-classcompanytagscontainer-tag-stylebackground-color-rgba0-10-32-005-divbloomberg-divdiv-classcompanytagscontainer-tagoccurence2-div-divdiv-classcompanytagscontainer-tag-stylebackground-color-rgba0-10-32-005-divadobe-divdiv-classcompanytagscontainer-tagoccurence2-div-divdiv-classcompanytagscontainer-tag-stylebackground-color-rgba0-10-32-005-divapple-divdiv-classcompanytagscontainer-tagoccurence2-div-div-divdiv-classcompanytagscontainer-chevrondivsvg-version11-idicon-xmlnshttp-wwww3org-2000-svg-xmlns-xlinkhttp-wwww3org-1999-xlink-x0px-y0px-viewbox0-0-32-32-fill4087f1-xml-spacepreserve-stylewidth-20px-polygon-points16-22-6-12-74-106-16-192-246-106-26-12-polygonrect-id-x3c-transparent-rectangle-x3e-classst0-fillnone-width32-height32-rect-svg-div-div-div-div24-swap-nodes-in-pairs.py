# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        b=head
        c=0
        while b:
            b=b.next
            c+=1
        for i in range(0 , c//2):
            a=curr.val
            curr.val=curr.next.val
            curr.next.val=a
            curr=curr.next.next
        return head