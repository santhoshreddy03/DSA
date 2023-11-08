# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ''''nums=[]
        while head:
            nums.append(head.val)
            head=head.next
        l,r=0,len(nums)-1
        while l<=r:
            if nums[l] != nums[r]:
                return False
            l +=1
            r -=1
        return True '''
        
        slow,fast=head,head.next
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev,curr=None,slow.next
        slow.next=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
    
        while head and prev:
            if head.val !=prev.val:
                return False
            head=head.next
            prev=prev.next
        return True

            
        