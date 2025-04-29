class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        i=1
        while i<33:
            res=res<<1
            res=res|n&1
            n=n>>1
            i+=1
        return res
        print(int(res))
            

        