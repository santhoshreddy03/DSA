class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashset=Counter(s)
        hashset2=Counter(t)
                
        if hashset==hashset2:
            return True
        else:
            return False