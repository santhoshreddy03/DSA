class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashmap=set()
        for i in emails:
            local,domain=i.split("@")
            local=local.split("+")[0]
            local=local.replace(".","")
            email=local + "@" + domain
            hashmap.add(email)
        return len(hashmap)
        
        