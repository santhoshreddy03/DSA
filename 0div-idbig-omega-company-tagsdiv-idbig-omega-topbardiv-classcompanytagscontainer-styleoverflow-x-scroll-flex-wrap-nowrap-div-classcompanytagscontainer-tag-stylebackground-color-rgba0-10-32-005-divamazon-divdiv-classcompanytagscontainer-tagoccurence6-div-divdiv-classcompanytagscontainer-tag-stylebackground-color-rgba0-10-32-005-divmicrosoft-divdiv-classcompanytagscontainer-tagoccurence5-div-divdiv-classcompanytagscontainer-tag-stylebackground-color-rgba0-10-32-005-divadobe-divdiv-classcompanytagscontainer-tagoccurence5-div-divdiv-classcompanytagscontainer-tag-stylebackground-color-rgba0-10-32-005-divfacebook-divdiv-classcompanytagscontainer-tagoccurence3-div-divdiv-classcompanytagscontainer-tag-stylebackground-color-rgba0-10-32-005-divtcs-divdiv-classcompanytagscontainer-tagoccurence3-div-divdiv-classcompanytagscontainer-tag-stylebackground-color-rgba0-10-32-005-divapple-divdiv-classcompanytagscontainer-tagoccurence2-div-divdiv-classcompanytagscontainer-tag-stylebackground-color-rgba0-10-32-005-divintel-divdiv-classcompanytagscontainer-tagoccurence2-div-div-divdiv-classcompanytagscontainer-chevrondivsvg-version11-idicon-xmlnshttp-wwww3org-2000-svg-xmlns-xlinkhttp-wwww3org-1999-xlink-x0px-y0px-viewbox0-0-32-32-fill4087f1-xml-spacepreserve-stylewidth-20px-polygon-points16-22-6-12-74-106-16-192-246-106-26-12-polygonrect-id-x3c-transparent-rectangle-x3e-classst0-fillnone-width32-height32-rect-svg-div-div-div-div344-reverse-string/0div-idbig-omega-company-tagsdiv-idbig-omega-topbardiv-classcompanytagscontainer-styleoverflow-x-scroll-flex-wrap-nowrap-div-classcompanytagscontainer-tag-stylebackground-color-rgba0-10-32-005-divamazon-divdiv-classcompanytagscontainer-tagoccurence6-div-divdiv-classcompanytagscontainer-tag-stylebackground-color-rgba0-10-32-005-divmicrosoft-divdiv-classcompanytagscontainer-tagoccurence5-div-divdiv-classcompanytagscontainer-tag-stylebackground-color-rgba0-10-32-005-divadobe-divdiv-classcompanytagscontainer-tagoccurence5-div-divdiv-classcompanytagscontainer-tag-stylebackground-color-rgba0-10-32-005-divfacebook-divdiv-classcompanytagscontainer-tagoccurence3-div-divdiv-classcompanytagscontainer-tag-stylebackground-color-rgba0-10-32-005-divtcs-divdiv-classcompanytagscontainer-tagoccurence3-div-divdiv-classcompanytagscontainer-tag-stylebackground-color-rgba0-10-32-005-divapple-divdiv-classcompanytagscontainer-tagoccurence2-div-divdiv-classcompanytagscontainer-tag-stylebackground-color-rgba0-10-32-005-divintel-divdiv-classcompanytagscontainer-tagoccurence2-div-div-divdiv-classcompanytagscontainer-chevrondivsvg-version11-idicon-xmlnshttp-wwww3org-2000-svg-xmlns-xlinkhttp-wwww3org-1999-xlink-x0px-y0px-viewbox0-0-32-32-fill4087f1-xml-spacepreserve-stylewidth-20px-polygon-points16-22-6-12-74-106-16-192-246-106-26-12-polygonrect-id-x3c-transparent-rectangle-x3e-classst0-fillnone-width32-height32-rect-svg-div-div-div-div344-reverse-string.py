class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def sw(i):
            if i==len(s)//2:
                return

            temp=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-1-i]=temp
            sw(i+1)
        sw(0)
        