class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def rec(i):
            if 2**i == n:
                return True
            if 2**i > n:
                return False
            return rec(i+1)
        return rec(0)
        
            
            