# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        curr=dummy
        while curr and curr.next:
            if curr.next.val==val:
                curr.next=curr.next.next
            else:
                curr=curr.next
        return dummy.next
        
        
        
#         if head==None:
#             return None
#         prev=head
#         curr=head.next
#         good=head
#         if good.val==val:
#             good.next=None

#         while curr:
#             if curr.val==val:
#                 prev.next=curr.next
#                 curr.next=None
#                 curr=prev.next
                
#             else:
#                 prev=prev.next
#                 curr=curr.next
        
#         return head

    
            
