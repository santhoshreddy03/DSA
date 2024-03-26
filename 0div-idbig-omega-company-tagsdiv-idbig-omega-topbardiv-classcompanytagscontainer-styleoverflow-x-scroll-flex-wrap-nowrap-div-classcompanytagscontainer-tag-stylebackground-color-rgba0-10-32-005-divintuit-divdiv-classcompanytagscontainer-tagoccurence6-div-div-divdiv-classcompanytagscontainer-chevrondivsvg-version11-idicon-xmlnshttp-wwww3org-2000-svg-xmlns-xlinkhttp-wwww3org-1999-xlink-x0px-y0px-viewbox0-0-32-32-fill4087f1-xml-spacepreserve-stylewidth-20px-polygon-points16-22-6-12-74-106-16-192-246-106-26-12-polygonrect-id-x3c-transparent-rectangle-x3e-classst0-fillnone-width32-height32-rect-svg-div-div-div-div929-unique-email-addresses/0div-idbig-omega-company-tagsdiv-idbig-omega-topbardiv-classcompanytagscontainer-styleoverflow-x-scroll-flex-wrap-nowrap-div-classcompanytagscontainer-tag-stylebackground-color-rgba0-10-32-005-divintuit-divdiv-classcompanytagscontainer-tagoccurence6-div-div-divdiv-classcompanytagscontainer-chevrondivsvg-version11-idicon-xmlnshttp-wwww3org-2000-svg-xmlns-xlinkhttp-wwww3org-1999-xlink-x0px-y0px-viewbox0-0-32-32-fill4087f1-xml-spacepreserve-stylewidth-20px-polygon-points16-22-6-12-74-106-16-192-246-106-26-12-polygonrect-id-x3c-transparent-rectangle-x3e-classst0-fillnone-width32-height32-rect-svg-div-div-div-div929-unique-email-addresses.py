class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap=set()
        for i in emails:
            local,domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            hashmap.add((local,domain))
        return len(hashmap)
        
        