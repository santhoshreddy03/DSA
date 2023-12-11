class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split(" ")
        dictt={}
        for i in range(len(list1)):
            dictt[list1[i][-1]] =list1[i][0:-1]
        m=len(dictt)
        k=''
        for i in range(m):
            k=k+" "+dictt[str(i+1)]
            
        return k[1:]
            
        
            
        