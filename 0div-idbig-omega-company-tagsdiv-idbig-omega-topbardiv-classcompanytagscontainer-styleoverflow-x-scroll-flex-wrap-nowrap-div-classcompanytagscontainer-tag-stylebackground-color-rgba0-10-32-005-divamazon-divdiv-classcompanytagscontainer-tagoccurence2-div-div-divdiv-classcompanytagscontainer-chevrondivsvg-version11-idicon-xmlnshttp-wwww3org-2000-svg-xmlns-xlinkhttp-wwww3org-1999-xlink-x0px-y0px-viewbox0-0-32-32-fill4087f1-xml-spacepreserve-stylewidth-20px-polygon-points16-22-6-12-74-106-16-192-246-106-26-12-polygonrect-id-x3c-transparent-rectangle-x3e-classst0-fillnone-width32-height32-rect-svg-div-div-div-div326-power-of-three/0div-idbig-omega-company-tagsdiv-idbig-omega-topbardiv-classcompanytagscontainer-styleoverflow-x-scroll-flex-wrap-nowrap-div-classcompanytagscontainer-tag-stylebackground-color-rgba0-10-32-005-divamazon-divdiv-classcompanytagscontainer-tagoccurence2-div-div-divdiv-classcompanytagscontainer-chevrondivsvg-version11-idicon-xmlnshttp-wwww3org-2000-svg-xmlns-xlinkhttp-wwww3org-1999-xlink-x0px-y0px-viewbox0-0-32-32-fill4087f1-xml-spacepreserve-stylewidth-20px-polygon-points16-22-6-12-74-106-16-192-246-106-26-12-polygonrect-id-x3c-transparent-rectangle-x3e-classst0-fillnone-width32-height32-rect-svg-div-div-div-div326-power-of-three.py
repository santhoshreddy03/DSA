class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(i):
            if 3 ** i == n:
                return True
            if 3** i >n :
                return False
            return rec(i+1)
        return rec(0)
        