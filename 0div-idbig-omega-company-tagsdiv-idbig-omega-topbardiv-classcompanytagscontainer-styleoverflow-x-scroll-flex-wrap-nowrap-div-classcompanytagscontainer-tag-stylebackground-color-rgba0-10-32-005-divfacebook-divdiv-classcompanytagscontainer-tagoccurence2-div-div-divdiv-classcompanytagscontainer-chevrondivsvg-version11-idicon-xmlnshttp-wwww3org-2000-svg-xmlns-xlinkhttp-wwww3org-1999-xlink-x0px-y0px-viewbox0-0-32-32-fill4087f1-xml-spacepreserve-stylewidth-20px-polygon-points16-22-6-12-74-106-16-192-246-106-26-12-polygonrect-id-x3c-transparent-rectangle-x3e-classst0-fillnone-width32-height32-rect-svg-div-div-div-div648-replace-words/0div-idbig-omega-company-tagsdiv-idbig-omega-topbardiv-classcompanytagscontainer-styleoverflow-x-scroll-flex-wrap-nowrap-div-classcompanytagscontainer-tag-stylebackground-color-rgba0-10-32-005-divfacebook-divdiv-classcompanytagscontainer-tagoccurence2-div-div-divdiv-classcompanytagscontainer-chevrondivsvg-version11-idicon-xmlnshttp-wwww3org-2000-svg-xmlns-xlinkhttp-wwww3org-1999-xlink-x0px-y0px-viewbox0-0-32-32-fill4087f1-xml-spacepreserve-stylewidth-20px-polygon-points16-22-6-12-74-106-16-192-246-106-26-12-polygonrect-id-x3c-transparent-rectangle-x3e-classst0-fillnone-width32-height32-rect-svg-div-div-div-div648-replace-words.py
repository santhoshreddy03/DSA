class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        list=[]
        list=sentence.split()
        print(list)
        ans=[]
        for word in list:
            n,i,bol=len(word),0,False
            while i<n:
                
                if word[:i+1] in dictionary:
                    ans.append(word[:i+1])
                    bol=True
                    break
                i+=1

            if bol==False:
                ans.append(word)
        return " ".join(ans)
                
                    
            