class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        dict={}
        count=0
        for i in range(len(s)):
         
            if s[i] not in dict and t[i] not in dict.values():
                dict[s[i]]=t[i]
            
        for i in range(len(s)):
            if s[i] in dict and t[i] in dict.values():
                if dict[s[i]] == t[i]:
                    count+=1
        return count == len(s)
                    
            
                
                
        