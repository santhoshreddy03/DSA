class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l,r=max(weights),sum(weights)
        res=r
        
        def canship(cap):
            day=1
            capacity=cap
            for w in weights:
                if capacity-w<0:
                    day+=1
                    capacity=cap
                capacity-=w
            return day<=days
        while l<=r:
            cap=(l+r)//2
            
            if canship(cap):
                res=min(res,cap)
                r=cap-1
            else:
                l=cap+1
        return res
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         l,r=max(weights),sum(weights)
#         weights.sort()
#         while l<=r:
#             summ=0
#             da=0
#             m=(l+r)//2
#             for i in range(len(weights)):
#                 if summ+weights[i] == m:
#                     da += 1
#                     summ = 0
#                 elif summ + weights[i] > m:
#                     da += 1
#                     summ = weights[i];
#                 else:
#                     summ += weights[i]
#             if da==days:
#                 return m
#             if da<days:
                
#                 r=m
#             else:
#                 l=m
                
                
