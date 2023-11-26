# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        
        a=head
        b=head
        c=0
        while a:
            c+=1
            a=a.next
        if c==1 or k==0 or k%c==0:
            return head
        
        if k>c:
            k= k%c
        f=c-k-1
        for i in range(f):
            b=b.next
        sec=b.next
        b.next=None
        z=sec
        while z.next:
            z=z.next
        z.next=head
        return sec
        
            
       

        