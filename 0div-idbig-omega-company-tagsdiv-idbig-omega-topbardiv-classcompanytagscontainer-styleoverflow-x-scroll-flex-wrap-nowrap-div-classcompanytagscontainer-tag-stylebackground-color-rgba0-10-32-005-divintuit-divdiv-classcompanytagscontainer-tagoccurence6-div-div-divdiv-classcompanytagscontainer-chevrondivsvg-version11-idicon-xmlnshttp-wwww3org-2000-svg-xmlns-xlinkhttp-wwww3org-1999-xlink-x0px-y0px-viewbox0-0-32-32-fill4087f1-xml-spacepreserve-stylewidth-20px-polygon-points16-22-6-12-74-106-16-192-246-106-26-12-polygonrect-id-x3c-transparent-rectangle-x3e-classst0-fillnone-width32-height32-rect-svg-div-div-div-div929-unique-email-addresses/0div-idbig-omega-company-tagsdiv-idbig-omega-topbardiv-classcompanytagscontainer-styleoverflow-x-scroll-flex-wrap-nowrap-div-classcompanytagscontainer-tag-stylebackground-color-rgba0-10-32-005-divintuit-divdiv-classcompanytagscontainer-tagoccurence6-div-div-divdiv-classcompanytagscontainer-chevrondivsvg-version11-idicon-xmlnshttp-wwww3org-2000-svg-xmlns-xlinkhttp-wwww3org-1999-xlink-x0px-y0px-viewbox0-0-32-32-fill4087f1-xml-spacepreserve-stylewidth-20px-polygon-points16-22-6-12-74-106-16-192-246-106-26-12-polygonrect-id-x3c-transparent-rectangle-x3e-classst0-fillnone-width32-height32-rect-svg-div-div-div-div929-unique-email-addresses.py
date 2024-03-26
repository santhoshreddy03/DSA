class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap=set()
        
        for e in emails:
            i,local=0,""
            while e[i] not in ["@", "+"]:
                if e[i] !=".":
                    local+=e[i]
                i+=1
            while e[i] not in["@"]:
                i+=1
            domain=e[i+1:]
            hashmap.add((local,domain))
        return len(hashmap)
        
        
        
        
#         hashset=set()
#         for i in emails:
#             local,domain=i.split("@")
#             local=local.split("+")[0]
#             local=local.replace(".","")
#             email=local + "@" + domain
#             hashset.add(email)

#         return len(hashset)
