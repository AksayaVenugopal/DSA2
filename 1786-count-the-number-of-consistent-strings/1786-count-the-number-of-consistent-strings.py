class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s=0
        e=len(allowed)
        for i in words:
            if len(set(i)-set(allowed))==0:
                s+=1
        return s
        