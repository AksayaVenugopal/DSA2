class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res=start
        for i in range(1,n):
            t=start+2*i
            res=res^t
        return res
        