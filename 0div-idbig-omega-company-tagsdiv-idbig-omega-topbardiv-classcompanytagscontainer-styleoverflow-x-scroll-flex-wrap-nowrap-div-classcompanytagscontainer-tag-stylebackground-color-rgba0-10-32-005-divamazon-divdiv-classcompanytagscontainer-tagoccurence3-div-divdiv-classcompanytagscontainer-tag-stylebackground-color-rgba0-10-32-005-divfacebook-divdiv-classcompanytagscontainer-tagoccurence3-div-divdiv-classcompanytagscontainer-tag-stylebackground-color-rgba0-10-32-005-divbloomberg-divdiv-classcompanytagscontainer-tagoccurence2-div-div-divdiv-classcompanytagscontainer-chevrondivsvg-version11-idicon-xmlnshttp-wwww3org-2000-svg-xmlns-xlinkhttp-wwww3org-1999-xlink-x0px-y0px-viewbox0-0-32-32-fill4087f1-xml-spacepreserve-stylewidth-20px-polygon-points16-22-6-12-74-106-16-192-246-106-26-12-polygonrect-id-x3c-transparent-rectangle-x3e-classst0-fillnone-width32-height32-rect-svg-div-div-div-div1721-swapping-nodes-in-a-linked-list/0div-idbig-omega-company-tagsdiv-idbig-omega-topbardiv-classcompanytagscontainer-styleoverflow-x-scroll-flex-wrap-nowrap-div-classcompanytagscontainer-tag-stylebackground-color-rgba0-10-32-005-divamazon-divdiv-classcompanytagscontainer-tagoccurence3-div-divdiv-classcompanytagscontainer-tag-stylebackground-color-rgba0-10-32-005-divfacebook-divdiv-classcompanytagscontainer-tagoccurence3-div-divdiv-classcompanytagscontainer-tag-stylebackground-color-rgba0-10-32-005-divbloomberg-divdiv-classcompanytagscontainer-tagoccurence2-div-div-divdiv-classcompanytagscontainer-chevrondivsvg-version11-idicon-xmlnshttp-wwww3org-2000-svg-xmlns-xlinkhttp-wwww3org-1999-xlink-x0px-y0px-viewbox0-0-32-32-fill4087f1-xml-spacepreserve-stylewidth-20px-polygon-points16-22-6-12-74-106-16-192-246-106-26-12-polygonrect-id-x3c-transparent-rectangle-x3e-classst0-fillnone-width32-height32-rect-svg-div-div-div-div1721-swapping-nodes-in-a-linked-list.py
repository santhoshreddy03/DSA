# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        a=head
        b=head
        d=head
        c=0
        for i in range(k-1):
            a=a.next
        while b:
            b=b.next
            c+=1
        for i in range(c-k):
            d=d.next
        f=a.val
        a.val=d.val
        d.val=f
        return head
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         a=head
#         b=head
#         final=head
#         c=0
#         while b:
#             c+=1
#             b=b.next

#         nums=[]
        
#         while a:
#             nums.append(a.val)
#             a=a.next


#         right=nums[k-1]
#         nums[k-1]=nums[c-k]
#         nums[c-k]=right
#         print(nums)
#         for i in nums:
#             head.val=i
#             head=head.next
#         return final
            

        
        