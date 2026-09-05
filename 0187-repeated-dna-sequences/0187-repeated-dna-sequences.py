class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dmap = {}
        res = []
        for i in range(10, len(s)+1):
            dmap[s[i-10:i]] = dmap.get(s[i-10:i],0) + 1

        for key, value in dmap.items():
            if int(value) > 1:
                res.append(key)
        
        return res