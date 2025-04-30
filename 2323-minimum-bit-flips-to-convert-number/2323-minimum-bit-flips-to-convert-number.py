class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        w=start^goal
        c=0
        while w!=0:
            c+=1
            w=w&w-1
        return c