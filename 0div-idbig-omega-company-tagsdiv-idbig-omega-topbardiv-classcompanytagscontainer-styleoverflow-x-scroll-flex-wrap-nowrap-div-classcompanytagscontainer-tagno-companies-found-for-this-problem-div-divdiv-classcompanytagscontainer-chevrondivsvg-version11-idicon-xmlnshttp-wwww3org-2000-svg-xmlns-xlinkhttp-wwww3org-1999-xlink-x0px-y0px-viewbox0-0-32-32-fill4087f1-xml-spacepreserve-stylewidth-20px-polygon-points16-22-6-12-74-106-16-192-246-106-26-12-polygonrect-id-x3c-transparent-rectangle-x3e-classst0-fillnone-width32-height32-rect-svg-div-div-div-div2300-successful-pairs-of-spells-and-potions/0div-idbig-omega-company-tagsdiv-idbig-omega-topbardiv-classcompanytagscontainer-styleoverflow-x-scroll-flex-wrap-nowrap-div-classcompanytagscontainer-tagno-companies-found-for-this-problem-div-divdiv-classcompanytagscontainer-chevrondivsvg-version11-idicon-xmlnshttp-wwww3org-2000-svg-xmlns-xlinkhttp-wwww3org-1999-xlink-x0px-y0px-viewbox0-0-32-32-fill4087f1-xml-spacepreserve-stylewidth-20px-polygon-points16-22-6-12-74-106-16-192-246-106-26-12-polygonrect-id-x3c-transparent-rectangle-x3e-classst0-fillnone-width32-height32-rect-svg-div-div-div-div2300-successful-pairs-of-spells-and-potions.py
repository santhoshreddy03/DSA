class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        
        res=[]
        for i in range(len(spells)):
            l,r=0,len(potions)-1
            c=len(potions)
            while l<=r:
                # print(c)
                m=(l+r)//2
                if spells[i]*potions[m]<success:
                    l=m+1
                else:
                    c=m
                    r=m-1
            # print(c,"---------")
            res.append(len(potions)-c)
            
        return res
        
        
        
        
        
        
        
        # pair=[]
        # for i in range(len(spells)):
        #     c=0
        #     for j in range(len(potions)):
        #         if spells[i]*potions[j]>=success:
        #             c+=1
        #     pair.append(c)
        # return pair
        