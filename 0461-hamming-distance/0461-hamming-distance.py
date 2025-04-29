class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r=x^y
        c=0
        while r!=0:
            c+=1
            r=r&r-1
        return c