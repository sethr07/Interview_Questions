class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []

        n = len(p)
        c1 = Counter(p)

        for i in range(len(s)):
            if abs(len(s)-i) < n:
                break
            sub = s[i:i+n]
            hashmap = Counter(sub)
            if hashmap == c1:
                res.append(i)

        return res        
