class Solution:
    def frequencySort(self, s: str) -> str:
        c={}
        for i in range(len(s)):
            c[s[i]]=c.get(s[i],0)+1
        sc = sorted(c.items(), key=lambda item: item[1], reverse=True)
        d=""
        for i in range(len(sc)):
            d+=sc[i][0]*sc[i][1]
        return d
            

        