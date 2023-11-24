# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        nums=[]
        a,b,c=head,head,head
        while a:
            if a.val<x:
                nums.append(a.val)
            a=a.next
        while b:
            if b.val>=x:
                nums.append(b.val)
            b=b.next
        i=0    
        while c:
            c.val=nums[i]
            i+=1
            c=c.next
        return head
        
            
            
        
        