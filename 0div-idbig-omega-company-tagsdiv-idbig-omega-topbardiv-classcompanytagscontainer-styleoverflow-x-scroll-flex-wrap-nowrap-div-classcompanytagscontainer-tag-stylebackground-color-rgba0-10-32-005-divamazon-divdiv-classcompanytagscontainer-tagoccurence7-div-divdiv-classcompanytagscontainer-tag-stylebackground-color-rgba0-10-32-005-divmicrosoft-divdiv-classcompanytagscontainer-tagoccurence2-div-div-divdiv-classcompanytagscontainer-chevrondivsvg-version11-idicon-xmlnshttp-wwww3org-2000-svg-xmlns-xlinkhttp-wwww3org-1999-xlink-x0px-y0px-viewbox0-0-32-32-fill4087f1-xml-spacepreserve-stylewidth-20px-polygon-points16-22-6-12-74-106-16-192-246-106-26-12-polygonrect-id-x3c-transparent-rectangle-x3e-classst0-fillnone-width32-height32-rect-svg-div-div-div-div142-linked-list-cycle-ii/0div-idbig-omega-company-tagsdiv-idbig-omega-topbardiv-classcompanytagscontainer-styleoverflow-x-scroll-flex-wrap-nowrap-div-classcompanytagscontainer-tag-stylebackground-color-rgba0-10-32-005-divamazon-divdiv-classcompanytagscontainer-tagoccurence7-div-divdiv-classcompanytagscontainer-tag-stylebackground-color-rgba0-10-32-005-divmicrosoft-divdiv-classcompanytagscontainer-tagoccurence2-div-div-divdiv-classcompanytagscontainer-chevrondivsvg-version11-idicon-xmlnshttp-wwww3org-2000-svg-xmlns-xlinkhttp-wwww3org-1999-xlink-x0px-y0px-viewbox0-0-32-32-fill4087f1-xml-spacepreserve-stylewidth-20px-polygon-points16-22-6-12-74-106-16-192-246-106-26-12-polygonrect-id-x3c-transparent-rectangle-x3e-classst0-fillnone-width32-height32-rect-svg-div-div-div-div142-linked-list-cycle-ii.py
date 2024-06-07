# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # slow=head
        # fast=head
        # first=head
        # while fast and fast.next:
        #     slow=slow.next
        #     fast=fast.next.next
        #     if slow==fast:
        #         while slow!=first:
        #             first=first.next
        #             slow=slow.next
        #         return slow
        # return None
        
        temp=head
        hashset={}
        while temp:
            if temp in hashset:
                return temp
            else:
                hashset[temp]=True
            temp=temp.next
        return None
                
                
        