# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head,head
        while fast:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        maa=0
        while prev:
            if prev.val+head.val > maa:
                maa=prev.val+head.val
            else:
                prev=prev.next
                head=head.next
        return maa
            
            
            
        
        