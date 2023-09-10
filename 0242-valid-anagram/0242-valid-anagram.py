class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count={}
        count1={}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] = count[s[i]] + 1
                
            else:
                count[s[i]] = 1
        for i in range(len(t)):
            if t[i] in count1:
                count1[t[i]] = count1[t[i]] + 1
                
            else:
                count1[t[i]] = 1
        return count==count1