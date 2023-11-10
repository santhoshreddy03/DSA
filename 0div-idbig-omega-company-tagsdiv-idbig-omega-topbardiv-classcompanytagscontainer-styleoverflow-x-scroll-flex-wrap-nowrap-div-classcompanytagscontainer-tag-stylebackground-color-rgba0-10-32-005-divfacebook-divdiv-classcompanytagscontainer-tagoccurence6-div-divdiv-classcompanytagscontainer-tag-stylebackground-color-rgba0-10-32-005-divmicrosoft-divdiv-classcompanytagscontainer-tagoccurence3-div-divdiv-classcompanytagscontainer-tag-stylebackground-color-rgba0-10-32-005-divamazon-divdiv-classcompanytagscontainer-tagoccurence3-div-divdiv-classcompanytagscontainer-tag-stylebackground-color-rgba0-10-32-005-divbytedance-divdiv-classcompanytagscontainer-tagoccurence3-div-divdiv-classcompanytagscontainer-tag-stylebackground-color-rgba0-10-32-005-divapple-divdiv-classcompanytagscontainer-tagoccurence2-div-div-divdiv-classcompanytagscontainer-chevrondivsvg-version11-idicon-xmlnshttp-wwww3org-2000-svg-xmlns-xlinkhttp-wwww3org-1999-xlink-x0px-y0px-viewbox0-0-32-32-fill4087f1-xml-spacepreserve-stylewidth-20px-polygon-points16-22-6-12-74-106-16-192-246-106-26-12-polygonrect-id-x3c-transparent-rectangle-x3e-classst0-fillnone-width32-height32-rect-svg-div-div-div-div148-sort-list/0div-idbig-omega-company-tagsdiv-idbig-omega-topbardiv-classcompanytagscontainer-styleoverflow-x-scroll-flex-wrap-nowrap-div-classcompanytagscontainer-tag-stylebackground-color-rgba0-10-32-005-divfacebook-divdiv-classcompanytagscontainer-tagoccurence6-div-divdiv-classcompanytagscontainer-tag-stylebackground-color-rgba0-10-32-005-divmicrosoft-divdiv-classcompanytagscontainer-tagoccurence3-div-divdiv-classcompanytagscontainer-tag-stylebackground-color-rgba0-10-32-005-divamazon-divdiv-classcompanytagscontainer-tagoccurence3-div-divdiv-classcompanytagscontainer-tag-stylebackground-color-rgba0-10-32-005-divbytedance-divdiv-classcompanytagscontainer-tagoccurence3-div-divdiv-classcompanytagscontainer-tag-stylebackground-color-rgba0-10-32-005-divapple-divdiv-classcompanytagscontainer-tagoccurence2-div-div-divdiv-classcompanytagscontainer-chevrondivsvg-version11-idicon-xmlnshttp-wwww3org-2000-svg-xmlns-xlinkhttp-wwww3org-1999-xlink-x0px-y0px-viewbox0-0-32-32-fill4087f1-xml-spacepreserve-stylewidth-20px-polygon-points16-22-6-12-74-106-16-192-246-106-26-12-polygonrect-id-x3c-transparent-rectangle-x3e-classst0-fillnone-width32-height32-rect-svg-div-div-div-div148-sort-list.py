# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=[]
        y=head
        x=head
        while head:
            nums.append(head.val)
            head=head.next
        nums.sort()
        for i in range(len(nums)):
            x.val=nums[i]
            x=x.next
        return y
        
        # curr=head
        # prev=head
        # while curr.next:
        #     if curr.val>curr.next.val:
        #         x=curr.next.next
        #         curr.next.next=curr
        #         curr.next=x
        #     else:
        #         curr=curr.next
        # return head
            
        # curr=head
        # nxt=head.next
        # while nxt.next and nxt:
        #     if nxt.val<curr.val:
        #         nxt=nxt.next
        #         curr.next.next=curr
        #         curr.next=nxt
        #     else:
        #         curr=curr.next
        #         nxt=nxt.next
        # return head
        
        
            