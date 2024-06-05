class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        prev=Counter(words[0])
        for i in range(1,len(words)):
            curr=Counter(words[i])
            temp={}
            for i in curr:
                if i in prev:
                    temp[i]=min(prev[i],curr[i])
            prev=temp
        arr=[]
        for i in temp:
            arr+=[i]*temp[i]
        return arr