class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dict1={}
        count=0
        for i in range(len(text)):
            dict1[text[i]]=dict1.get(text[i],0)+1
        if "l" in dict1 and 'o' in dict1:
            dict1["l"] = dict1["l"]//2
            dict1["o"] = dict1["o"]//2

        keys=['b','a','l','o','n']
        
        values=[dict1[key] for key in keys if key in dict1]
        for i in range(len(keys)):
            if keys[i] in dict1:
                count+=1
            
        if count==5:
            return min(values)
        else:
            return 0