class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ms=0
        for i in accounts:
            s=sum(i)
            if ms<s:
                ms=s
        return ms
        