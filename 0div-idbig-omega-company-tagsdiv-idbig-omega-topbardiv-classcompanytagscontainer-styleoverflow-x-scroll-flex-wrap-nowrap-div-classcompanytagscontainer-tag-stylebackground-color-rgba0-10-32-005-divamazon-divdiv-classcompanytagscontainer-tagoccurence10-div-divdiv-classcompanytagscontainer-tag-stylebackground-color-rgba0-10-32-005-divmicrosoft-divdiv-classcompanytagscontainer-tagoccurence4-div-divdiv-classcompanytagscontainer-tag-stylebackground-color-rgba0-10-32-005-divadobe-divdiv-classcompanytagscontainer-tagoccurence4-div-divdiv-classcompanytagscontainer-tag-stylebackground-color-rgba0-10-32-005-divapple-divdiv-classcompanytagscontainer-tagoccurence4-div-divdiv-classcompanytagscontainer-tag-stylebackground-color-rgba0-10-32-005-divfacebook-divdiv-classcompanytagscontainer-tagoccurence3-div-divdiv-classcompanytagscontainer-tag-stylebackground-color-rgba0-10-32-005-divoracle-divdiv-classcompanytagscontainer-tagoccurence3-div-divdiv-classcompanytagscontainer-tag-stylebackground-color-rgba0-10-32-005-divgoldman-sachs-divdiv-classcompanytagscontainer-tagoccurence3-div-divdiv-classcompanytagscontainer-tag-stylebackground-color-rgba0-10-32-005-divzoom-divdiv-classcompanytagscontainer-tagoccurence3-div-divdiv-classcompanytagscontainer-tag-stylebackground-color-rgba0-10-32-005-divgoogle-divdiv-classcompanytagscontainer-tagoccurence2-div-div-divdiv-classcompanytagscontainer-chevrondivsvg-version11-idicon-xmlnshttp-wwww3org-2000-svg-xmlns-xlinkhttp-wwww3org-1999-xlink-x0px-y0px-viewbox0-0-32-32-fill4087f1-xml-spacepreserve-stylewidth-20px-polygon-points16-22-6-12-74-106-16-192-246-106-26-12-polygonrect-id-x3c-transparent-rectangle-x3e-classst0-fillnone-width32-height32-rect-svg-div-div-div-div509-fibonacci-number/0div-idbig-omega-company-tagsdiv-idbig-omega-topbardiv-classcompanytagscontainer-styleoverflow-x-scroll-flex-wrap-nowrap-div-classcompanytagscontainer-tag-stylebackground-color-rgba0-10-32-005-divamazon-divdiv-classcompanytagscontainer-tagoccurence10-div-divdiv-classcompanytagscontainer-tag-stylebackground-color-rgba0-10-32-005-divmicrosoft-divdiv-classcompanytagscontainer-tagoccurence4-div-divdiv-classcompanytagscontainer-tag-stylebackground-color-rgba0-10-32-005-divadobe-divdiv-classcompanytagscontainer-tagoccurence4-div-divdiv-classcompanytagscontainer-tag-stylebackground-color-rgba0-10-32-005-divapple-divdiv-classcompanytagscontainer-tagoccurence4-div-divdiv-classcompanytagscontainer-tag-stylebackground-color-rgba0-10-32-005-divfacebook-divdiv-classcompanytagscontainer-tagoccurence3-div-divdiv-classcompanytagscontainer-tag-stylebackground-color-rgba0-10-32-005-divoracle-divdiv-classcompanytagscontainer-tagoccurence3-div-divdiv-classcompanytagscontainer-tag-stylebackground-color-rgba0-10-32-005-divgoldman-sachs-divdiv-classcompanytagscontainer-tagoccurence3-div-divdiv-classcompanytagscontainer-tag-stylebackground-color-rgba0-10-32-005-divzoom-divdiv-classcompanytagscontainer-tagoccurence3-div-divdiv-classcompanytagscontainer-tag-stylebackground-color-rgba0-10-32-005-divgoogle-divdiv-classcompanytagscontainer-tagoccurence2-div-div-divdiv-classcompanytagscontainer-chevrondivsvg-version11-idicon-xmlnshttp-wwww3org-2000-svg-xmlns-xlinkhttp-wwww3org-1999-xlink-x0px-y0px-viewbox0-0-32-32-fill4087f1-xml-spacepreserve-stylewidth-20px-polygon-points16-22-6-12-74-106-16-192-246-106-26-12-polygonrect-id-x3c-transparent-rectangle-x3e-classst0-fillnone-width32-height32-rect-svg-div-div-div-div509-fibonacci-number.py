class Solution:
    def fib(self, n: int) -> int:
        def fibb(i):
        
            if i==1:
                return 1
            if i==0:
                return 0
            return fibb(i-1)+fibb(i-2)
        return fibb(n)

            
        