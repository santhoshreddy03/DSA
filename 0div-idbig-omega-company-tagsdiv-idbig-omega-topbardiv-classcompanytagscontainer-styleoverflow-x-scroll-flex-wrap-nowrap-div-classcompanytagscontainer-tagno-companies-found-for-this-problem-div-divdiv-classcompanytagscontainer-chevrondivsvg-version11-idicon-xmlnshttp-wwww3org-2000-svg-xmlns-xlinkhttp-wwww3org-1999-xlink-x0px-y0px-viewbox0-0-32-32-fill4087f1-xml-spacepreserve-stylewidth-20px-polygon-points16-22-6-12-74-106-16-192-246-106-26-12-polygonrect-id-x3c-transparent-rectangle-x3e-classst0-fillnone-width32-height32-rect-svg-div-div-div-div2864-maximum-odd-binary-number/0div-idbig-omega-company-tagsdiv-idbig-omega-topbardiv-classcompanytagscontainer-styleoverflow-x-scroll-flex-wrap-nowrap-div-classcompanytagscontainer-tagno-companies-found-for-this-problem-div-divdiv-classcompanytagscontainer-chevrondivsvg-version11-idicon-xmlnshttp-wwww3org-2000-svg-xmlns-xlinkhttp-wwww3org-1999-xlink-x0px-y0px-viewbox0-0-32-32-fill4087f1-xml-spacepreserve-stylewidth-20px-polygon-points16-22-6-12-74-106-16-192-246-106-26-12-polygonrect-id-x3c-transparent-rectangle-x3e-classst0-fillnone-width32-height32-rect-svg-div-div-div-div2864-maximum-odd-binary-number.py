class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a=''
        x,y=s.count("1"),s.count("0")
        for i in range(x-1):
            a+="1"
        for j in range(y):
            a+="0"
        return a + "1"