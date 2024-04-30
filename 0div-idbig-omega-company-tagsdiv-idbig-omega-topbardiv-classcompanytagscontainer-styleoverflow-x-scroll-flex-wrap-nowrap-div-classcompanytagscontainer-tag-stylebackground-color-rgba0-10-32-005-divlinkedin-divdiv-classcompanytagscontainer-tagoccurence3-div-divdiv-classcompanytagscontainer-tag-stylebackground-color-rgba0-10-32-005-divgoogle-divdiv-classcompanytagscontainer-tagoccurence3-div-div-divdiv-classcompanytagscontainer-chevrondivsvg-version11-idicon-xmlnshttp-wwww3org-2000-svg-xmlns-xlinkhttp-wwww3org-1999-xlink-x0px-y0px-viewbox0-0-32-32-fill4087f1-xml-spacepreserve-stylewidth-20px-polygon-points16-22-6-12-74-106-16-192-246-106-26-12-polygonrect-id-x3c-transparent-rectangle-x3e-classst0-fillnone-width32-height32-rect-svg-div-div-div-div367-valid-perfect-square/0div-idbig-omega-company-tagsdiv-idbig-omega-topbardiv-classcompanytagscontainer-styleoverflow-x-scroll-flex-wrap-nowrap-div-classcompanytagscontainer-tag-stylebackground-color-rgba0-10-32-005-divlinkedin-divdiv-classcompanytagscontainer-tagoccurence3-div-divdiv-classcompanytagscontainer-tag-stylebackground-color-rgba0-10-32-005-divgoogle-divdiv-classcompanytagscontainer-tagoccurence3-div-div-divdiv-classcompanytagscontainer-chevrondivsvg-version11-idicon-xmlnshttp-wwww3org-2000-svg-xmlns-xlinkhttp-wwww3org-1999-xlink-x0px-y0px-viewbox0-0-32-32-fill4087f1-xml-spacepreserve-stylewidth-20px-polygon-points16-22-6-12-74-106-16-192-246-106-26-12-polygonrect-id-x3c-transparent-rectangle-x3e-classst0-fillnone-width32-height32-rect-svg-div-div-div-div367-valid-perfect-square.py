class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=0,num//2
        if num==1:
            return True
        while l<=r:
            m=(l+r)//2
            if m*m==num:
                return True
            if m*m>num:
                r=m-1
            else:
                l=m+1
        return False
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l,r=0,num
#         while l<=r:
#             mid=(l+r)//2
#             if mid*mid==num:
#                 return True
#             if mid*mid>num:
#                 r=mid-1
#             else:
#                 l=mid+1
#         return False
        