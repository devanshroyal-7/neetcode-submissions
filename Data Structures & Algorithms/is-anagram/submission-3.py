class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        
        hash_s = dict()
        hash_t = dict()

        for i in range(len(t)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 1
            else:
                hash_s[s[i]] += 1

            if t[i] not in hash_t:
                hash_t[t[i]] = 1
            else:
                hash_t[t[i]] += 1

        for i in hash_s:
            if i not in hash_t:
                return False
            
            if hash_s[i] != hash_t[i]:
                return False

        return True